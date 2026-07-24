# Báo Cáo Phân Tích Sâu (Deep-Dive Report)

**Tên Nhóm:** Nhóm ABC  
**Số lượng:** 06 Thành viên
1. Thành viên 1: Nguyễn Trọng Đức - 2A202601673
2. Thành viên 2: Nguyễn Đào Nam Hải - 2A202601037
3. Thành viên 3: Nguyễn Nam Anh - 2A202601703
4. Thành viên 4: Bùi Đặng Quốc An - 2A202601799
5. Thành viên 5: Nguyễn Minh Hoàng - 2A202601609
6. Thành viên 6: Nguyễn Hoàng Việt - 2A202601940

---

## 1. Quyết định chọn bài toán

Cả nhóm thống nhất chọn bài toán: "Hỗ trợ điều phối viên Xanh SM xử lý sự cố sạc pin thực địa" (Card #1).

Lý do lựa chọn:
- Ảnh hưởng trực tiếp tới vận hành thời gian thực (Real-time operation) của Xanh SM.
- Giúp giảm tình trạng xe dừng đón khách vì hết pin, nâng cao trải nghiệm của tài xế và khách hàng.
- Có các chỉ số đo lường (Metrics) rõ ràng và khả năng kiểm soát rủi ro an toàn cao nhờ mô hình Human-in-the-loop.

---

## 2. Problem Statement (6-field)

1. Actor / Operator:
   Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM.

2. Current Workflow:
   Khi tài xế báo hết pin giữa đường, điều phối viên tra cứu vị trí GPS xe trên bản đồ nội bộ, truy cập Dashboard trạm sạc VinFast để tìm trụ sạc trống phù hợp loại xe (VF5, VF8, v.v.), gõ tin nhắn chỉ dẫn gửi qua App tài xế và gọi xe cứu hộ pin nếu dung lượng pin dưới 5%.

3. Bottleneck:
   Bước tra cứu thủ công trụ sạc trống phù hợp và soạn tin nhắn chỉ đường tiếng Việt thân thiện (mất khoảng 10 phút/lượt).

4. Business Impact:
   Mỗi ngày có khoảng 80 sự cố pin thực địa tại Hà Nội, gây lãng phí 20 giờ làm việc/ngày của team điều vận và giảm 15% hiệu suất hoạt động của tài xế.

5. Success Metric:
   - Giảm tổng thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút.
   - Tỷ lệ chỉ dẫn đúng trạm sạc còn trụ trống đạt từ 98% trở lên.

6. Operational Boundary:
   - AI được phép: Truy cập API lấy tọa độ GPS, kiểm tra trạng thái trụ sạc trống và tự động soạn thảo tin nhắn chỉ dẫn ở dạng nháp (DRAFT).
   - AI TUYỆT ĐỐI CẤM: Không tự động gửi tin nhắn cho tài xế khi chưa được điều phối viên duyệt; Không gợi ý trạm sạc xa quá 5km nếu dung lượng pin hiện tại dưới 5% (phải chuyển sang yêu cầu điều xe cứu hộ pin).

---

## 3. Future-State Flow & AI Fit

- AI Fit Matrix: LLM Feature (có con người duyệt - Human-in-the-loop).

Quy trình vận hành tương lai:

1. Tài xế gọi báo sự cố pin khẩn cấp.
2. Hệ thống tự động lấy vị trí GPS xe và truy vấn API danh sách trạm sạc VinFast trống gần nhất.
3. AI tự động soạn thảo bản nháp tin nhắn (DRAFT) hướng dẫn đường đi hoặc đưa ra cảnh báo điều xe cứu hộ pin.
4. Điều phối viên kiểm tra nội dung nháp, thực hiện phê duyệt (bấm gửi) hoặc chỉnh sửa nếu cần.
5. Phương án dự phòng (Fallback): Nếu AI gặp lỗi hệ thống hoặc không tạo được tin nhắn, điều phối viên sẽ tự gõ tay thủ công theo quy trình cũ.

---

## 4. Evaluate & Quyết định cuối cùng

Checklist độ sẵn sàng AI:
- [x] Có sẵn dữ liệu vị trí GPS xe và log trạng thái trạm sạc.
- [x] Rủi ro khi AI sai được kiểm soát chặt chẽ thông qua bước duyệt của điều phối viên (HITL).
- [x] Đội ngũ điều phối viên sẵn sàng chuyển sang quy trình duyệt tin nháp tự động.

Quyết định cuối cùng của nhóm: GO (Bắt đầu xây dựng bản mẫu Prototype).

Lý giải quyết định:
Bài toán có ranh giới rõ ràng, rủi ro vận hành thấp nhờ bước duyệt của con người. Chi phí gọi API LLM để tạo tin nhắn nháp rất nhỏ (khoảng 0.0001 USD/lượt với Gemini Flash) so với lợi ích tiết kiệm được 12 phút xử lý cho mỗi sự cố xe, giúp nâng cao đáng kể hiệu suất vận hành cho Xanh SM.