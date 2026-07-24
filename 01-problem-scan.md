# 📄 Báo Cáo Cá Nhân: Scan & Quick Problem Cards

- **Họ và tên:** [Tên của bạn]
- **Mã số sinh viên (MSSV):** [MSSV của bạn]
- **Đơn vị:** Vin Smart Future (Vingroup)

---

## 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Vận Hành (5 Problems)

Áp dụng 4 Lenses (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain) để quét qua các công ty thành viên Vingroup:

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên xử lý thủ công sự cố xe cạn pin giữa đường, tìm trạm sạc VinFast còn trụ trống và nhắn tin chỉ đường cho tài xế (mất 12-15 phút/cuộc). |
| 2 | **Vinhomes** | Lặp lại | Phân loại và route tự động các phản ánh/khiếu nại của cư dân từ App Vinhomes Resident đến đúng Ban Quản Lý tòa nhà. |
| 3 | **Vinpearl** | AI-upgrade | Tổng hợp review từ Agoda/Google Maps, tự động phát hiện phàn nàn khẩn cấp về vệ sinh/thái độ dịch vụ gửi thẳng tới Hotel Manager. |
| 4 | **VinFast** | Pain từ người khác | Kỹ thuật viên mất nhiều thời gian tra cứu sơ đồ điện/mã lỗi OBD-II từ mô tả tiếng Việt cảm quan của khách hàng khi sửa chữa xe điện. |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút/bệnh nhân để trích xuất tóm tắt hồ sơ bệnh án điện tử làm bản tóm tắt xuất viện (Discharge Summary). |

---

## 🃏 Phase 2 — QUICK-ASSESS: Top 3 Quick Problem Cards

### 💳 QUICK PROBLEM CARD #1
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Hỗ trợ tài xế Xanh SM bị sự cố hết pin thực địa  │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ lâu) & Điều phối viên      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận cuộc gọi báo hết pin ──> 2. Định vị GPS xe         │
│   ──> 3. Tra thủ công trụ sạc trống ──> 4. Nhắn tin chỉ đường│
│   ──> 5. Điều xe cứu hộ nếu dưới 5% pin                     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 10 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Tự động tra cứu trụ sạc trống + Draft tin nhắn chỉ đường)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm tổng thời gian xử lý sự cố từ 15 min ──> under 3 min.  │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘



┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại & Route ticket phản ánh cư dân Vinhomes │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH BQL & Cư dân (chờ lâu)  │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh lên App ──> 2. CSKH đọc nội dung   │
│   ──> 3. Chọn phòng ban xử lý (Kỹ thuật/Vệ sinh/Bảo vệ)     │
│   ──> 4. Tạo ticket và chuyển tiếp                            │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 15 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Đọc văn bản, phân loại phòng ban & trích xuất độ khẩn cấp) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Phân loại và route tự động 85% ticket trong under 10 giây.  │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Trích xuất bản tóm tắt hồ sơ xuất viện Vinmec     │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính)   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tổng hợp diễn tiến điều trị ──> 2. Đọc kết quả xét nghiệm│
│   ──> 3. Tóm tắt chỉ định thuốc ──> 4. Gõ văn bản xuất viện │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ 20 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Trích xuất dữ liệu EHR và draft bản tóm tắt ngôn ngữ dễ hiểu)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Rút ngắn thời gian soạn hồ sơ từ 25 min ──> under 5 min.    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Có Human-in-the-loop)  │
└─────────────────────────────────────────────────────────────┘