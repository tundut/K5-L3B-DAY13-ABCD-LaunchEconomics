# Team

## Thông tin nhóm

- Tên nhóm: ABCD
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-ABCD-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `...` · nhánh `main` · commit `...`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Phan Tuấn Đức | 2A202603818 | 26ai.ducnpt@vinuni.edu.vn | tundut  | Người viết code + Người gắn nhãn 1 (Phụ trách định lượng & phân tích dữ liệu) |
|   2 | Huỳnh Văn Cường | 2A202603866 | 26ai.cuonghv@vinuni.edu.vn | cuong-huynh | Người kiểm số + Người gắn nhãn 2 kiêm giữ hồ sơ (Phụ trách thiết kế pilot & tổng hợp hồ sơ) |

> Nhóm có 2 thành viên nên gộp 4 vai chuẩn của lab như trên để chạy song song và tránh xung đột file. Sau giờ giải lao, Thành viên 2 chạy kiểm chéo lại `src/lab13.py` trên máy cá nhân để đảm bảo cả hai đều nắm vững phần tính chi phí và cỡ mẫu.

## Phân công chi tiết theo Checkpoint

| Giai đoạn | Thành viên 1 (Code & Định lượng + Gắn nhãn 1) | Thành viên 2 (Hồ sơ, Pilot & Kiểm số + Gắn nhãn 2) |
| --- | --- | --- |
| **Chuẩn bị (14:00–14:10)** | Cài `.venv` trong `src/`, cài `requirements.txt`, kiểm tra môi trường Python | Hoàn thiện thông tin nhóm trong `TEAM.md`, chuẩn bị khung các file trong `report/team/` |
| **CP1 · Nhiệm vụ A (14:10–14:53)** | Viết A1 (3 phép thử), A2 (`mo_hinh`), A3 (theo `loai`), A4 (chi phí cố định) trong `src/lab13.py`; xuất số liệu vào `report/team/bang_chi_phi.md` | Tính tay kiểm chéo số liệu A2/A4; viết nhận xét (≤ 3 dòng, có số) và kiểm nhãn `simulated`; cập nhật Mục 1 & Mục 3 vào `report/team/ho_so_launch_v0.md` |
| **CP2 · Nhiệm vụ B (14:53–15:20)** | Viết code độ nhạy B1 (9 kịch bản), B2 (đổi cặp), B3 (chi phí cả hệ thống 1/2/3 lần chạy), B4 (xem lại 100%); điền số vào `report/team/bang_chi_phi.md` | Xếp hạng 3 yếu tố nhạy nhất (B2), viết nhận xét B3 & B4; cập nhật Mục 2 vào `report/team/ho_so_launch_v0.md`; dựng sườn rủi ro kinh tế (E2) trong `report/team/chi_so.md` |
| **CP3 · Nhiệm vụ C (15:35–16:08)** | Gắn nhãn độc lập 20 ca lỗi trong 8 phút (không trao đổi); sau khi so nhãn, chuyển sang code D1 (cỡ mẫu) và tỉ lệ `mo_lai_trong_7_ngay` | Gắn nhãn độc lập 20 ca lỗi trong 8 phút (không trao đổi); so nhãn (≥ 80%), viết quy tắc cho ca lệch, hoàn thiện bảng khắc phục 5 ca vào `report/team/bang_loi.md` và Mục 5 `ho_so_launch_v0.md` |
| **CP4 · Nhiệm vụ D (16:08–16:36)** | Hoàn thiện code D1 & tính thử 3 chỉ số E1; kiểm tra `yaml.safe_load` và kiểm không còn dấu `?` trong `pilot_plan.yaml` | Điền toàn bộ `report/team/pilot_plan.yaml` (chú thích D1, 5 câu D2, phương án chia cụm, ≥ 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`); cập nhật Mục 6 `ho_so_launch_v0.md` |
| **CP5 · Nhiệm vụ E (16:36–17:00)** | Soạn bảng chỉ số E1, danh sách ≥ 6 event có `trace_id` và kiểm tra chéo chỉ số–event trong `report/team/chi_so.md` | Hoàn thiện bảng rủi ro kinh tế (E2) trong `report/team/chi_so.md`; hoàn thiện Mục 4, Mục 7 và Đề xuất cuối trong `report/team/ho_so_launch_v0.md`; rà lỗi `production` và nhãn `simulated` |
| **Duyệt chéo Gate 2a (17:00–17:45)** | Soi số liệu, độ nhạy, cỡ mẫu của nhóm được chấm; trả lời câu hỏi phản biện về mô hình chi phí & cỡ mẫu | Soi phạm vi, nhãn `simulated`, luật dừng & đề xuất của nhóm được chấm; ghi `report/team/phieu_cham.md`; trình bày 1 phút hồ sơ nhóm |
| **Đóng gói & Nộp (17:45–18:00)** | Viết báo cáo cá nhân `report/team/MSSV_HoTen.md`, rà soát checklist kỹ thuật, push commit | Chạy kiểm chéo `src/lab13.py` trên máy cá nhân, hoàn thiện `report/team/group_report.md`, `TEAM.md` và báo cáo cá nhân; cả 2 nộp link repo lên LMS |

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## Nguyễn Phan Tuấn Đức — 2A202603818

### Phần việc phụ trách

- Thiết lập môi trường Python, viết và chạy toàn bộ code phân tích (`src/lab13.py`) cho Nhiệm vụ A, B, D1 và số liệu E1.
- Điền các bảng định lượng trong `report/team/bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca lỗi (Người gắn nhãn 1) ở Nhiệm vụ C.
- Soạn danh sách event có `trace_id` và kiểm tra chéo chỉ số–event trong `report/team/chi_so.md`.
- Kiểm tra kỹ thuật `report/team/pilot_plan.yaml` (`yaml.safe_load`, không còn dấu `?`) và phản biện phần số liệu trong phiên duyệt chéo Gate 2a.

### Đóng góp cụ thể

- (Cập nhật sau khi hoàn thành từng checkpoint)

### Bằng chứng

- `src/lab13.py`
- `report/team/bang_chi_phi.md`
- `report/team/bang_loi.md` (bộ nhãn độc lập Người 1)
- `report/team/chi_so.md` (phần E1 & danh sách event)
- `report/team/MSSV_HoTen.md` (báo cáo cá nhân)

## Huỳnh Văn Cường — 2A202603866

### Phần việc phụ trách

- Kiểm tra chéo số liệu định lượng, viết nhận xét ngắn (≤ 3 dòng, có số) và kiểm soát nhãn `simulated` trong `report/team/bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca lỗi (Người gắn nhãn 2), tính đồng thuận và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Thiết kế và điền hoàn chỉnh `report/team/pilot_plan.yaml` (D2, D3, luật dừng).
- Hoàn thiện bảng rủi ro kinh tế (E2) trong `report/team/chi_so.md` và giữ/cập nhật liên tục trang tổng hợp `report/team/ho_so_launch_v0.md`.
- Hoàn thiện `report/team/phieu_cham.md`, `report/team/group_report.md`, `TEAM.md` và chạy kiểm chéo `src/lab13.py` trên máy cá nhân trước khi nộp.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C (bộ nhãn Người 2 trong `report/team/bang_loi.md`).
- Tính đồng thuận (19/20 = 95%), viết quy tắc phân biệt ca lệch và hoàn thiện bảng khắc phục 5 ca.
- Thiết kế pilot: tính D1 (cỡ mẫu 3 cách chia, chọn chia theo yêu cầu 1.251/nhóm), trả lời D2, điền `report/team/pilot_plan.yaml` gồm 3 luật dừng.
- Hoàn thiện E2 trong `report/team/chi_so.md` (4 rủi ro kinh tế có số) và trang `report/team/ho_so_launch_v0.md` (đề xuất Go có điều kiện).
- Tạo báo cáo cá nhân `report/team/2A202603866_Cuong.md`.

### Bằng chứng

- `report/team/bang_loi.md` (bộ nhãn độc lập Người 2 & bảng khắc phục)
- `report/team/pilot_plan.yaml`
- `report/team/chi_so.md` (phần E2)
- `report/team/ho_so_launch_v0.md`
- `report/team/phieu_cham.md`, `report/team/group_report.md`, `TEAM.md`
- `report/team/MSSV_HoTen.md` (báo cáo cá nhân)
