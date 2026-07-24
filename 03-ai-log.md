# Nhật ký Tương Tác với AI (AI Log & Reflection)

Trong quá trình thực hiện bài Lab 02, việc sử dụng AI (như Gemini, ChatGPT) đóng vai trò làm người đồng hành (Thought-partner) đã mang lại cho nhóm rất nhiều trải nghiệm thú vị.

**1. AI đã giúp gì cho nhóm?**
- AI hỗ trợ nhóm suy nghĩ (brainstorm) cực kỳ nhanh các vấn đề/bài toán tiềm năng trong hệ sinh thái Vingroup, giúp nhóm có cái nhìn tổng quan ở Phase 1.
- AI đóng vai trò như một kỹ sư giàu kinh nghiệm, giúp phản biện và chỉ ra những điểm bất hợp lý trong quy trình xử lý sự cố hiện tại của Xanh SM.
- Đặc biệt trong Phase 4, AI đã giúp viết code Python (`prompt_prototype.py`) sử dụng thư viện `google-genai` SDK cực kỳ chuẩn xác. AI còn hỗ trợ viết một System Prompt tiếng Anh rất chặt chẽ để xử lý triệt để các ranh giới an toàn (Operational Boundaries).

**2. AI đã sai / nhầm lẫn điều gì?**
- Lúc đầu, khi sử dụng các prompt chung chung hoặc tiếng Việt, đôi khi AI tỏ ra quá "sáng tạo" và có xu hướng bỏ qua thẻ `[DRAFT_ONLY]` nếu người dùng (tài xế) cố tình ép buộc hoặc dọa nạt (Adversarial attack).
- Ở một số lần test, AI trả về nội dung hướng dẫn hơi rườm rà, thêm thắt thông tin thừa vào chuỗi JSON gây khó khăn cho việc phân tích dữ liệu tự động của hệ thống.

**3. Nhóm đã điều chỉnh như thế nào để khắc phục?**
- Để khắc phục sự "linh hoạt quá mức" của LLM, nhóm đã chuyển sang sử dụng System Prompt bằng tiếng Anh với cú pháp rõ ràng, chia làm các khối `[RULE 1]`, `[RULE 2]` và nhấn mạnh mạnh mẽ các từ khóa cấm kị như `STRICTLY`, `MUST NEVER`.
- Thêm cấu hình `temperature=0.0` trong code Python để ép LLM hoạt động ở chế độ logic tuyệt đối (Deterministic). 
- Kết quả: Khi áp dụng các biện pháp bảo vệ này, mô hình đã trở nên vô cùng nguyên tắc và vượt qua 100% các bài test ranh giới an toàn, không thể bị người dùng thao túng.
