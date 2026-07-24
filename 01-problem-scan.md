# 01-problem-scan.md

## Phase 1 — SCAN

Dưới đây là 5 bài toán thực tế thuộc các công ty thành viên Vingroup mà nhóm tôi đã quét qua bằng 4 lenses.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Lặp lại | Điều phối viên phải xử lý thủ công các yêu cầu đổi điểm đón khách và phân bổ lại cuốc xe khi khách hủy giữa chừng. |
| 2 | Xanh SM | Tốn thời gian | Tài xế báo sự cố pin/het pin giữa đường, điều phối viên mất nhiều thời gian tra cứu trạm sạc và soạn tin nhắn chỉ dẫn. |
| 3 | VinFast | AI-upgrade | Hệ thống hiện tại chưa tự động gợi ý trạm sạc phù hợp và chưa có trợ lý ngôn ngữ tự nhiên cho khách hàng. |
| 4 | Vinhomes | Pain từ người khác | Cư dân gửi phản ánh qua App, bộ phận quản lý phải đọc thủ công và phân loại từng phản ánh. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ mất nhiều thời gian soạn tóm tắt hồ sơ xuất viện từ hồ sơ bệnh án và ghi chú lâm sàng. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card #1 — Xanh SM: Sự cố sạc pin thực địa

- Bài toán: Tài xế Xanh SM báo hết pin giữa đường cần được hướng dẫn nhanh đến trạm sạc gần nhất.
- Công ty thành viên: Xanh SM
- Actor: Tài xế và điều phối viên trung tâm
- Workflow thủ công hiện tại: Tài xế gọi tổng đài → điều phối viên tra cứu vị trí → tra cứu trạm sạc → soạn tin hướng dẫn → gửi cho tài xế.
- Bước tốn thời gian/lỗi nhất: Tra cứu trạm sạc và soạn tin nhắn, khoảng 10–15 phút/lượt.
- AI có thể hỗ trợ: Tự động tra cứu và soạn draft tin nhắn chỉ dẫn.
- Metric: Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút.
- Quick Architecture: LLM

### Quick Problem Card #2 — Vinhomes: Phân loại phản ánh cư dân

- Bài toán: Các phản ánh cư dân được gửi qua App nhưng chưa được phân loại tự động.
- Công ty thành viên: Vinhomes
- Actor: Nhân viên quản lý tòa nhà
- Workflow thủ công hiện tại: Nhận phản ánh → đọc nội dung → phân loại → chuyển cho bộ phận đúng.
- Bước tốn thời gian/lỗi nhất: Đọc và phân loại thủ công, khoảng 8–10 phút/lượt.
- AI có thể hỗ trợ: Phân loại phản ánh và đề xuất bộ phận xử lý.
- Metric: Giảm thời gian phân loại từ 10 phút xuống dưới 2 phút.
- Quick Architecture: Rule + LLM

### Quick Problem Card #3 — Vinmec: Tóm tắt hồ sơ xuất viện

- Bài toán: Bác sĩ mất thời gian soạn bản tóm tắt hồ sơ xuất viện cho bệnh nhân.
- Công ty thành viên: Vinmec
- Actor: Bác sĩ và nhân viên y tế
- Workflow thủ công hiện tại: Đọc hồ sơ → trích xuất thông tin quan trọng → viết tóm tắt → kiểm tra lại.
- Bước tốn thời gian/lỗi nhất: Viết tóm tắt thủ công, khoảng 20–30 phút/bệnh nhân.
- AI có thể hỗ trợ: Tạo bản tóm tắt đầu tiên để bác sĩ rà soát.
- Metric: Giảm thời gian soạn từ 25 phút xuống dưới 8 phút.
- Quick Architecture: LLM
