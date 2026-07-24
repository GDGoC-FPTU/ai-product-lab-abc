# DEEP-DIVE REPORT — VINMEC
Tên Nhóm: Nhóm ABC
Số lượng: 06 Thành viên

Thành viên 1: Nguyễn Trọng Đức - 2A202601673
Thành viên 2: Nguyễn Đào Nam Hải - 2A202601037
Thành viên 3: Nguyễn Nam Anh - 2A202601703
Thành viên 4: Bùi Đặng Quốc An - 2A202601799
Thành viên 5: Nguyễn Minh Hoàng - 2A202601609
Thành viên 6: Nguyễn Hoàng Việt - 2A202601940
> **Lưu ý:** Các số liệu trong báo cáo là giả định để thiết kế pilot, không phải dữ liệu nội bộ đã được Vinmec xác nhận. Nhóm cần đo baseline thực tế trước khi triển khai.

---

# 1. Quyết định lựa chọn

Nhóm chọn bài toán:

> **Trợ lý AI tạo bản nháp tóm tắt hồ sơ xuất viện tại Vinmec.**

AI đọc bệnh án, diễn biến điều trị, kết quả cận lâm sàng và đơn thuốc để tạo bản nháp tóm tắt. Bác sĩ phải kiểm tra, chỉnh sửa và ký duyệt trước khi hồ sơ được lưu hoặc gửi cho bệnh nhân.

**Lý do lựa chọn:**

- Bác sĩ đang phải đọc và tổng hợp thủ công nhiều nguồn thông tin.
- Quy trình lặp lại, ước tính mất 22–34 phút/hồ sơ.
- Phần tổng hợp ghi chú phi cấu trúc phù hợp với LLM.
- Kết quả có thể đo bằng thời gian xử lý và độ chính xác.
- Rủi ro được giới hạn bằng cơ chế draft-only và Human-in-the-loop.

---

# 2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | **Actor chính:** bác sĩ điều trị nội trú. **Actor liên quan:** điều dưỡng kiểm tra hồ sơ, bác sĩ có thẩm quyền ký duyệt và phòng quản lý chất lượng. |
| **2. Current Workflow** | Bác sĩ thực hiện 5 bước: **(1)** mở và rà soát bệnh án, **(2)** chọn chẩn đoán, thuốc, thủ thuật và kết quả quan trọng, **(3)** viết tóm tắt diễn biến điều trị, **(4)** kiểm tra và bổ sung trường còn thiếu, **(5)** ký duyệt. Tổng thời gian giả định là **22–34 phút/hồ sơ**, baseline dùng để tính toán là **25 phút/hồ sơ**. |
| **3. Bottleneck** | Bước chọn dữ kiện và viết tóm tắt mất khoảng **13–19 phút/hồ sơ**. Thông tin nằm rải rác trong nhiều ghi chú, có nội dung lặp hoặc mâu thuẫn. Rule-based code kiểm tra được trường trống nhưng khó tổng hợp văn bản y khoa phi cấu trúc thành một bản tóm tắt mạch lạc. |
| **4. Business Impact** | Kịch bản giả định **2.000 hồ sơ/tháng × 25 phút = 833 giờ bác sĩ/tháng**. Nếu giảm xuống 10 phút/hồ sơ, hệ thống có thể hoàn trả khoảng **500 giờ/tháng**. Với chi phí cơ hội nhân sự giả định **300.000–600.000 đồng/giờ**, giá trị năng lực tương đương **150–300 triệu đồng/tháng**. Đây là năng lực được giải phóng, không mặc định là tiền mặt tiết kiệm. |
| **5. Success Metric** | **(1)** Giảm thời gian hoàn thiện trung vị từ 25 xuống **≤10 phút/hồ sơ**; **(2)** ≥95% dữ kiện bắt buộc khớp nguồn; **(3)** 0 lỗi nghiêm trọng về thuốc, dị ứng, chẩn đoán hoặc thủ thuật trên tập kiểm thử khóa; **(4)** ≥80% bản nháp chỉ cần chỉnh sửa nhẹ; **(5)** 100% đầu ra được bác sĩ duyệt trước khi lưu. |
| **6. Operational Boundary** | AI chỉ được đọc dữ liệu thuộc đúng encounter, trích xuất dữ kiện và tạo **bản nháp có dẫn chiếu nguồn**. AI **không được** tự chẩn đoán, thêm thông tin không có trong hồ sơ, thay đổi thuốc, ký duyệt, lưu bản chính thức hoặc gửi cho bệnh nhân. Hồ sơ thiếu dữ liệu, mâu thuẫn hoặc có độ tin cậy thấp phải chuyển sang xử lý thủ công. |

