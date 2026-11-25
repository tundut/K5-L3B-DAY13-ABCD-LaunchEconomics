# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: ABCD
- Lớp: L3B
- Thành viên: xem `TEAM.md`
- Repo: `K5-L3B-DAY13-ABCD-LaunchEconomics`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN trước cổng Gate 2a: trả lời bốn câu hỏi — có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra quyết định. Nhóm 2 người chia đôi: Thành viên 1 viết code `src/lab13.py` và định lượng; Thành viên 2 kiểm số, gắn nhãn độc lập, thiết kế pilot và giữ hồ sơ.

## 3. Giải pháp

- **A–B (chi phí & độ nhạy):** `src/lab13.py` tính mô hình chi phí từ trace; kết quả trong `report/team/bang_chi_phi.md`.
- **C (lỗi):** hai người gắn nhãn độc lập 20 ca theo Google PAIR; đồng thuận và bảng khắc phục trong `report/team/bang_loi.md`.
- **D (pilot):** `report/team/pilot_plan.yaml` — chia ngẫu nhiên theo yêu cầu, 1.251/nhóm, MDE +5 điểm, 3 luật dừng.
- **E (chỉ số & hồ sơ):** đặc tả chỉ số + event + rủi ro kinh tế trong `report/team/chi_so.md`; trang một mục trong `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

- Chi phí mỗi việc thành công: **4.472 đ** (`simulated`), gấp 16,3 lần hoá đơn token chia số yêu cầu; chi phí cả hệ thống 5.865 đ/yêu cầu = **0,49×** mức nhân viên tự làm (`simulated`).
- Phạm vi đề xuất: chỉ `noi_dia` + `hang_nang`; loại `quoc_te` (1,88×) và `doi_tac` (0,85×, điều khoản riêng).
- Chỉ số trong đợt chạy thử: chính **82,83%**, chỉ số dùng (bỏ qua gợi ý) **27,12%**, chỉ số an toàn (lỗi lọt khách) **4,25%**.
- Đề xuất cuối: **Go có điều kiện** — điều kiện phạm vi, điều kiện hoàn tất pilot theo `pilot_plan.yaml`, điều kiện chi phí đo thật < 12.000 đ trước khi mở rộng.
- Kết quả duyệt chéo của hội đồng: (ghi sau buổi duyệt chéo Gate 2a).

## 5. Khó khăn và cách xử lý

- Số liệu chi phí phụ thuộc cột `_simulated` nên mọi kết luận gắn nhãn `simulated` và pilot phải đo lại bằng số liệu thật trước khi mở rộng.
- Chia cụm theo nhân viên/depot không đủ cỡ mẫu (tối đa 1.000 và 300 hiệu dụng < 1.251), nên chọn chia theo yêu cầu và giảm nhiễu bằng phân tầng depot.
- Một ca gắn nhãn lệch giữa hai người (ca 6) — đã thống nhất quy tắc: lựa chọn của khách mâu thuẫn nội dung đơn thì gắn Ngữ cảnh.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và báo cáo cá nhân `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- Cột phút xem lại/làm lại là giả lập; pilot cần đo `phut_xem_lai`/`phut_lam_lai` thật — nếu trung bình > 4,8–5,1 phút/ca thì trợ lý không còn lợi thế chi phí.
- MDE +5 điểm chỉ đủ phát hiện ở mức yêu cầu; nếu cần kết luận theo depot thì phải kéo dài pilot hoặc chấp nhận MDE lớn hơn.
- Đợt chạy thử 2 tuần chưa có đối chứng nên mọi chỉ số chỉ là "chỉ số trong đợt chạy thử", chưa kết luận nhân quả.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels: `stats.power.NormalIndPower`, `proportion_effectsize`
