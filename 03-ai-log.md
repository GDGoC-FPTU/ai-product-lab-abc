## 1. AI đã hỗ trợ được những gì?

Trong buổi làm bài lab, tôi đã sử dụng AI (Gemini / ChatGPT) làm trợ lý đồng hành (Thought-partner) cho các công việc sau:

- Brainstorm bài toán: Gợi ý các nút thắt cổ chai thực tế trong quy trình vận hành của các công ty thành viên Vingroup như Xanh SM, Vinhomes, VinFast, Vinpearl và Vinmec.
- Phản biện thẻ bài toán: Đóng vai trò là Trưởng phòng Vận hành khắt khe để stress-test các thẻ Quick Cards, giúp phát hiện ra các điểm thiếu thực tế trong Success Metric và các bước thủ công.
- Tối ưu hóa lập trình Prompt: Hỗ trợ viết cấu trúc Python cho hàm evaluate_prompt, thiết lập GenerateContentConfig với temperature bằng 0 và định hình output định dạng JSON.
- Xây dựng Test Cases: Gợi ý các câu lệnh tấn công (Adversarial Prompts) để kiểm tra độ vững chắc của ranh giới an toàn (Operational Boundary).

---

## 2. AI đã đưa ra thông tin sai hoặc lệch lạc nào?

Trong quá trình tương tác, AI đã mắc phải một số điểm chưa chuẩn xác:

- Bẫy logic khi test ranh giới pin: Khi tôi truyền vào prompt tấn công với nội dung xe VF8 đang cạn pin ở mức 2% nhưng tài xế cố tình yêu cầu tìm trạm sạc cách đó 8km, mô hình ban đầu vẫn trả về kết quả gợi ý trạm sạc thay vì chặn lại.
- Nguyên nhân: System Prompt ban đầu chỉ ghi chung chung là "không gợi ý trạm sạc quá xa khi pin thấp" chứ chưa quy định con số cụ thể (ngưỡng 5%) và chưa yêu cầu bắt buộc phải chuyển sang hành động gọi xe cứu hộ di động.
- Đề xuất giải pháp quá phức tạp: AI ban đầu gợi ý xây dựng hệ thống Multi-Agent tự động cho bài toán điều phối, trong khi thực tế chỉ cần mô hình LLM Feature đơn giản kết hợp với quy trình con người phê duyệt (Human-in-the-loop).

---

## 3. Tôi đã điều chỉnh và khắc phục như thế nào?

Để ép AI tuân thủ đúng ranh giới an toàn và cho ra kết quả chính xác, tôi đã thực hiện các điều chỉnh sau:

- Bổ sung quy tắc cứng vào System Prompt: Thiết lập rõ quy định "Nếu dung lượng pin dưới 5%, TUYỆT ĐỐI KHÔNG đề xuất trạm sạc, BẮT BUỘC trả về JSON với hành động dispatch_mobile_charger".
- Ép tham số kĩ thuật: Đặt temperature = 0.0 trong cấu hình gọi API để mô hình đưa ra câu trả lời nhất quán, mang tính logic cao và loại bỏ sự ngẫu nhiên.
- Siết chặt cấu hình Output: Ép mô hình trả về dữ liệu chuẩn JSON có cấu trúc rõ ràng thay vì văn bản tự do để code Python có thể dễ dàng bắt lỗi và xử lý Fallback.