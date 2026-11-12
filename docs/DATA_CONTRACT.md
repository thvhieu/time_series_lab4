# Data contract METR-LA
## Raw data
`data/traffic/METR-LA.h5`, Pandas HDF group `df`: 34272 timestamps × 207 sensor IDs.
Khoảng cách 5 phút, timestamps không mang timezone trong file; chưa tự gán timezone.
Giữ nguyên thứ tự sensor/target. Đơn vị tốc độ cần đối chiếu metadata benchmark trước khi gắn nhãn.

## Split và preprocessing
Split theo thời gian 70/15/15. Ghi cách làm tròn, mốc cuối mỗi tập và sensor set đã chốt.
Scaler/imputer chỉ fit train. Validation dùng chọn cấu hình/early stopping, test chỉ đánh giá cuối.
File không có NaN nhưng có 575302 số 0. Chốt mask và cách tính MAPE cho zero/near-zero;
không tự giả định 0 luôn là missing hoặc luôn quan sát hợp lệ. Báo số mẫu hợp lệ cho từng metric.

## Window và target
Tại origin t, input `[t-L+1,...,t]`; target vector tại t+3, t+6, t+12.
L chưa chốt: đề ghi `[t-12,...,t]` là 13 mốc, benchmark thường dùng 12. Leader cần quyết định và ghi rõ.
L là **bước 5 phút**, không phải giờ. Tensor LSTM `(samples,L,N)`, target có thể `(samples,3,N)`;
flatten cho XGBoost phải giữ schema. VAR dự báo đến bước12 rồi lấy 3/6/12.
Features rolling chỉ dùng quá khứ tại origin; không bê mean6h/std24h/trend của bài điện sang 5 phút mà không định nghĩa lại.
Chọn origin sao cho tất cả labels cần dùng còn trong cùng split: không để label train horizon12 vượt sang validation.
Nếu gap/missing, xác định đầy đủ khoảng thời gian thay vì chỉ dịch theo vị trí dòng.

## Backtest công bằng
Rolling origins: ở mỗi origin forecast cả 3/6/12 từ thông tin đã có, không dùng actual giữa origin và target
để hoàn thành một forecast multi-step. Sang origin tiếp theo mới dùng các quan sát thực lúc đó đã xuất hiện.
Model/scaler cố định trong lượt test mặc định. Refit là thí nghiệm khác phải chốt protocol chung.
Mọi mô hình cùng origin, sensor set, masks và thang đo. Subset chỉ dùng khi cả nhóm thống nhất và báo rõ.

## Outputs
Predictions: dataset,model,origin,target_timestamp,horizon_steps,sensor_id,y_true,y_pred,unit,valid_mask.
Metrics: model,horizon_steps,horizon_minutes,n_eval,RMSE,MAE,MAPE_pct,mask_policy,unit.
Metric riêng 15/30/60 phút, ghi cách aggregate trên toàn sensor set. Không claim so benchmark nếu khác protocol.
