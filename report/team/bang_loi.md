# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên 1 · Người gắn nhãn 2: Thành viên 2 (gắn độc lập trong 8 phút, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 2 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Trùng | Ngầm |
| 6 | Ngữ cảnh | Do người dùng | Lệch | Ngữ cảnh |
| 7 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 8 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 9 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Trùng | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Trùng | Do người dùng |
| 15 | Hệ thống | Hệ thống | Trùng | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Trùng | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Trùng | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Trùng | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95% (đạt ngưỡng 80%)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 6 (lệch): Người 1 gắn **Ngữ cảnh**, Người 2 gắn **Do người dùng**. Quy tắc thống nhất: nếu lựa chọn của khách mâu thuẫn trực tiếp với nội dung mô tả đơn (chọn "giao trễ" nhưng nội dung là "hàng vỡ"), gắn **Ngữ cảnh** vì hệ thống có đủ dữ liệu để hỏi lại làm rõ thay vì xử lý theo nhãn khách tự chọn; chỉ gắn Do người dùng khi khách nhập sai dữ liệu mà hệ thống không thể suy ra ý đúng (ví dụ ca 1, 9).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua` lỗi từ ngân hàng > 2 ca/tuần, hoặc tỉ lệ yêu cầu lỗi định dạng STK > 1% | Validate định dạng STK ngay khi khách nhập, báo lỗi tại chỗ kèm ví dụ; không tạo lệnh hoàn khi STK chưa hợp lệ | Nhân viên CSKH (quy trình) + Kỹ sư sản phẩm (validate) |
| 7 | Hệ thống | Cảnh báo khi API sổ cái trả 5xx > 1% số lần gọi trong 15 phút; đối chiếu `refund_ledger_write` với thông báo đã gửi khách hằng ngày | Chỉ báo "đã hoàn tiền" sau khi `refund_ledger_write` thành công; thêm trạng thái "đang xử lý" khi retry | Kỹ sư tích hợp sổ cái |
| 10 | Ngữ cảnh | Tỉ lệ `ticket_reopened` có lý do "bất khả kháng/chính sách" > 3% số yêu cầu loại `noi_dia` trong tuần | Hiển thị điều khoản bất khả kháng và ngoại lệ "cam kết 24 giờ" ngay trong màn hình yêu cầu; nhân viên xử lý ca biên có checklist riêng | Trưởng ca CSKH |
| 11 | Giới hạn hệ thống | Đếm event tin nhắn thoại (`refund_request_created` có cờ `voice`) > 5% tổng yêu cầu trong tuần | Chuyển ngay tin nhắn thoại cho nhân viên kèm bản chép tự động (STT) hoặc nút "gọi lại"; không để trợ lý trả lời mẫu cụt | Product owner trợ lý |
| 5 | Ngầm | `audit_sample_checked` có `so_tien_da_hoan != so_tien_dung` > 0,5% số đơn kiểm tra mẫu trong tuần | Thêm bước kiểm tra mã giảm giá/phiên bản bảng giá trước khi hoàn; chặn hoàn nếu đơn có mã KM mà giá hoàn = giá gốc | Kiểm soát chất lượng (đối soát) |
