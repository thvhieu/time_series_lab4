# Làm việc qua Git
Mỗi người làm file riêng và nhánh riêng. Không sửa chồng notebook tổng hợp.
TV1 là người dùng/leader, TV2 preprocessing, TV3 VAR, TV4 XGBoost, TV5 LSTM, TV6 đánh giá.
Dataset có sẵn; chỉ đọc file HDF, không sửa raw hoặc tự thay sensor/time split.
Gửi PR có code/config/nhận xét và mẫu HANDOFF; merge file không tự tích hợp nội dung notebook.
Giữ code TODO trong scaffold ban đầu. Khi làm xong, chạy từ kernel mới và bỏ --todo-only khi validate.
Chỉ đưa raw METR-LA đã xác nhận lên Git, không đưa model/checkpoints/cache/output thử hay credential.
