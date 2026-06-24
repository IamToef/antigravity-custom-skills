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

---
*Created using Antigravity IDE and Skill Creator.*
