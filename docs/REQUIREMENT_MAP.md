# Phạm vi theo dữ liệu nhóm chọn
**Đang triển khai:** METR-LA, mục Traffic Forecasting của PDF; 207 sensor, 5 phút, horizon 15/30/60 phút.
Nhóm giữ ý tưởng so sánh VAR/XGBoost/LSTM cho dữ liệu traffic như kế hoạch phân công.

| ID | Nội dung | Chủ trì |
|---|---|---|
| T01 | File dữ liệu gốc và sensor/timestamp manifest | Đã đưa vào repo; TV2 kiểm tra sử dụng |
| T02 | Window/split/scaler/mask, tránh leakage | TV2 |
| T03 | VAR và giới hạn đa biến | TV3 |
| T04 | XGBoost và features | TV4 |
| T05 | LSTM và overfitting | TV5 |
| T06 | Multi-horizon backtesting | TV6 |
| T07 | RMSE/MAE/MAPE theo 15/30/60 phút | TV6 |
| T08 | Tích hợp/giải thích/giới hạn | TV1 + cả nhóm |

**Không coi là đã hoàn thành bằng METR-LA:** phần điện + temperature/humidity/wind_speed trong PDF,
các đồ thị/câu hỏi weather, cửa sổ điện 24×4 và Dense(1) cho load. Không gắn nhãn tốc độ sensor thành load/weather.
Các câu hỏi có thể thảo luận cho traffic: VAR thất bại khi nào, XGBoost học lag/sensor nào,
LSTM overfit không, giới hạn lookback và khác biệt ML/DL. Không bịa câu trả lời weather.
