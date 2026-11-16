# Phân công Lab4 METR-LA — 6 người

Dataset đã có (`data/traffic/METR-LA.h5`). Toàn bộ 6 phần đã hoàn thành và đồng bộ theo cùng protocol (`5` sensors đầu tiên `['773869', '767541', '767542', '717447', '717446']`, `L = 12` bước = 60 phút, `horizons = [3, 6, 12]` bước = 15/30/60 phút, split `70/15/15`, `mask_policy = y_true > 0`).

| Người | Phần | Bàn giao |
|---|---|---|
| TV1 — `thvhieu` (Leader) | [Bạn — leader và tích hợp](contributions/01_leader_integration.ipynb) | Config/protocol đã thống nhất, bảng tiến độ, nhận xét tổng hợp, notebook cuối chạy từ kernel mới. |
| TV2 — `mquyen-kkk` | [Preprocessing và tạo features](contributions/02_preprocessing_features.ipynb) | Split timestamps, sensor order, mask policy, scaler, feature schema, tensor shapes 3D/2D và target origin/horizon arrays. |
| TV3 — `lengocanh270706-maker` | [VAR baseline](contributions/03_var.ipynb) | Sensor set, kiểm định ADF, lag AIC/BIC (`p=12`), cấu hình/code fit, inverse và forecasts `h=3/6/12`. |
| TV4 — `lamhuwng` | [XGBoost](contributions/04_xgboost.ipynb) | Feature order (75 features), chiến lược Direct, config/best_iteration, code và bảng forecasts. |
| TV5 — `huyhoangdeptrai210-dotcom` | [LSTM](contributions/05_lstm.ipynb) | Input/output shapes `(samples, 12, 7)`, kiến trúc `LSTM(64)->LSTM(32)->Dense`, loss curves, code inverse và forecasts. |
| TV6 — Thành viên 6 | [Backtesting và đánh giá](contributions/06_backtesting_evaluation.ipynb) | Predictions gắn origin/target/sensor/horizon, RMSE/MAE/MAPE theo horizon, valid counts (`n_eval`), đồ thị và nhận xét. |

## Phụ thuộc và làm song song
- TV1 chốt sensor set/L/protocol, TV2 chuẩn bị đầu vào từ file có sẵn.
- TV3/TV4/TV5 chuẩn bị khung trước, train song song sau khi nhận data contract từ TV2.
- TV6 chuẩn bị metrics/schema trước; so sánh cuối tổng hợp forecasts từ cả 3 mô hình.
- TV1 tích hợp vào [Lab4_Multivariate.ipynb](Lab4_Multivariate.ipynb); từng người tự review và giải thích phần mình.

## Mốc hoàn thành
1. Chốt `L = 12`, subset 5 sensors, đơn vị `mph`, mask `y_true > 0` và split `70/15/15` — Đã hoàn thành.
2. TV2 bàn giao data windows/scaler/schema — Đã hoàn thành.
3. TV3/TV4/TV5 bàn giao code/config/forecasts — Đã hoàn thành.
4. TV6 metric/đồ thị, TV1 tích hợp và cả nhóm review — Đã hoàn thành.

## Điều kiện hoàn thành
- [x] Cùng origin/sensor/mask/horizon, đúng đơn vị và inverse.
- [x] Scaler/tuning không học test; không đưa actual tương lai vào forecast horizon.
- [x] Forecast đủ phạm vi đã chốt; dùng subset 5 sensors và ghi rõ, không báo là toàn 207 sensor.
- [x] Có code chạy lại, cấu hình và nhận xét, không chỉ gửi ảnh.
- [x] Không đưa phần present vào repo Lab4.
