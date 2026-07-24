# 02-deep-dive-report.md

## Quyết định lựa chọn

Nhóm chọn bài toán: Xử lý sự cố sạc pin thực địa cho tài xế Xanh SM.

## Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| Actor / Operator | Điều phối viên trung tâm Xanh SM và tài xế đang đi trên đường. |
| Current Workflow | Khi tài xế báo hết pin, điều phối viên phải tra cứu vị trí, tra cứu trạm sạc gần nhất, soạn tin nhắn chỉ dẫn và gửi lại cho tài xế. |
| Bottleneck | Bước tra cứu trạm sạc và soạn tin nhắn chỉ dẫn mất nhiều thời gian và dễ sai sót. |
| Business Impact | Mỗi ngày có nhiều sự cố pin thực địa, làm chậm việc đón khách và tăng rủi ro hiệu suất vận hành. |
| Success Metric | Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút; đạt tỷ lệ đúng địa điểm trên 95%. |
| Operational Boundary | AI được phép soạn draft, không được tự động gửi tin mà không có phê duyệt; không được đề xuất trạm sạc quá xa khi pin dưới 5%. |

## Future-State Flow & AI Fit

- AI Fit: LLM Feature
- Future-State Flow: Nhận sự cố → thu thập vị trí và trạng thái pin → AI đề xuất trạm gần nhất và draft tin nhắn → điều phối viên phê duyệt → gửi cho tài xế.
- Human-in-the-loop: Có bước điều phối viên duyệt trước khi gửi.
- Fallback: Nếu AI không tin cậy, điều phối viên tự soạn lại thủ công.

## Evaluate

- Checklist: Có dữ liệu mẫu và quy trình rõ ràng; rủi ro có thể kiểm soát bằng HITL; stakeholders có thể thay đổi quy trình.
- Final Decision: GO
- Justification: Đây là bài toán có phạm vi hẹp, metric rõ ràng và có thể triển khai bằng prompt prototype trước khi đầu tư lớn.
