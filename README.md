# Antigravity Custom Skills

Repository này lưu trữ các skill tùy chỉnh (custom skills) được phát triển cho trợ lý ảo AI Antigravity nhằm phục vụ các quy trình công việc cá nhân.

## Danh sách các Skill

### 1. [mom-to-wiki](skills/mom-to-wiki)
* **Mục đích**: Tự động đọc và parse Biên Bản Họp (MOM) định dạng `.docx`, tạo file nháp Markdown và tự động đăng tải biên bản cuộc họp lên Confluence Wiki (NDSVN) thông qua Confluence MCP Server.
* **Cấu trúc**:
  * [SKILL.md](skills/mom-to-wiki/SKILL.md): Hướng dẫn định tuyến và quy tắc chung cho Agent.
  * [resources/playbook.md](skills/mom-to-wiki/resources/playbook.md): Cẩm nang chi tiết định dạng, ID các trang cha, mapping tài khoản.
  * [scripts/parse_mom.py](skills/mom-to-wiki/scripts/parse_mom.py): Script Python để phân tách thông tin từ file `.docx`.

### 2. [internet-research](skills/internet-research)
* **Mục đích**: Hướng dẫn chi tiết cho Agent thực hiện nghiên cứu Internet chuyên nghiệp, tối ưu hóa câu tìm kiếm và thẩm định thông tin đa nguồn.
* **Cấu trúc**:
  * [SKILL.md](skills/internet-research/SKILL.md): Hướng dẫn chung về quy trình nghiên cứu.
  * [resources/playbook.md](skills/internet-research/resources/playbook.md): Các cú pháp tìm kiếm nâng cao và ma trận đánh giá nguồn tin cậy.

### 3. [cv-optimizer](skills/cv-optimizer)
* **Mục đích**: Phân tích CV định dạng LaTeX của bạn, sửa từ ngữ yếu thành động từ hành động mạnh, thêm các chỉ số đo lường và thuật ngữ song ngữ Anh-Việt ấn tượng.
* **Cấu trúc**:
  * [SKILL.md](skills/cv-optimizer/SKILL.md): Định nghĩa các Phase xử lý của Agent trên LaTeX.
  * [resources/playbook.md](skills/cv-optimizer/resources/playbook.md): Cẩm nang so sánh diễn đạt Yếu vs. Ấn tượng, danh sách Action Verbs và quy tắc cú pháp LaTeX an toàn (escape ký tự đặc biệt).

### 4. [cover-letter-writer](skills/cover-letter-writer)
* **Mục đích**: Hỗ trợ soạn thảo thư xin việc Cover Letter trang trọng lịch sự, cá nhân hóa dựa trên thông tin CV và JD tuyển dụng, hỗ trợ cả tiếng Anh và tiếng Việt.
* **Cấu trúc**:
  * [SKILL.md](skills/cover-letter-writer/SKILL.md): Định nghĩa quy trình phân tích đầu vào và dựng cấu trúc Cover Letter.
  * [resources/playbook.md](skills/cover-letter-writer/resources/playbook.md): Mẫu cấu trúc thư tiêu chuẩn song ngữ Anh-Việt, lời chào kết lịch thiệp và checklist kiểm tra.

---
*Created and maintained using Antigravity IDE.*
