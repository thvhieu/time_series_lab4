# Phân công Lab4 METR-LA — 6 người

Dataset đã có. Bỏ nhiệm vụ tìm/tải/ghép dữ liệu. Tên TV2–TV6 và ngày/giờ: TODO.

| Người | Phần | Bàn giao |
|---|---|---|
| TV1 — Bạn/leader | [Bạn — leader và tích hợp](contributions/01_leader_integration.ipynb) | Config/protocol đã thống nhất, bảng tiến độ, nhận xét tổng hợp, notebook cuối chạy từ kernel mới. |
| TV2 — TODO tên | [Preprocessing và tạo features](contributions/02_preprocessing_features.ipynb) | Split timestamps, sensor order, mask policy, scaler, feature schema, tensor shapes và target origin/horizon arrays. |
| TV3 — TODO tên | [VAR baseline](contributions/03_var.ipynb) | Sensor set, phép xử lý, lag/AIC/BIC, cấu hình/code fit, inverse và forecasts h=3/6/12. |
| TV4 — TODO tên | [XGBoost](contributions/04_xgboost.ipynb) | Feature order, chiến lược multi-output/direct/recursive, config/best_iteration, code và bảng forecasts. |
| TV5 — TODO tên | [LSTM](contributions/05_lstm.ipynb) | Input/output shapes, kiến trúc/seed/epochs/checkpoint, loss curves, code inverse và forecasts. |
| TV6 — TODO tên | [Backtesting và đánh giá](contributions/06_backtesting_evaluation.ipynb) | Predictions gắn origin/target/sensor/horizon, RMSE/MAE/MAPE theo horizon, valid counts, đồ thị và nhận xét. |

## Phụ thuộc và làm song song
- TV1 chốt sensor set/L/protocol, TV2 chuẩn bị đầu vào từ file có sẵn.
- TV3/TV4/TV5 chuẩn bị khung trước, train song song sau khi nhận data contract từ TV2.
- TV6 chuẩn bị metrics/schema trước; so sánh cuối cần forecasts từ cả 3 mô hình.
- TV1 tích hợp; từng người tự review và giải thích phần mình.

## Mốc (chưa có ngày cụ thể)
1. Chốt L, sensor set, đơn vị/mask và split — TODO ngày/giờ.
2. TV2 bàn giao data windows/scaler/schema — TODO ngày/giờ.
3. TV3/TV4/TV5 bàn giao code/config/forecasts — TODO ngày/giờ.
4. TV6 metric/đồ thị, TV1 tích hợp và cả nhóm review — TODO ngày/giờ.

## Điều kiện hoàn thành
- [ ] Cùng origin/sensor/mask/horizon, đúng đơn vị và inverse.
- [ ] Scaler/tuning không học test; không đưa actual tương lai vào forecast horizon.
- [ ] Forecast đủ phạm vi đã chốt; dùng subset thì ghi rõ, không báo là toàn 207 sensor.
- [ ] Có code chạy lại, cấu hình và nhận xét, không chỉ gửi ảnh.
- [ ] Không đưa phần present vào repo Lab4.
