# 03 — AI Log & Reflection (Cá nhân) — Vin Smart Future

> Nhật ký phản ánh trung thực quá trình dùng AI (Claude) làm thought-partner trong Phase 1 & 2 của bài Lab.

---

## 1. AI giúp gì?

Tôi dùng Claude như một thought-partner ở hai việc chính:

* **Brainstorm & cấu trúc hoá 3 Quick Problem Cards:** Từ 5 bài toán đã liệt kê ở Phase 1 (SCAN), tôi nhờ AI giúp diễn giải mỗi bài toán thành đúng khuôn mẫu thẻ (Actor, Workflow 3-5 bước, Bottleneck, Metric, Architecture) để tiết kiệm thời gian trình bày, thay vì phải tự canh format ASCII từng ký tự.
* **Stress-test thẻ bài toán bằng prompt đóng vai CFO/Trưởng phòng Vận hành:** Đúng theo gợi ý trong worksheet, tôi dán một thẻ bài toán mẫu vào AI và yêu cầu nó đóng vai một CFO khắt khe để phản biện. AI chỉ ra 3 điểm yếu logic: (1) card cho phép chọn kiến trúc AI *trước khi* chẩn đoán nguyên nhân gốc của bottleneck, (2) metric không có baseline tần suất/khối lượng nên không tính được ROI, (3) 4 lựa chọn Quick Architecture được đặt ngang hàng thay vì theo bậc thang buộc phải chứng minh rule-based không đủ trước khi leo thang lên LLM/Agent. Phản biện này thực sự hữu ích — nó ép tôi phải nghĩ về chi phí vận hành và rủi ro compliance (đặc biệt liên quan dữ liệu bảo hành ở Card #1), chứ không chỉ nghĩ AI "nghe hay".

## 2. AI sai gì?

Khi giúp tôi soạn 3 Quick Problem Cards, AI đã **tự đặt ra các con số metric cụ thể** (ví dụ: "giảm thời gian nhập liệu từ 8 phút xuống dưới 1 phút", "tỉ lệ gõ sai mã giảm từ ~5% xuống dưới 0.5%", "85% ticket được phân loại đúng phòng ban dưới 10 giây", "giảm tỉ lệ không hiểu câu hỏi từ ~30% xuống dưới 5%") mà **không có bất kỳ dữ liệu thực tế nào của VinFast làm căn cứ**. Đây chính là dạng hallucination nguy hiểm nhất: không phải AI bịa một sự kiện sai rõ ràng, mà nó tạo ra những con số *nghe rất hợp lý và đúng định dạng chuẩn* (kiểu "85% dưới 10 giây" giống hệt ví dụ mẫu trong worksheet), khiến người đọc dễ nhầm tưởng đó là số liệu đã khảo sát thật. Nếu tôi copy thẳng các card này vào báo cáo trình Ban Giám Đốc mà không tự nhận thức được điều này, đó sẽ là một quyết định đầu tư dựa trên số liệu tưởng tượng.

## 3. Sửa đổi ra sao?

Tôi đã yêu cầu bổ sung rõ ràng: mọi con số target/metric do AI đề xuất mà chưa có nguồn dữ liệu thực tế phải được gắn nhãn là **giả định cần xác thực** (không phải kết quả đo đạc), và chỉ được dùng làm **giả thuyết mục tiêu (hypothesis)** để nhóm đi khảo sát thực địa ở Phase 3 (Deep-Dive) — không được coi là số liệu final để quyết định GO/NO-GO. Tôi đã cập nhật lại `01-problem-scan.md` để đánh dấu rõ ràng ghi chú này ngay dưới mỗi card, thay vì để các con số trông như dữ liệu đã kiểm chứng. Bài học rút ra: khi dùng AI làm thought-partner để soạn số liệu, luôn phải hỏi ngược "con số này AI lấy từ đâu?" trước khi đưa vào bất kỳ tài liệu ra quyết định nào.
