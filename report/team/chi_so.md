# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai == 1` | Chỉ số trong đợt chạy thử là **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51 / 1.200); trong phạm vi `noi_dia` + `hang_nang` là **3,97%** (39 / 982) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu thuộc nhóm can thiệp có mở gợi ý của trợ lý | Số yêu cầu có event `agent_suggestion_shown` chia tổng số yêu cầu của nhóm can thiệp (`arm == treatment`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần | Số đơn có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn được kiểm tra mẫu (`audit_sample_checked`, nhằm bắt lỗi ngầm) | Không cần tính |

Lưu ý: Chỉ ghi "chỉ số trong đợt chạy thử là …", không khẳng định "trợ lý đã nâng chỉ số" vì đợt chạy thử 2 tuần chưa có nhóm đối chứng.

## Danh sách event

Mỗi event đều gắn `trace_id` để nối xuyên suốt với trace của agent và sổ cái hoàn phí.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách hàng | `request_id`, `loai`, `so_tien_vnd`, `depot`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý hoàn phí (Agent) | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất xử lý lại ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Trợ lý hoàn phí (Agent) | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi ticket yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Kế toán / Kiểm soát chất lượng | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `bang_gia_version`, `trace_id` | Khi kiểm tra mẫu đối soát hằng tuần |

**Kiểm tra chéo (chỉ số ↔ event):**
- **Chỉ số chính (% đóng trong 24h & không mở lại 7 ngày):** tính từ `refund_request_created` (mốc tạo yêu cầu), `ticket_closed` (`closed_at - created_at <= 24h`) và không có `ticket_reopened` trong 7 ngày nối qua `trace_id`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** tính từ `staff_review_decision` (số event có `quyet_dinh` là `sua` hoặc `bo` chia tổng số `staff_review_decision`).
- **Chỉ số an toàn — Tỉ lệ mở lại trong 7 ngày:** tính từ `ticket_reopened` (trong 7 ngày sau `ticket_closed`) chia tổng số `refund_request_created`.
- **Chỉ số dùng đề xuất (% mở gợi ý ở nhóm can thiệp):** tính từ `agent_suggestion_shown` chia `refund_request_created` có `arm == treatment`.
- **Chỉ số an toàn đề xuất (% hoàn sai tiền qua kiểm mẫu):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số event kiểm mẫu).
- **Chi phí thật thay thế cột `_simulated` trong pilot:** tính từ `agent_run_completed` (token, tool), `staff_review_decision` (`phut_xem_lai` đo thật) và `staff_rework_completed` (`phut_lam_lai` đo thật).

## E2 · Rủi ro kinh tế

*(Phần Thành viên 2 hoàn thiện: điền ít nhất 2 dòng lấy số từ `bang_chi_phi.md` — gợi ý: số ca làm lại gấp đôi +51,8% lên 6.787 đ [simulated]; xem lại 100% kéo dài 11.743–12.415 đ = 0,98–1,03× [simulated]; khối lượng giảm một nửa làm chi phí cố định tăng từ 1.185 đ lên 2.370 đ/việc [simulated].)*

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
