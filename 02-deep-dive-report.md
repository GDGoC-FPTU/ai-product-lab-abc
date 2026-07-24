# 02 — Deep-Dive Report (Nhóm) — Vin Smart Future

**Tên nhóm:** Nhóm ABC
**Số lượng:** 06 thành viên

1. Nguyễn Trọng Đức — 2A202601673
2. Nguyễn Đào Nam Hải — 2A202601037
3. Nguyễn Nam Anh — 2A202601703
4. Bùi Đặng Quốc An — 2A202601799
5. Nguyễn Minh Hoàng — 2A202601609
6. Nguyễn Hoàng Việt — 2A202601940

---

# 🗳️ Quyết định lựa chọn của nhóm

Nhóm chọn **Card #2 — VinFast: CS phân loại ticket khiếu nại pin/phần mềm** từ 3 Quick Problem Cards (xem `01-problem-scan.md`) để thực hiện Deep-Dive.

**Lý do loại các card khác:**
* **Card #1 (Nhập tay mã DTC bảo hành):** Đây thực chất là bài toán tra bảng đối chiếu (lookup), có thể giải quyết bằng Rule-based validation đơn giản — không đủ độ phức tạp ngôn ngữ để biện minh cho một Deep-Dive về AI Fit.
* **Card #3 (Trợ lý ảo trong xe):** Rủi ro vận hành cao (chạy real-time trong xe, ảnh hưởng an toàn lái xe) và cần tích hợp phần cứng/firmware ngoài phạm vi 1 buổi lab — phù hợp làm dự án dài hạn hơn là scope nhanh.
* **Card #2** vừa có khối lượng đủ lớn để đo ROI (nhiều ticket/ngày), vừa là bài toán phân loại ngôn ngữ tự nhiên kinh điển cho LLM Feature với rủi ro kiểm soát được qua HITL.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình xử lý ticket khiếu nại hiện tại của nhân viên CSKH VinFast:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận ticket  │     │ Đọc nội dung,│     │ Tra bảng     │     │ Gắn nhãn,    │
│ từ 3 kênh    │ ──→ │ xác định chủ │ ──→ │ phân công    │ ──→ │ chuyển ticket│
│ (app/hotline/│     │ đề (pin/PM/  │     │ theo phòng   │     │ cho phòng ban│
│ MXH)         │     │ khác) 🔄     │     │ ban          │     │ 🔄           │
│ Ai: CS       │     │ Ai: CS       │     │ Ai: CS       │     │ Ai: CS       │
│ ⏱ 1 phút     │     │ ⏱ 4 phút 🔴  │     │ ⏱ 2 phút 🔴  │     │ ⏱ 1 phút     │
│ In: Nội dung │     │ In: Nội dung │     │ In: Chủ đề   │     │ In: Phòng ban│
│ raw          │     │ raw          │     │ đã xác định  │     │ đã chọn      │
│ Out: Ticket  │     │ Out: Nhãn chủ│     │ Out: Tên     │     │ Out: Ticket  │
│ đã log       │     │ đề           │     │ phòng ban    │     │ đã route     │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
🔴 = Bottleneck   🔄 = Handoff (người-hệ thống / người-người)
⏱ Tổng thời gian xử lý thủ công: 8 phút/lượt.
```

## 3.2. Problem Statement (6-field)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên CSKH (Customer Support) tại trung tâm chăm sóc khách hàng VinFast. |
| **2. Current Workflow** | Ticket khiếu nại đổ về từ 3 kênh (App, Hotline ghi âm chuyển văn bản, mạng xã hội). CS đọc từng ticket, tự phán đoán chủ đề (pin/phần mềm/khác), tra bảng phân công nội bộ để tìm đúng phòng ban tiếp nhận, rồi gắn nhãn và chuyển ticket đi. 4 bước, hoàn toàn thủ công, mất 8 phút/lượt. |
| **3. Bottleneck** | Bước 2 & 3 (mất 6 phút): Đọc hiểu ý định khách hàng từ văn bản tự do (đặc biệt ticket dài, đa chủ đề) và tra cứu đúng phòng ban phù hợp — dễ hiểu sai ý khách, gây route nhầm phòng ban. |
| **4. Business Impact** | Ước tính ~150 ticket/ngày trên toàn hệ thống. Route sai gây ticket bị chuyển qua lại giữa các phòng ban (re-routing), kéo dài thời gian phản hồi khách hàng trung bình, ảnh hưởng SLA CSKH và điểm hài lòng khách hàng (CSAT). *(Số liệu khối lượng ticket/ngày và tỉ lệ route sai hiện tại là giả định ban đầu của nhóm — [GIẢ ĐỊNH: cần đối chiếu số liệu thật từ phòng CSKH VinFast trước khi dùng để quyết định ngân sách].)* |
| **5. Success Metric** | 1. 85% ticket được AI gợi ý đúng phòng ban trong dưới 10 giây (Quality).<br>2. Giảm thời gian xử lý từ 8 phút xuống dưới 2 phút/lượt (Efficiency). *(Đây là mục tiêu giả thuyết ban đầu — xem ghi chú giả định ở mục 4, cần baseline thực tế trước khi chốt.)* |
| **6. Operational Boundary** | AI được phép: đọc nội dung ticket, gợi ý (không tự động chốt) chủ đề + phòng ban nhận, kèm % độ tin cậy. **CẤM:** AI không được tự động đóng ticket hoặc trả lời trực tiếp khách hàng; không được tự ý chuyển ticket đi khi độ tin cậy dưới ngưỡng (ví dụ < 80%) — bắt buộc CS xác nhận trước khi gửi đi (HITL). |

## 3.3. Future-State Flow & AI Fit

* **AI Fit:** Chọn **LLM Feature** (không cần Agentic Loop vì chỉ có 1 bước ra quyết định — phân loại + gợi ý phòng ban — không cần AI tự lập kế hoạch nhiều bước hay gọi nhiều công cụ liên tiếp).
* **Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận ticket  │     │ 🔵 AI phân   │     │ 🟢 CS xem    │     │ Ticket được  │
│ từ 3 kênh    │ ──→ │ loại chủ đề +│ ──→ │ gợi ý, xác   │ ──→ │ route đi     │
│              │     │ gợi ý phòng  │     │ nhận/sửa rồi │     │              │
│              │     │ ban + % tin  │     │ duyệt        │     │              │
│              │     │ cậy          │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                  │
                                                  ▼
                                           ↩️ Fallback: Nếu độ tin cậy AI < 80%
                                           hoặc AI lỗi/timeout, ticket rơi về
                                           hàng đợi phân loại thủ công như cũ,
                                           không chặn luồng xử lý.
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? *(Có log ticket lịch sử từ hệ thống CSKH, cần làm sạch/gán nhãn trước khi fine-tune prompt.)*
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? *(Có — AI chỉ gợi ý, CS luôn là người duyệt cuối, có ngưỡng tin cậy + fallback về quy trình thủ công.)*
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? *(Chưa xác nhận — cần khảo sát ý kiến team CSKH trước khi triển khai đại trà.)*

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[ ] GO (Bắt đầu xây dựng Prototype)
[x] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline)**
[ ] NO-GO (Không khả thi / Rule-based tốt hơn)

**Justification:**
> Bài toán có AI Fit hợp lý (LLM Feature, rủi ro kiểm soát được qua HITL + Fallback) và metric mục tiêu rõ ràng, nhưng nhóm hiện chưa có số liệu thực tế về khối lượng ticket/ngày, tỉ lệ route sai hiện tại, và mức độ sẵn sàng thay đổi quy trình của đội CSKH — các con số trong mục 3.2/3.3 đều là giả thuyết ban đầu của nhóm, chưa được xác thực (xem `03-ai-log.md` về rủi ro AI tự đặt số liệu chưa kiểm chứng). Quyết định **NOT YET**: cần 1-2 tuần thu thập baseline thật (khối lượng, tỉ lệ lỗi route hiện tại, khảo sát stakeholder) trước khi cam kết ngân sách xây prototype.
