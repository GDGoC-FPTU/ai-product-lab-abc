# 03-ai-log.md

## AI giúp gì

Trong buổi lab, tôi dùng AI như một người đồng hành tư duy để brainstorm các bài toán vận hành phù hợp cho Vin Smart Future, viết prompt prototype cho quy trình xử lý sự cố sạc pin và kiểm tra các ranh giới an toàn của hệ thống.

## AI sai gì

Một điểm AI có thể đưa ra câu trả lời sai là đề xuất trạm sạc ở khoảng cách quá xa khi pin đang ở mức thấp. Đây là lỗi nguy hiểm vì có thể khiến tài xế không kịp về đến trạm và rơi vào tình huống nguy hiểm.

## Sửa đổi ra sao

Tôi đã bổ sung ràng buộc rõ ràng trong prompt: bắt buộc thêm tag [DRAFT_ONLY], và khi pin dưới 5% thì phải chuyển sang đề xuất xe cứu hộ pin di động thay vì đưa ra đường đi đến trạm xa. Việc này giúp hệ thống có phản ứng an toàn hơn trước các lời yêu cầu bypass.
