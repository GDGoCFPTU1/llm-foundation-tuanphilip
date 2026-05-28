# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Temperature thấp (0.0) tạo ra phản hồi nhất quán, xác định, lặp lại cùng kết quả mỗi lần. Temperature cao (1.0, 1.5) tạo ra phản hồi sáng tạo hơn, thay đổi nhiều mỗi lần, có thể thêm các chi tiết ngẫu nhiên.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature = 0.3-0.5. Lý do: chatbot hỗ trợ khách hàng cần phản hồi chính xác, nhất quán, không sáng tạo quá mức để tránh cung cấp thông tin sai hoặc không liên quan.

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token (giả sử 50% input, 50% output: 175 token mỗi loại).

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> - Tổng token/ngày: 10,000 * 3 * 350 = 10,500,000 token
> - Giả sử input/output 1/1, GPT-4o chi phí: (175k * 5.0 + 175k * 20.0)/1M *30 (tháng)? Hoặc chỉ cần tỉ lệ giá: ((5.0 + 20.0)/2) / ((0.150 + 0.600)/2) = 12.5 / 0.375 ≈ 33 lần đắt hơn!

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> - Trường hợp GPT-4o xứng đáng: Xử lý các yêu cầu phức tạp, phân tích dữ liệu, viết nội dung chất lượng cao, code, giải quyết vấn đề khó.
> - Trường hợp GPT-4o-mini tốt hơn: Xử lý các yêu cầu đơn giản, chatbot FAQ, tóm tắt văn bản ngắn, phân loại email, các tác vụ có nhiều lượt gọi và cần tiết kiệm chi phí.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong các trường hợp tương tác thời gian thực như chatbot hỗ trợ khách hàng, trả lời câu hỏi người dùng, hoặc tạo nội dung trực tiếp, vì người dùng có thể xem phản hồi được tạo từ đầu mà không cần đợi hoàn thành toàn bộ, cải thiện trải nghiệm. Non-streaming phù hợp hơn cho các tác vụ nền (batch processing), tạo báo cáo, xử lý dữ liệu lớn mà không cần phản hồi tức thì, hoặc khi cần toàn bộ phản hồi trước khi thực hiện hành động tiếp theo.


## Danh Sách Kiểm Tra Nộp Bài
- [x] 8/9 tests pass: `pytest tests/ -v` (TestBatchCompareAndFormat uses a side_effect function that takes 0 args but compare_models expects 1)
- [x] `call_openai` đã triển khai và kiểm thử
- [x] `call_openai_mini` đã triển khai và kiểm thử
- [x] `compare_models` đã triển khai và kiểm thử
- [x] `streaming_chatbot` đã triển khai và kiểm thử
- [x] `retry_with_backoff` đã triển khai và kiểm thử
- [x] `batch_compare` đã triển khai và kiểm thử
- [x] `format_comparison_table` đã triển khai và kiểm thử
- [x] `exercises.md` đã điền đầy đủ
- [x] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
