# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ABCD · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công, gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); gấp 0,37× mức nhân viên tự làm 12.000 đ | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1% khi tăng 25%) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× mức 12.000 đ; thêm chi phí cố định 40 triệu đ/tháng vẫn chỉ 0,38–0,48× | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200); dùng — tỉ lệ bỏ qua gợi ý 27,12% (48/177); an toàn — lỗi lọt đến khách 4,25% (51/1.200), trong phạm vi pilot 3,97% (39/982) | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi, đồng thuận 19/20 = 95%; 5 cách khắc phục đủ 5 loại, mỗi cách có event/ngưỡng đo được và một vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 6 · Pilot plan | Chia ngẫu nhiên theo yêu cầu, 1.251 yêu cầu/nhóm, MDE đúng +5 điểm; 3 luật dừng có ngưỡng–thời hạn–quyền dừng | Xong, có bằng chứng | Người gắn nhãn 2 kiêm giữ hồ sơ |
| 7 · Rủi ro kinh tế | 4 rủi ro có số: làm lại gấp đôi +51,8% (6.787 đ); xem lại 100% chỉ còn 0,98–1,03×; khối lượng giảm nửa đẩy chi phí cố định/việc từ 1.185 đ lên 2.370 đ | Giả lập | Người gắn nhãn 2 kiêm giữ hồ sơ |

**Đề xuất:** Go có điều kiện.

- Điều kiện 1 — Chỉ chạy pilot trong phạm vi `noi_dia` + `hang_nang`, loại `quoc_te` (22.515 đ/việc = 1,88×) và `doi_tac` (10.215 đ/việc = 0,85×, điều khoản riêng) theo kết quả A3; người phụ trách: Trưởng ca CSKH; kiểm tra: cuối tuần 1 của pilot.
- Điều kiện 2 — Hoàn tất pilot theo `pilot_plan.yaml` (20 nhân viên/nhóm, MDE 6 điểm, 3 luật dừng); nếu chỉ số an toàn vượt 6,0% trong 7 ngày liên tiếp hoặc chi phí đo thật > 12.000 đ trong 2 tuần liên tiếp thì dừng; người phụ trách: Trưởng ca CSKH; kiểm tra: mỗi tuần trong pilot.
- Điều kiện 3 — Trước khi mở rộng, chi phí mỗi việc thành công đo bằng số liệu thật (token, tool, phút xem/làm lại đo thật) phải < 12.000 đ và tỉ lệ xem lại không đẩy hoà vốn dưới 4,8 phút/ca; người phụ trách: Người kiểm số; kiểm tra: báo cáo kết thúc pilot, Gate 2b.
