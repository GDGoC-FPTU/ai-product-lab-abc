# 01 — Problem Scan (Cá nhân) — Vin Smart Future

---

# 🔍 Phase 1 — SCAN

Dùng **4 Lenses** quét qua hoạt động vận hành của các công ty thành viên Vingroup. Danh sách tối thiểu 5 bài toán thực tế:

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | VinFast | Lặp lại | Kỹ thuật viên nhập tay dữ liệu chẩn đoán lỗi xe (mã DTC) vào hệ thống bảo hành để đối chiếu điều khoản |
| 2 | VinFast | Tốn thời gian | CS đọc và phân loại thủ công ticket khiếu nại pin/phần mềm từ app, hotline, mạng xã hội để route đúng phòng ban |
| 3 | VinFast | AI-upgrade | Trợ lý ảo trong xe phản hồi rập khuôn theo kịch bản cố định, không hiểu câu hỏi tự nhiên về pin/tính năng ADAS |
| 4 | VinFast | Stakeholder Pain (nhân viên) | Nhân viên đại lý tự tổng hợp báo cáo tồn kho phụ tùng theo tuần bằng Excel, đối chiếu thủ công giữa các kho vùng |
| 5 | VinFast | Stakeholder Pain (khách hàng) | Khách hàng phàn nàn dự đoán quãng đường/thời gian sạc còn lại không chính xác so với thực tế vận hành |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Top 3 bài toán được chọn từ danh sách SCAN ở trên để đánh giá nhanh: **#1 (Nhập tay mã DTC), #2 (Phân loại ticket khiếu nại), #3 (Trợ lý ảo trong xe)**.

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Kỹ thuật viên nhập tay mã lỗi DTC vào hệ  │
│ thống bảo hành để đối chiếu điều khoản.                     │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Kỹ thuật viên đại lý (Service Advisor) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc mã DTC từ máy chẩn đoán ──> 2. Tra bảng điều khoản │
│   bảo hành ──> 3. Gõ tay mã lỗi + điều khoản vào hệ thống   │
│   ──> 4. Đối chiếu, xác nhận với quản lý trước khi duyệt    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 8 phút/lượt,     │
│ hay gõ nhầm mã DTC dẫn đến từ chối bảo hành sai)             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tự động tra │
│ cứu điều khoản khớp mã DTC và điền sẵn form)                │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian nhập   │
│ liệu từ 8 phút ──> dưới 1 phút/lượt; tỉ lệ gõ sai mã giảm   │
│ từ ~5% xuống dưới 0.5%.                                     │
│                                                             │
│ Quick Architecture: [x] Rule  [ ] No AI  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): CS đọc và phân loại thủ công ticket khiếu │
│ nại pin/phần mềm từ app, hotline, mạng xã hội để route đúng │
│ phòng ban.                                                  │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH (Customer Support)      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận ticket từ 3 kênh (app/hotline/MXH) ──> 2. Đọc nội │
│   dung, xác định chủ đề (pin/phần mềm/khác) ──> 3. Tra bảng │
│   phân công theo phòng ban ──> 4. Gắn nhãn, chuyển ticket   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 6 phút/lượt,     │
│ dễ hiểu sai ý khách, route nhầm phòng ban)                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (phân loại   │
│ chủ đề + gợi ý phòng ban nhận ticket)                        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? 85% ticket được phân  │
│ loại đúng phòng ban dưới 10 giây; giảm thời gian xử lý từ   │
│ 6 phút ──> dưới 1 phút/lượt.                                │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý ảo trong xe phản hồi rập khuôn theo│
│ kịch bản cố định, không hiểu câu hỏi tự nhiên về pin/ADAS.  │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Khách hàng lái xe VinFast              │
│                                                             │
│ Workflow thủ công hiện tại (3 bước):                        │
│   1. Khách hỏi câu tự do ──> 2. Hệ thống match từ khoá cố   │
│   định trong kịch bản ──> 3. Trả lời sai/không nhận diện,   │
│   khách phải gọi hotline                                    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ không xác định   │
│ được ý định câu hỏi, tỉ lệ "không hiểu" cao)                │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (hiểu ngôn ngữ │
│ tự nhiên, trả lời dựa trên tài liệu kỹ thuật xe)             │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm tỉ lệ "không     │
│ hiểu câu hỏi" từ ~30% xuống dưới 5%; giảm số cuộc gọi        │
│ hotline liên quan đến câu hỏi cơ bản 20%.                    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
