---
name: internet-research
description: Hướng dẫn chuyên sâu về nghiên cứu thông tin trên Internet, tối ưu hóa câu truy vấn, chọn lọc nguồn tin cậy, trích xuất nội dung và đối chiếu kiểm chứng thông tin.
---

# Internet Research Skill

Skill này hướng dẫn agent cách thực hiện nghiên cứu thông tin trên Internet một cách chuyên nghiệp, hiệu quả, và chính xác nhằm phục vụ cho việc lập trình, giải quyết lỗi, phân tích đối thủ, hoặc cập nhật tài liệu kỹ thuật.

## Use this skill when

- Cần tìm tài liệu tham khảo API (API references), thư viện mới nhất, hoặc các mẫu thiết kế code (code design patterns) chưa có sẵn trong workspace.
- Gặp lỗi kỹ thuật lạ, lỗi từ trình biên dịch/trình thông dịch và cần tìm kiếm giải pháp trên GitHub Issues, StackOverflow, hoặc các diễn đàn kỹ thuật uy tín.
- Cần thực hiện phân tích thị trường, nghiên cứu đối thủ cạnh tranh, hoặc thu thập số liệu thống kê từ Internet.
- Cần tóm tắt tài liệu, sách trắng, hoặc bài viết dài từ các URL cụ thể.

## Do not use this skill when

- Nhiệm vụ chỉ yêu cầu thao tác trên các tệp tin cục bộ có sẵn trong workspace (ví dụ: refactor code, viết unit test dựa trên logic hiện có).
- Tìm kiếm thông tin nội bộ của dự án hoặc thông tin nhạy cảm của người dùng.
- Cần tương tác với các trang web yêu cầu đăng nhập bằng tài khoản cá nhân, xác thực hai lớp (2FA), hoặc giải mã CAPTCHA.

## Instructions

1. Xác định rõ ràng mục tiêu nghiên cứu và các từ khóa cốt lõi trước khi thực hiện tìm kiếm.
2. Xây dựng ít nhất 3 biến thể câu truy vấn khác nhau để bao phủ tối đa kết quả tìm kiếm có liên quan.
3. Sử dụng công cụ `search_web` để tìm kiếm thông tin ban đầu, sau đó chọn lọc các liên kết uy tín nhất (ví dụ: tài liệu chính thức, blog kỹ thuật nổi tiếng, Github, StackOverflow).
4. Sử dụng công cụ `read_url_content` để đọc sâu nội dung của các trang web được chọn.
5. Đối chiếu thông tin từ nhiều nguồn độc lập, phát hiện và làm rõ các điểm mâu thuẫn trước khi đưa ra kết luận.
6. Trích dẫn đầy đủ nguồn tham khảo (URL) cho các tuyên bố hoặc đoạn code quan trọng.

## Phase 1: Xây dựng câu truy vấn & Chiến lược tìm kiếm (Query Formulation & Search Strategy)

Để thu được kết quả chính xác cao, cần tối ưu hóa các từ khóa tìm kiếm:

- **Sử dụng toán tử tìm kiếm cơ bản**:
  - Đặt cụm từ chính xác trong dấu ngoặc kép (ví dụ: `"TypeError: Cannot read properties of undefined"`).
  - Sử dụng dấu trừ `-` để loại bỏ các từ khóa không liên quan (ví dụ: `nextjs app router -pages`).
  - Kết hợp từ khóa kỹ thuật cụ thể cùng với phiên bản (ví dụ: `react 19 state management`).
- **Tạo các biến thể câu hỏi**:
  - Dạng lỗi trực tiếp: Lấy thông tin stack trace hoặc thông điệp lỗi chính xác.
  - Dạng tính năng: Tìm tài liệu hướng dẫn (ví dụ: `how to implement JWT authentication in FastAPI`).
  - Dạng so sánh: Tìm so sánh các thư viện (ví dụ: `Zustand vs Redux Toolkit performance 2026`).

## Phase 2: Đánh giá & Chọn lọc nguồn thông tin (Source Evaluation & Filtering)

Khi nhận được danh sách kết quả từ `search_web`, không nên đọc ngẫu nhiên mà cần chọn lọc theo độ uy tín:

- **Các nguồn chính thống (Authoritative Sources)**:
  - Tài liệu chính thức của công nghệ/thư viện (ví dụ: `docs.nestjs.com`, `react.dev`).
  - Các trang web kỹ thuật cộng đồng lớn: `stackoverflow.com`, `github.com` (đặc biệt là mục Issues và Discussions).
  - Blog của các kỹ sư nổi tiếng hoặc tổ chức uy tín (ví dụ: `web.dev`, blog của Vercel, Microsoft).
- **Phân loại nguồn cần cảnh giác**:
  - Các bài viết tổng hợp tự động bằng AI kém chất lượng (thường không có code ví dụ thực tế hoặc thông tin lỗi thời).
  - Diễn đàn hoặc blog cá nhân chưa qua kiểm chứng, đặc biệt là khi bài viết đã quá cũ (trên 3 năm) đối với các công nghệ cập nhật nhanh.

## Phase 3: Trích xuất & Đọc nội dung chi tiết (Content Extraction & Deep Reading)

Sử dụng `read_url_content` để đọc nội dung trang web:

- **Đọc lướt (Scanning)**: Kiểm tra nhanh tiêu đề, các tiêu đề phụ (h2, h3) và các khối mã code (code blocks) để xác định bài viết có thực sự giải quyết vấn đề hay không.
- **Trích xuất thông tin quan trọng**:
  - Lấy các đoạn code ví dụ mẫu (code snippets).
  - Chú ý các cảnh báo bảo mật, lưu ý về hiệu năng, hoặc sự khác biệt giữa các phiên bản.
  - Theo dõi các đường link tham chiếu (citations) khác xuất hiện trong bài viết nếu cần đào sâu thêm.
- **Quản lý context budget**: Tránh đọc quá nhiều trang web cùng lúc. Tối đa chỉ nên đọc từ 3-5 bài viết chất lượng cao cho một vấn đề cụ thể.

## Phase 4: Tổng hợp & Kiểm chứng chéo (Synthesis & Cross-Referencing)

Tổng hợp dữ liệu thành báo cáo hoàn chỉnh:

- **Xác thực thực tế (Fact-Checking)**: Đối chiếu mã code hoặc thông tin giải pháp giữa các nguồn khác nhau để đảm bảo giải pháp không bị lỗi thời hoặc gây lỗ hổng bảo mật.
- **Ghi nhận sự mâu thuẫn**: Nếu nguồn A và nguồn B đưa ra hai cách giải quyết khác nhau, hãy phân tích ưu và nhược điểm của từng cách (ví dụ: về hiệu năng, độ phức tạp) thay vì chỉ chọn bừa một cách.
- **Lập tài liệu**: Trình bày kết quả nghiên cứu dưới dạng một báo cáo có cấu trúc rõ ràng bao gồm:
  - Tóm tắt kết quả tìm kiếm (Key Findings).
  - Mã code ví dụ đã được tối ưu hóa và kiểm tra.
  - Danh sách liên kết tham khảo (Sources list).
