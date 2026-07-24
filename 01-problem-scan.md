

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinmec** | Tốn thời gian | Bác sĩ phải tổng hợp thủ công bệnh án, kết quả xét nghiệm và đơn thuốc để viết tóm tắt xuất viện, mất khoảng 20–30 phút/bệnh nhân. |
| 2 | **Vinmec** | AI-upgrade | Dự báo bệnh nhân có nguy cơ không đến khám để gửi nhắc lịch cá nhân hóa và tự động lấp slot trống từ danh sách chờ. |
| 3 | **Vinhomes** | Pain từ người khác | Phân loại, xác định mức độ khẩn cấp và chuyển tự động phản ánh của cư dân trên ứng dụng đến đúng bộ phận xử lý, thay cho việc CSKH đọc và route thủ công. |
| 4 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện với dữ liệu phiên sạc và đối soát chênh lệch từ các trạm sạc hoặc đối tác hằng tuần. |
| 5 | **VinFast** | Tốn thời gian | Kỹ thuật viên đọc thủ công mô tả lỗi, lịch sử sửa chữa và dữ liệu chẩn đoán xe để phân loại hồ sơ bảo hành và chuyển đến đúng nhóm phụ trách. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                      │
│                                                                            │
│ Bài toán (1 câu): Tạo bản nháp tóm tắt xuất viện từ bệnh án, kết quả       │
│ xét nghiệm và đơn thuốc để bác sĩ kiểm tra, chỉnh sửa và ký duyệt.          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________                  │
│                                                                            │
│ Ai đang đau (Actor)? Bác sĩ điều trị và điều dưỡng phụ trách hồ sơ.         │
│                                                                            │
│ Workflow thủ công hiện tại (3-5 bước):                                     │
│   1. Mở nhiều nguồn hồ sơ ──> 2. Đọc và chọn thông tin quan trọng ──>       │
│   3. Soạn tóm tắt ──> 4. Kiểm tra, bổ sung và ký duyệt                     │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Đọc, tổng hợp và soạn bản nháp             │
│ (⏱ 20–30 phút/bệnh nhân).                                                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: trích xuất dữ kiện và       │
│ tạo bản nháp có dẫn chiếu nguồn; bác sĩ bắt buộc duyệt trước khi lưu.       │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian soạn trung vị từ       │
│ 25 xuống ≤10 phút; ≥95% dữ kiện bắt buộc chính xác; 100% bản nháp được duyệt.│
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                      │
│                                                                            │
│ Bài toán (1 câu): Phân loại mức độ khẩn cấp và chuyển phản ánh dạng         │
│ văn bản tự do của cư dân đến đúng bộ phận xử lý.                            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________                  │
│                                                                            │
│ Ai đang đau (Actor)? Nhân viên CSKH, ban quản lý và cư dân.                 │
│                                                                            │
│ Workflow thủ công hiện tại (3-5 bước):                                     │
│   1. Nhận phản ánh ──> 2. Đọc nội dung/ảnh ──> 3. Chọn nhóm và mức ưu tiên  │
│   ──> 4. Chuyển bộ phận, sửa route nếu bị trả lại                           │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Hiểu nội dung và chọn đúng route           │
│ (⏱ 5–10 phút/ticket; có thể lâu hơn khi nội dung mơ hồ).                    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: đề xuất category, priority, │
│ bộ phận và lý do; ticket khẩn cấp/độ tin cậy thấp chuyển người duyệt.       │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)? ≥90% ticket route đúng ngay lần đầu;  │
│ ≥85% ticket được phân loại trong ≤30 giây; 100% ticket khẩn cấp có HITL.    │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                      │
│                                                                            │
│ Bài toán (1 câu): Phân loại sơ bộ hồ sơ bảo hành từ mô tả lỗi, lịch sử      │
│ sửa chữa và mã chẩn đoán để chuyển đến đúng nhóm kỹ thuật.                  │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes                 │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________                  │
│                                                                            │
│ Ai đang đau (Actor)? Cố vấn dịch vụ, kỹ thuật viên và nhóm bảo hành.        │
│                                                                            │
│ Workflow thủ công hiện tại (3-5 bước):                                     │
│   1. Nhận hồ sơ ──> 2. Đọc mô tả và lịch sử xe ──> 3. Đối chiếu mã lỗi     │
│   và chính sách ──> 4. Phân loại, chuyển nhóm hoặc yêu cầu bổ sung          │
│                                                                            │
│ Bước nào tốn thời gian/lỗi nhất? Tổng hợp mô tả tự do với lịch sử sửa chữa  │
│ để chọn nhóm lỗi (⏱ 15–25 phút/hồ sơ).                                     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2–3: tóm tắt bằng chứng, đề xuất │
│ nhóm lỗi và dữ liệu còn thiếu; con người quyết định duyệt/từ chối bảo hành. │
│                                                                            │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian phân loại xuống        │
│ ≤5 phút/hồ sơ; ≥90% route đúng lần đầu; 0 hồ sơ được AI tự duyệt/từ chối.  │
│                                                                            │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent                │
└────────────────────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---
