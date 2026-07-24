# Phase 1: SCAN - Tìm kiếm cơ hội tối ưu bằng AI

Dưới đây là danh sách các bài toán (vấn đề) trong hệ sinh thái Vingroup mà nhóm tìm thấy:

| # | Công ty | Loại vấn đề (Lens) | Mô tả bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Lặp lại | So khớp và phân bổ lại cuốc xe khi khách hàng yêu cầu thay đổi điểm đến giữa chừng. |
| 2 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố sạc pin hoặc va chạm thực địa (mất 15-20 phút/lượt). |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện và đối chiếu số liệu trạm sạc đối tác hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Hệ thống phân loại và điều hướng tự động các phản hồi/khiếu nại của cư dân trên App Vinhomes Resident. |
| 5 | **Vinmec** | Pain từ người khác | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện cho bệnh nhân (20-30 phút/ca). |

---

# Phase 2: QUICK-ASSESS - 3 Thẻ Bài Toán Tiềm Năng

### Thẻ Bài Toán 1 (Bài toán được nhóm chọn)
- **Bài toán:** Tài xế Xanh SM báo cáo sự cố sạc pin / hết pin giữa đường cần điều phối cứu hộ hoặc trạm sạc gần nhất.
- **Công ty thành viên:** Xanh SM (GSM)
- **Ai đang gặp khó khăn?** Tài xế (phải chờ đợi), Điều phối viên (quá tải công việc vào giờ cao điểm).
- **Quy trình thủ công hiện tại:**
  1. Tài xế gọi báo hết pin -> 2. Tra cứu định vị GPS -> 3. Tìm trạm sạc trống -> 4. Soạn tin nhắn hướng dẫn -> 5. Gọi cứu hộ (nếu pin < 5%).
- **Bước gây tắc nghẽn (Bottleneck):** Bước 3 & 4: Tra cứu trạm sạc phù hợp và tự tay soạn tin nhắn (tốn 10-12 phút).
- **Đo lường thành công:** Giảm thời gian xử lý sự cố từ 15 phút xuống dưới 3 phút/lượt.
- **Giải pháp AI:** LLM Feature (Tự động tra cứu và soạn tin nhắn chỉ dẫn/cứu hộ).

### Thẻ Bài Toán 2
- **Bài toán:** Phân loại và điều hướng khiếu nại của cư dân trên App Vinhomes Resident đang quá chậm trễ.
- **Công ty thành viên:** Vinhomes
- **Ai đang gặp khó khăn?** Nhân viên CSKH (phải đọc và chuyển tiếp thủ công), Cư dân (thời gian chờ phản hồi lâu).
- **Quy trình thủ công hiện tại:**
  1. Cư dân gửi khiếu nại -> 2. CSKH đọc -> 3. Phân loại theo ban ngành (điện, nước, vệ sinh) -> 4. Chuyển tiếp cho kỹ thuật.
- **Bước gây tắc nghẽn (Bottleneck):** Đọc và phân loại thủ công.
- **Đo lường thành công:** Giảm thời gian chuyển tiếp khiếu nại từ 12 tiếng xuống 15 phút.
- **Giải pháp AI:** LLM Classification & Rule-based Router (Tự động gắn tag chuyên mục).

### Thẻ Bài Toán 3
- **Bài toán:** Bác sĩ tốn rất nhiều thời gian để viết Tóm tắt hồ sơ xuất viện (Discharge Summary).
- **Công ty thành viên:** Vinmec
- **Ai đang gặp khó khăn?** Bác sĩ chuyên khoa (bị quá tải công việc giấy tờ, hành chính).
- **Quy trình thủ công hiện tại:**
  1. Tổng hợp bệnh án điện tử -> 2. Xem kết quả xét nghiệm/chuẩn đoán -> 3. Viết tay tóm tắt xuất viện bằng ngôn ngữ dễ hiểu.
- **Bước gây tắc nghẽn (Bottleneck):** Tổng hợp dữ liệu phân tán và soạn thảo văn bản (tốn 20-30 phút/ca).
- **Đo lường thành công:** Giảm thời gian soạn hồ sơ xuống dưới 5 phút, độ chính xác y khoa đạt 100%.
- **Giải pháp AI:** LLM Feature (Agent hỗ trợ trích xuất thông tin y tế thành văn bản tóm tắt).
