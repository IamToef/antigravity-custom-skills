---
name: cv-optimizer
description: >
  Phân tích tệp CV LaTeX của người dùng (như .tex), đề xuất tối ưu hóa câu từ chuyên nghiệp, nâng cao tính thuyết phục và định dạng chuẩn mực nhằm gây ấn tượng với nhà tuyển dụng. Hỗ trợ song ngữ Anh-Việt.
---

# CV Optimizer Skill

Skill này giúp Agent phân tích và nâng cấp CV định dạng LaTeX của người dùng thành một phiên bản chuyên nghiệp, tối ưu hóa cả về mặt ngữ nghĩa (chọn từ mạnh mẽ, cấu trúc câu rõ ràng, làm nổi bật thành tựu) và kỹ thuật định dạng LaTeX.

## Use this skill when

- Người dùng muốn cải thiện, nâng cấp CV hiện tại (đặc biệt là tệp LaTeX `.tex` đang mở hoặc trong workspace).
- Cần dịch thuật, chuyển đổi ngôn ngữ CV giữa tiếng Anh và tiếng Việt một cách tự nhiên và chuyên nghiệp.
- Người dùng yêu cầu tối ưu hóa CV để ứng tuyển vào một vị trí/công ty cụ thể hoặc muốn CV của mình "ấn tượng hơn" với nhà tuyển dụng.

## Do not use this skill when

- CV không phải ở dạng văn bản hoặc định dạng LaTeX mà ở dạng ảnh hoặc định dạng không thể đọc/chỉnh sửa trực tiếp.
- Người dùng yêu cầu tạo mới hoàn toàn một CV mà không cung cấp bất kỳ thông tin cá nhân hay nền tảng kinh nghiệm nào.

---

## Instructions (Hướng dẫn các bước thực hiện)

### Bước 1: Đọc và Phân tích cấu trúc LaTeX
1. Sử dụng các công cụ đọc file để đọc toàn bộ tệp `.tex` trong workspace (ví dụ: `cv_tran_tien_phong.tex`).
2. Xác định các phân mục chính của CV: Thông tin cá nhân, Học vấn (Education), Kinh nghiệm làm việc (Experience), Dự án (Projects), Kỹ năng (Skills).
3. Đọc hiểu mô tả công việc (Job Description - JD) nếu người dùng cung cấp, nhằm định vị các từ khóa then chốt cần làm nổi bật.

### Bước 2: Đề xuất cải tiến nội dung & Câu từ (Song ngữ)
1. **Kiểm tra động từ hành động (Action Verbs)**: Thay thế các từ diễn đạt thụ động hoặc yếu (ví dụ: *làm về, phụ trách, help with, worked on*) bằng các động từ hành động mạnh mẽ và chuyên nghiệp (ví dụ: *thiết kế, tối ưu hóa, tiên phong, lead, design, architect, spearhead*).
2. **Nâng cao tính thuyết phục**: Khảo sát các kinh nghiệm và bổ sung các con số, chỉ số đo lường hiệu quả (ví dụ: *giảm 30% thời gian xử lý, tăng 15% độ chính xác, tối ưu hóa tốc độ tải trang gấp 2 lần*) thay vì chỉ liệt kê các tác vụ hàng ngày.
3. **Đối chiếu chéo**: Đảm bảo thuật ngữ chuyên ngành được dịch và sử dụng chuẩn xác bằng cả tiếng Anh và tiếng Việt.

### Bước 3: Sửa đổi trực tiếp và Biên dịch kiểm tra
1. Thực hiện các chỉnh sửa trực tiếp vào mã nguồn LaTeX của tệp `.tex` theo từng khối (block) kinh nghiệm hoặc dự án để tránh xung đột cấu trúc.
2. **Quy tắc cú pháp LaTeX**:
   - Tránh làm hỏng các lệnh định dạng gốc như `\item`, `\begin`, `\end`, `\section`.
   - Đảm bảo các ký tự đặc biệt được escape đúng cách (ví dụ: `%` đại diện cho phần trăm trong văn bản phải viết là `\%` để tránh bị LaTeX coi là comment).
   - Kiểm tra các cặp dấu ngoặc nhọn `{}` luôn đóng mở đầy đủ.
3. Khuyến nghị người dùng biên dịch thử sang PDF để kiểm tra bố cục hiển thị cuối cùng.

---

## Các Phase xử lý chi tiết của Agent

### Phase 1: Đọc mã nguồn LaTeX và Đánh giá sơ bộ
- Đọc nội dung file `.tex` trong workspace.
- Tạo một báo cáo đánh giá sơ bộ chỉ ra:
  - Điểm mạnh hiện tại của CV.
  - Những phần nội dung còn mơ hồ, thiếu số liệu hoặc dùng từ ngữ chưa đủ ấn tượng.
  - Các lỗi định dạng LaTeX tiềm ẩn (nếu có).

### Phase 2: Soạn thảo nội dung tối ưu hóa
- Trình bày cho người dùng các đoạn văn bản/kinh nghiệm trước và sau khi tối ưu hóa (dạng bảng so sánh hoặc diff) để người dùng duyệt trước.
- Áp dụng các mẫu câu và từ vựng từ playbook của skill này để nâng tầm tính chuyên nghiệp.
- Dịch và đồng bộ hóa nội dung song ngữ Anh - Việt theo yêu cầu.

### Phase 3: Áp dụng thay đổi vào file LaTeX
- Thực hiện thay đổi vào file `.tex` sử dụng các công cụ thay thế nội dung file thích hợp.
- Giữ nguyên bố cục thẩm mỹ ban đầu của mẫu LaTeX (không thay đổi cấu trúc bảng biểu, font chữ trừ khi người dùng yêu cầu).
- Báo cáo kết quả và hướng dẫn người dùng cách biên dịch kiểm tra.