## Công thức đo tác động

```text
Giờ được hoàn trả/tháng
= Số hồ sơ × (Thời gian baseline − Thời gian sau pilot) / 60

= 2.000 × (25 − 10) / 60
= 500 giờ/tháng
```

---

# 3. Future-State Flow & AI Fit

## 3.1. Phân loại AI Fit

- [ ] **Rule / State-Machine thuần túy**
- [x] **LLM Feature kết hợp Rule-based Validation**
- [ ] **Agentic Loop**

**Giải thích:**

- **Rule-based** xử lý quyền truy cập, kiểm tra encounter, trường bắt buộc, mã thuốc và định dạng.
- **LLM** đọc ghi chú phi cấu trúc, chọn lọc dữ kiện và tạo bản tóm tắt.
- **Con người** kiểm tra nội dung và đưa ra quyết định cuối cùng.
- Không dùng Agentic Loop vì AI không được tự lập kế hoạch, ký hoặc phát hành hồ sơ.

## 3.2. Future-State Flow

```text
[1. Bác sĩ chọn hồ sơ cần xuất viện]
                    |
                    v
[2. RULE: Kiểm tra quyền truy cập,
    đúng encounter và trường bắt buộc]
        | PASS                         | FAIL
        v                              v
[3. RULE: Chuẩn hóa dữ liệu]       [↩ FALLBACK:
    - chẩn đoán                       Xử lý thủ công]
    - thuốc và dị ứng
    - xét nghiệm, thủ thuật
        |
        v
[4. 🔵 LLM: Tạo bản nháp tóm tắt
    kèm dẫn chiếu tới nguồn]
        |
        v
[5. RULE: Kiểm tra đầu ra
    - đủ trường
    - dữ kiện khớp nguồn
    - đạt ngưỡng tin cậy]
        | PASS                         | FAIL
        v                              v
[6. 🟢 BÁC SĨ REVIEW]              [↩ FALLBACK:
    - đối chiếu nguồn                 Gắn cờ lỗi và
    - chỉnh sửa                       soạn thủ công]
    - xác nhận nội dung
        |
        v
[7. 🟢 BÁC SĨ KÝ DUYỆT]
        |
        v
[8. HIS/EMR lưu bản chính thức
    và audit log]
```

## 3.3. Human-in-the-loop

Bác sĩ bắt buộc phải:

1. Đối chiếu bản nháp với dữ liệu nguồn.
2. Kiểm tra chẩn đoán, thuốc, dị ứng, thủ thuật và hướng dẫn theo dõi.
3. Sửa hoặc từ chối bản nháp nếu có sai lệch.
4. Chủ động ký duyệt trước khi hồ sơ được lưu chính thức.

AI không được cấp quyền ký, phát hành hồ sơ hoặc tự gửi nội dung cho bệnh nhân.

## 3.4. Fallback

Hệ thống quay về quy trình thủ công khi:

- HIS/EMR hoặc LLM không hoạt động.
- Hồ sơ thiếu trường bắt buộc.
- Các nguồn dữ liệu mâu thuẫn.
- AI không dẫn chiếu được nguồn cho dữ kiện lâm sàng.
- Điểm tin cậy thấp hơn ngưỡng được phê duyệt.
- Hồ sơ thuộc nhóm ca phức tạp hoặc ngoài phạm vi pilot.

Fallback phải hiển thị rõ lý do và không làm gián đoạn quá trình xuất viện.

---

# 4. Evaluate

## 4.1. AI Readiness Checklist

