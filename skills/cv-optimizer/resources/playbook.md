# Playbook: Cẩm nang Tối ưu hóa CV và Biên soạn LaTeX Chuyên nghiệp

Tài liệu này hướng dẫn các phương pháp chọn lọc từ ngữ, chuyển đổi câu từ sang phong cách ấn tượng và cách xử lý mã nguồn LaTeX an toàn để nâng cấp CV của người dùng.

---

## 1. Nguyên tắc nâng cấp câu từ (Phrasing Upgrades)

Nguyên tắc cốt lõi để gây ấn tượng với nhà tuyển dụng là loại bỏ lối viết "liệt kê công việc" (task-oriented) và thay thế bằng lối viết "làm nổi bật thành tựu và tác động" (result/impact-oriented).

### 1.1 So sánh diễn đạt Yếu (Weak) vs. Ấn tượng (Impressive)

| Nội dung gốc (Chưa tối ưu) | Diễn đạt nâng cấp (Tiếng Việt) | Diễn đạt nâng cấp (Tiếng Anh) | Yếu tố ấn tượng được thêm vào |
| :--- | :--- | :--- | :--- |
| Làm về hệ thống API cho mobile app. | **Thiết kế và phát triển** hệ thống RESTful API hiệu năng cao hỗ trợ hơn 50.000 người dùng hoạt động hàng ngày. | **Architected and deployed** high-performance RESTful APIs, successfully scaling backend services for 50K+ daily active users. | Động từ hành động mạnh, số lượng người dùng cụ thể. |
| Giúp sửa lỗi code và tăng tốc độ web. | **Chủ động debug** và **tối ưu hóa mã nguồn**, giúp giảm 40% thời gian phản hồi (response time) của trang web. | **Spearheaded debugging and performance tuning**, resulting in a 40% reduction in web page load times. | Số liệu đo lường cụ thể (40%), làm nổi bật tính chủ động. |
| Quản lý dự án YOLO phát hiện xe. | **Nghiên cứu và triển khai** mô hình YOLOv3 nhận diện phương tiện giao thông thời gian thực với độ chính xác đạt 92%. | **Engineered and optimized** a real-time YOLOv3 object detection pipeline, achieving a 92% mAP accuracy. | Chỉ số độ chính xác (92%), tính ứng dụng thực tế. |
| Tham gia viết tài liệu dự án. | **Biên soạn chuẩn hóa** toàn bộ tài liệu kỹ thuật của dự án, giúp rút ngắn 50% thời gian onboard cho thành viên mới. | **Standardized and compiled** comprehensive technical documentation, accelerating new developer onboarding speed by 50%. | Tác động thực tế (giảm thời gian onboard). |

---

## 2. Bảng tra cứu Động từ Hành động Song ngữ (Action Verbs)

Tránh lặp lại các từ như "làm", "phụ trách", "worked on", "managed". Hãy sử dụng đa dạng các từ sau:

### Nhóm Kỹ thuật & Phát triển (Engineering & Tech)
* **Tiếng Việt**: Thiết kế, Xây dựng, Khởi tạo, Tối ưu hóa, Triển khai, Tích hợp, Chuyển đổi, Lập trình.
* **Tiếng Anh**: Architected, Engineered, Developed, Deployed, Optimized, Integrated, Refactored, Debugged.

### Nhóm Sáng tạo & Cải tiến (Innovation & Creation)
* **Tiếng Việt**: Tiên phong, Sáng lập, Thiết lập, Cải tiến, Tái cấu trúc, Đơn giản hóa.
* **Tiếng Anh**: Spearheaded, Pioneered, Formulated, Streamlined, Modernized, Redesigned.

### Nhóm Phân tích & Nghiên cứu (Analysis & Research)
* **Tiếng Việt**: Điều tra, Đánh giá, Khảo sát, Dự báo, Thẩm định, Khai phá (dữ liệu).
* **Tiếng Anh**: Analyzed, Evaluated, Forecasted, Investigated, Extracted, Audited.

---

## 3. Quy tắc An toàn khi chỉnh sửa LaTeX (LaTeX Safety Guidelines)

Mã nguồn LaTeX rất nhạy cảm với cú pháp. Khi sửa đổi tệp `.tex`, Agent bắt buộc phải tuân theo các quy tắc sau để tránh lỗi biên dịch:

### 3.1 Escape các ký tự đặc biệt trong văn bản
* Ký tự phần trăm `%`: Trong LaTeX, `%` là bắt đầu comment. Để hiển thị dấu phần trăm trong câu (ví dụ: tăng 30%), bắt buộc phải viết là `30\%`.
* Ký tự và `&`: Thường dùng trong căn chỉnh bảng biểu. Nếu viết trong văn bản (ví dụ: R&D), phải viết là `R\&D`.
* Ký tự đô la `$`: Dùng để mở công thức toán học. Viết số tiền phải escape: `\$10,000`.
* Ký tự gạch dưới `_`: Phải viết là `\_` (ví dụ: `database\_helper`).

### 3.2 Bảo toàn cấu trúc môi trường
* Các cấu trúc danh sách liệt kê thường viết dưới dạng:
  ```latex
  \begin{itemize}
    \item Developed high-performance backend systems...
    \item Optimized database queries, reducing latency by 20\%...
  \end{itemize}
  ```
* Tuyệt đối không xóa hoặc làm lệch các lệnh `\begin{itemize}`, `\end{itemize}`, và `\item`. Chỉ thay thế phần nội dung chữ đứng sau `\item`.

### 3.3 Tránh lỗi xuống dòng
* Không dùng ký tự xuống dòng tùy tiện trong LaTeX. Để xuống dòng tạo khoảng cách nhỏ, có thể dùng `\smallskip` hoặc `\medskip`. Để xuống hàng trong cùng đoạn văn, dùng lệnh `\\` (tuy nhiên nên hạn chế trong danh sách `itemize`).

---

## 4. Bảng đồng bộ Thuật ngữ CV Song ngữ

| Tiếng Việt | Tiếng Anh (Chuyên nghiệp) |
| :--- | :--- |
| Kinh nghiệm làm việc | Professional Experience / Work History |
| Tóm tắt chuyên môn | Professional Summary / Profile |
| Học vấn | Education & Credentials |
| Dự án cá nhân / Dự án nổi bật | Key Projects / Portfolio |
| Kỹ năng chuyên môn | Technical Skills / Core Competencies |
| Người tham chiếu | References (Available upon request) |
