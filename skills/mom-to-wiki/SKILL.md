---
name: mom-to-wiki
description: >
  Đọc file Biên Bản Họp (MOM) định dạng .docx từ thư mục MOM, phân tích trích xuất dữ liệu cuộc họp, tự động tạo file nháp .md trong thư mục cho người dùng review chỉnh sửa, sau khi người dùng chốt và xác nhận (confirm), đăng tải lên Confluence Wiki làm trang con tương ứng với loại cuộc họp (Daily Standup Meetings, Sprint planning hoặc Sprint review and Retrospective) bằng MCP Server. Tiêu đề trang con theo định dạng: 'Page chủ – dd/mm/yyyy'.
---

# MOM → Confluence Wiki Skill

Skill này tự động hóa quy trình phân tích biên bản cuộc họp (MOM) và đăng tải chúng lên Confluence Wiki của NDSVN qua 2 bước: tạo file nháp cục bộ để người dùng phê duyệt/điều chỉnh, sau đó upload lên đúng nhánh trang con của Space `MS`.

## Use this skill when

- Người dùng yêu cầu tải MOM lên Wiki / Confluence (ví dụ: "publish MOM lên wiki", "đẩy biên bản lên Confluence", "tạo wiki từ MOM").
- Cần tổng hợp hoặc làm rõ danh sách action items, các task đang và chưa hoàn thành từ biên bản họp ngày cụ thể.
- Người dùng đề cập đến file MOM hoặc file nháp wiki trong thư mục `d:\BA_And_Stuff\MOM` và muốn cập nhật trang Wiki.

## Do not use this skill when

- Trang Wiki cần tải lên không phải là Confluence của NDSVN hoặc nằm ngoài Space `MS`.
- Yêu cầu chỉ đơn thuần là dịch thuật hoặc tóm tắt văn bản thông thường không liên quan đến việc publish tài liệu cuộc họp.
- File biên bản cuộc họp ở định dạng không hỗ trợ (không phải `.docx` hoặc `.md`).

## Hướng dẫn các bước thực hiện (Instructions)

### Giai đoạn 1: Đọc MOM và Tạo file nháp Markdown (.md)
1. **Xác định file MOM đầu vào**: Quét thư mục `d:\BA_And_Stuff\MOM` để tìm các file `.docx` mới nhất hoặc theo yêu cầu cụ thể của người dùng.
2. **Parse nội dung biên bản**: Chạy script `scripts/parse_mom.py` để trích xuất thông tin cuộc họp (dự án, ngày họp, thành viên, action items, tasks, retro).
3. **Tạo file nháp cục bộ**:
   - Chuyển đổi dữ liệu JSON thành tài liệu Markdown đẹp mắt (có bảng biểu và link mention).
   - Lưu tài liệu nháp thành file `.md` trong thư mục `d:\BA_And_Stuff\MOM` (ví dụ: `DailyMeeting_120626_wiki-draft.md`).
4. **Thông báo cho người dùng**: Gửi thông báo bằng tiếng Việt chỉ ra đường dẫn file `.md` vừa tạo, ví dụ: *"Em đã tạo file nháp tại [đường dẫn]. Anh/chị vui lòng điều chỉnh trực tiếp trên file nháp này. Khi nào hoàn thành, hãy phản hồi 'confirm' hoặc 'chốt' để em đăng lên Confluence."* và **dừng lại chờ**.

### Giai đoạn 2: Đăng tải sau khi có xác nhận (Confirm)
1. **Đọc nội dung cuối**: Đọc lại toàn bộ nội dung file `.md` nháp sau khi người dùng đã tự tay chỉnh sửa trong workspace.
2. **Định tuyến ID trang cha (`parentId`)**: Dựa trên loại cuộc họp hoặc tên file nháp để xác định ID trang cha tương ứng:
   - **DailyMeeting** (Daily Standup) ➔ Parent ID: `164660481` (Daily Standup Meetings)
   - **ReviewAndRetro** (Sprint Review & Retrospective) ➔ Parent ID: `177373263` (Sprint review and Retrospective)
   - **SprintPlanning** (Sprint Planning) ➔ Parent ID: `177373261` (Sprint planning)
3. **Định dạng Tiêu đề trang**: Cú pháp: `[Tên trang chủ] – [Ngày cuộc họp (dd/mm/yyyy)]`
   - *Ví dụ*: `Daily Standup Meetings – 12/06/2026` hoặc `Sprint planning – 15/06/2026`.
4. **Publish lên Confluence**: Chuyển đổi nội dung Markdown sang HTML Storage Format và sử dụng MCP Server `ndsvn-confluence` để tạo trang con dưới trang cha tương ứng.
5. **Xác nhận kết quả**: Trả về link Confluence của trang con vừa tạo để người dùng kiểm chứng.

---

## Các Phase xử lý chi tiết của Agent

### Phase 1: Phân tích file .docx và tạo nháp Markdown
- Đọc file Word bằng script `python scripts/parse_mom.py "<docx_path>"`.
- Phân tích thông tin cuộc họp và lập danh sách các mục:
  - Cập nhật định dạng tên người phụ trách sang dạng `@username` tương ứng (ví dụ: `@dinh.quan`, `@huy.vo`,...) dựa trên playbook.
- Tạo file `.md` nháp tại `d:\BA_And_Stuff\MOM\[tên-file]-wiki-draft.md`.
- Trả lời người dùng: Gửi link file `.md` và hướng dẫn họ chỉnh sửa rồi phản hồi lại để bắt đầu Phase 2.

### Phase 2: Chờ người dùng xác nhận và Đăng tải lên Wiki
- Đợi người dùng gửi tin nhắn chốt / xác nhận (ví dụ: "chốt", "đẩy lên đi", "confirm").
- Đọc lại nội dung file `.md` đã chỉnh sửa.
- Trích xuất tiêu đề mới và phân loại cuộc họp từ file nháp:
  - `DailyMeeting` ➔ trang cha ID `164660481`
  - `ReviewAndRetro` ➔ trang cha ID `177373263`
  - `SprintPlanning` ➔ trang cha ID `177373261`
- Chuyển đổi Markdown sang HTML Storage Format (XHTML). Ánh xạ thẻ `@username` sang thẻ mention của Confluence Server: `<ac:link><ri:user ri:username="username" /></ac:link>`.
- Sử dụng các tool của MCP `ndsvn-confluence` (ví dụ: `confluence_create_page` hoặc `createConfluencePage`) để publish trang.
- Trả về đường link kiểm chứng dạng: `https://wiki.ndsvn.vn/pages/viewpage.action?pageId=PAGE_ID` cho người dùng.