| Tiêu chí | Trạng thái | Việc cần thực hiện |
|---|---|---|
| Có dữ liệu mẫu/log sạch để test? | [ ] **Chưa xác nhận** | Chuẩn bị 500–1.000 hồ sơ đã khử định danh và tập kiểm thử khóa 200–300 hồ sơ. |
| Có baseline định lượng? | [ ] **Chưa có** | Đo thời gian xử lý và tỷ lệ sửa lỗi trong 2–4 tuần. |
| Rủi ro khi AI sai có thể kiểm soát? | [x] **Có điều kiện** | Áp dụng draft-only, dẫn chiếu nguồn, rule validation, HITL và fallback thủ công. |
| Stakeholder sẵn sàng tham gia? | [ ] **Chưa xác nhận** | Phỏng vấn bác sĩ, điều dưỡng, IT/HIS, quản lý chất lượng và pháp chế. |
| Có tiêu chuẩn nghiệm thu lâm sàng? | [ ] **Chưa hoàn tất** | Bác sĩ xây rubric lỗi nghiêm trọng, ngưỡng confidence và danh sách ca loại trừ. |
| Có cơ chế bảo mật và audit? | [x] **Có thiết kế sơ bộ** | Hoàn thành RBAC, mã hóa, audit log và security review trước pilot. |

## 4.2. Ước lượng chi phí pilot

### Chi phí một lần

| Hạng mục | Chi phí ước tính |
|---|---:|
| Khảo sát workflow và đo baseline | 30–50 triệu đồng |
| Khử định danh, làm sạch dữ liệu và tạo tập đánh giá | 50–90 triệu đồng |
| Tích hợp sandbox HIS/EMR và giao diện review | 100–160 triệu đồng |
| Phát triển prompt, grounding và rule validation | 50–80 triệu đồng |
| Security review, phân quyền và audit log | 30–60 triệu đồng |
| Đánh giá lâm sàng, đào tạo và hỗ trợ pilot | 30–60 triệu đồng |
| **Tổng chi phí một lần** | **290–500 triệu đồng** |

### Chi phí vận hành

| Hạng mục | Chi phí/tháng |
|---|---:|
| Model inference | 5–20 triệu đồng |
| Hạ tầng, monitoring và lưu audit log | 10–25 triệu đồng |
| QA lâm sàng và hỗ trợ vận hành | 20–45 triệu đồng |
| **Tổng chi phí vận hành** | **35–90 triệu đồng/tháng** |

### Tổng ngân sách pilot 3 tháng

```text
Chi phí một lần + 3 × Chi phí vận hành tháng
= 290–500 triệu + 3 × (35–90 triệu)
= 395–770 triệu đồng
```

Đây là **ROM estimate**. Chi phí thực tế phụ thuộc vào số hồ sơ, độ dài hồ sơ, model sử dụng, phương án triển khai cloud/on-premise và mức độ tích hợp HIS/EMR.

## 4.3. Quyết định cuối cùng

- [x] **GO — Có điều kiện:** bắt đầu prototype offline với phạm vi hẹp.
- [ ] **NOT YET:** chưa triển khai.
- [ ] **NO-GO:** hủy dự án hoặc chỉ dùng rule-based.

### Luận điểm kỹ thuật

- LLM phù hợp với việc tổng hợp ghi chú y khoa phi cấu trúc; rule-based phù hợp với validation và các ranh giới cứng.
- Draft-only, source grounding, HITL và fallback giúp giới hạn hậu quả khi AI sai.
- Có thể kiểm thử offline trước khi đưa hệ thống vào workflow thật.
- Không sử dụng Agentic Loop nên AI không có quyền tự thực hiện hành động lâm sàng.

### Luận điểm vận hành và tài chính

- Theo kịch bản giả định, giải pháp có thể hoàn trả khoảng **500 giờ bác sĩ/tháng**, tương đương **150–300 triệu đồng giá trị năng lực/tháng**.
- Ngân sách pilot 3 tháng dự kiến **395–770 triệu đồng**.
- Chỉ có thể tính payback chính thức sau khi xác minh baseline và chứng minh thời gian tiết kiệm tạo ra năng lực khám chữa bệnh, giảm làm thêm hoặc cải thiện SLA.

### Điều kiện để chuyển sang production

1. Không có lỗi nghiêm trọng trên tập kiểm thử khóa và giai đoạn shadow mode.
2. ≥95% dữ kiện bắt buộc khớp nguồn.
3. Thời gian hoàn thiện trung vị ≤10 phút/hồ sơ.
4. ≥80% bản nháp chỉ cần chỉnh sửa nhẹ.
5. Security, pháp chế, quản lý chất lượng và hội đồng chuyên môn phê duyệt.
6. Có cơ chế dừng hệ thống và quay lại workflow thủ công ngay lập tức.

Nếu không đạt các điều kiện trên, quyết định chuyển thành **NOT YET** để bổ sung dữ liệu và điều chỉnh hệ thống.
