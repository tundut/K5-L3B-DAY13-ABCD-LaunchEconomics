# Báo cáo cá nhân — ThanhVien1-MSSV

## 1. Thông tin thành viên

- Họ tên: Nguyễn Phan Tuấn Đức
- MSSV: 2A202603818
- Email: ducnguyenphan05@gmail.com
- GitHub: tundut
- Vai trong nhóm: **Người viết code + Người gắn nhãn 1** (Phụ trách định lượng & phân tích dữ liệu)

## 2. Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) và triển khai toàn bộ chương trình phân tích `src/lab13.py` cho Nhiệm vụ A (A1–A4), Nhiệm vụ B (B1–B4), Nhiệm vụ D1 (tính cỡ mẫu và tỉ lệ mở lại 7 ngày) và Nhiệm vụ E1 (tính thử 3 chỉ số).
- Tổng hợp bảng số liệu định lượng, gắn nhãn `simulated` và viết nhận xét ngắn (≤ 3 dòng, có số) trong `report/team/bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (bộ nhãn Người gắn nhãn 1) trong `report/team/bang_loi.md`.
- Hoàn thiện đặc tả chỉ số (E1), danh sách 10 event có `trace_id` và kiểm tra chéo chỉ số–event trong `report/team/chi_so.md`.
- Phân công công việc cho nhóm 2 người trong `TEAM.md` và kiểm soát kỹ thuật trước khi chuyển giao cho Thành viên 2.

## 3. Đóng góp cụ thể

- **Thiết lập & phân công:** Khởi tạo bảng phân công 2 người theo từng checkpoint trong `TEAM.md`, cài đặt `pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml` vào `src/.venv`.
- **Nhiệm vụ A (CP1):** Viết 3 hàm A1 đạt 100% phép thử biết trước (`1,20 · 1,25 · 1,25`); viết `mo_hinh(...)` với `keep_default_na=False`, tính được chi phí mỗi việc thành công là **4.472 đ** (`simulated`, gấp **16,3 lần** hoá đơn token+tool 274,7 đ/yêu cầu), chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** (`simulated`); tách 4 loại yêu cầu (A3) chỉ ra `quoc_te` tốn **22.515 đ = 1,88×** và tỉ lệ `ok` tụt từ 30,0% → 11,4% → 2,2%; cộng chi phí cố định 40 triệu/tháng cho `noi_dia + hang_nang` (A4: **4.599 đ = 0,38×** ở 45.000 yc/tháng và **5.784 đ = 0,48×** ở một nửa khối lượng, `simulated`).
- **Nhiệm vụ B (CP2):** Chạy đủ 9 kịch bản độ nhạy (B1), kịch bản kết hợp token×2 + xem lại×2 (B2: **6.543 đ**, `+46,3%`, `simulated`), xác định top 3 yếu tố nhạy nhất (1. Làm lại, 2. Xem lại, 3. Lương nhân viên); tính chi phí cả hệ thống cho giới hạn 1/2/3 lần chạy (B3: rẻ nhất ở **2 lần** với **6.901.220 đ**, `simulated`); tính kịch bản xem lại 100% (B4: **11.743 đ = 0,98×** với 9 phút làm lại và **12.415 đ = 1,03×** với trung bình dữ liệu 15,3 phút, `simulated`).
- **Nhiệm vụ C (CP3):** Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và hoàn thành bộ nhãn độc lập của Người gắn nhãn 1 trong `report/team/bang_loi.md`.
- **Nhiệm vụ D1 & E1 (CP4–CP5):** Tính đủ 5 câu cỡ mẫu D1 (`1.251`; `3.103 / 42 người`; tối đa `1.000`; tối đa `300`; MDE 6 điểm `n=859` → `m ≥ 299`, `DE=6,96`, power ở 5 điểm = `0,64`), tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn bộ; `3,97%` trong phạm vi), 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`) và thiết kế 10 event có `trace_id` kèm kiểm tra chéo trong `report/team/chi_so.md`.

## 4. Bằng chứng

- `TEAM.md` (commit `b0d0e2e` — phân công chi tiết cho nhóm 2 người).
- `src/lab13.py` (chạy hoàn chỉnh từ đầu đến cuối, in `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A2, A3, A4, B1–B4, D1, E1).
- `report/team/bang_chi_phi.md` (đủ bảng A1–A4, B1–B4, đủ nhãn `simulated`).
- `report/team/bang_loi.md` (bộ nhãn độc lập 20 ca của Người gắn nhãn 1).
- `report/team/chi_so.md` (đặc tả chỉ số E1, 10 event có `trace_id`, kiểm tra chéo chỉ số ↔ event).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI lập trình tích hợp trong IDE (Antigravity / Gemini).
- **Mục đích sử dụng:** Tóm tắt yêu cầu đề bài, gợi ý phân chia công việc cho nhóm 2 người, hỗ trợ viết khung code `src/lab13.py`, định dạng bảng markdown và kiểm tra lỗi quy tắc (nhãn `simulated`, quy tắc 5 về phạm vi Gate 2a, giới hạn 3 dòng).
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `src/.venv/bin/python lab13.py` trên dữ liệu gốc `logix_runs.csv` và `logix_requests.csv` (không sửa dữ liệu), kiểm tra đạt 100% ba phép thử A1 (`1,20 · 1,25 · 1,25`).
  - Đối chiếu toàn bộ con số đầu ra (A2, A3, A4, B1–B4, D1, E1) với tài liệu `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%, nằm hoàn toàn trong ngưỡng 2%).
  - Kiểm tra tính nhất quán tuyến tính của bảng độ nhạy (kịch bản giảm một nửa bằng đúng nửa mức tăng của kịch bản gấp đôi) và rà soát toàn bộ `report/team/` theo quy tắc 5 để đảm bảo không vi phạm.
  - Hiểu và tự giải thích được 3 câu hỏi cốt lõi: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm ca thành công, công thức cỡ mẫu hiệu dụng khi chia theo cụm ($n_{\text{hiệu dụng}} = c \cdot m / DE < c / ICC$), và lý do phạm vi pilot chỉ gồm `noi_dia + hang_nang`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng tiến độ và chính xác các phần việc định lượng, lập trình và hồ sơ kỹ thuật được phân công cho Thành viên 1.
- Các file bàn giao sạch sẽ, không xung đột để Thành viên 2 tiếp tục hoàn thiện Nhiệm vụ C (so nhãn & bảng khắc phục), Nhiệm vụ D (`pilot_plan.yaml`), Nhiệm vụ E2 (`chi_so.md`) và tổng hợp `ho_so_launch_v0.md`.
- Mức hoàn thành phần việc cá nhân: **100%**.
