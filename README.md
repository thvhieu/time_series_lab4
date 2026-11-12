# time_series_lab4 — METR-LA

Lab4 Traffic Forecasting cho **6 người**, **TV1 là bạn/leader**. Code bài làm giữ dạng **TODO**.
Dataset đã được đưa vào repo: `data/traffic/METR-LA.h5`, không cần tìm hoặc ghép dữ liệu mới.

## Bắt đầu
```bash
git clone https://github.com/thvhieu/time_series_lab4.git
cd time_series_lab4
python -m venv .venv
```
Windows / PowerShell:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```
Người chạy LSTM cài thêm `requirements-lstm.txt`. Dùng Python 3.12.
macOS/Linux dùng `.venv/bin/python` thay đường dẫn Windows.

## File quan trọng
- [Notebook tổng hợp](Lab4_Multivariate.ipynb)
- [Phân công 6 người](PHAN_CONG_6_NGUOI.md)
- [6 notebook riêng](contributions/README.md)
- [Data contract / chống leakage](docs/DATA_CONTRACT.md)
- [Nguồn và kiểm tra dữ liệu](docs/DATA_SOURCES.md)
- [Phạm vi so với PDF](docs/REQUIREMENT_MAP.md)
- [Đề gốc](resources/practice_4.pdf)

## Dataset đã kiểm tra
- Shape **34.272 × 207**, timestamps từ **2012-03-01 00:00** đến **2012-06-27 23:55**.
- Cách nhau 5 phút, không trùng timestamps, không có NaN/Inf trong block dữ liệu.
- Có **575.302 giá trị 0**; không vì không có NaN mà coi như không cần missing/zero policy.
- [Manifest/hash](data/traffic/manifest.json) và [kết quả kiểm tra](data/traffic/inspection.json).
- File gốc giữ nguyên byte. Chưa train mô hình hoặc có kết quả forecast.

## Phạm vi đang làm
Theo lựa chọn của nhóm, repo tập trung **METR-LA/Traffic**, horizon **3/6/12 bước = 15/30/60 phút**.
Không còn nhiệm vụ tìm/tải/ghép electricity-weather. METR-LA không chứa các cột weather của phần điện trong PDF;
khung này không tự coi phần điện/weather đã hoàn thành bằng dữ liệu traffic.
Lookback L để leader chốt: PDF viết `[t-12,...,t]` là 13 quan sát nếu lấy cả hai đầu; nếu định dùng 12 cần ghi rõ.

## Kiểm tra trước khi bàn giao
```bash
python scripts/check_notebooks.py --todo-only
python scripts/check_data.py
```
Khi đã viết code, bỏ `--todo-only`. Đây là validator cấu trúc/data, không phải kiểm thử chất lượng mô hình.
Mỗi người tự viết code/nhận xét phần mình; leader tích hợp, không làm thay tất cả.
Phần present không nằm trong repo. `_checks`, cache, môi trường và outputs thử không được commit.
