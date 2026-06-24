# Playbook: Đăng tải MOM lên Confluence Wiki qua MCP Server

Tài liệu này hướng dẫn cách định dạng nội dung, sử dụng công cụ MCP Server `ndsvn-confluence` để tạo hoặc cập nhật trang biên bản cuộc họp dưới dạng trang con tùy thuộc vào loại cuộc họp.

---

## 1. Định tuyến các trang cha (Parent Pages Routing)

Tùy vào loại cuộc họp được trích xuất từ file MOM, Agent phải định tuyến trang mới làm trang con của đúng trang chủ tương ứng:

| Loại cuộc họp (Meeting Type) | ID trang cha (Parent ID) | Tiêu đề trang cha (Parent Title) | URL trang cha trên Confluence |
|-----------------------------|--------------------------|----------------------------------|------------------------------|
| **DailyMeeting** (Daily Standup) | `164660481` | `Daily Standup Meetings` | `https://wiki.ndsvn.vn/spaces/MS/pages/164660481/Daily+Standup+Meetings` |
| **ReviewAndRetro** (Sprint Review & Retro) | `177373263` | `Sprint review and Retrospective` | `https://wiki.ndsvn.vn/spaces/MS/pages/177373263/Sprint+review+and+Retrospective` |
| **SprintPlanning** (Sprint Planning) | `177373261` | `Sprint planning` | `https://wiki.ndsvn.vn/spaces/MS/pages/177373261/Sprint+planning` |

---

## 2. Quy tắc đặt tiêu đề trang con (Page Title Syntax)

Tiêu đề của trang con được tạo tự động theo cú pháp:
`[Tiêu đề trang cha] – [Ngày cuộc họp (format: dd/mm/yyyy)]`

*Ví dụ*:
- Nếu là Daily Meeting ngày 12/06/2026: `Daily Standup Meetings – 12/06/2026`
- Nếu là Sprint Planning ngày 15/06/2026: `Sprint planning – 15/06/2026`
- Nếu là Sprint Review & Retrospective ngày 12/06/2026: `Sprint review and Retrospective – 12/06/2026`

---

## 3. Luồng làm việc 2 giai đoạn (Mandatory 2-Step Flow)

Quy trình đăng tải MOM bắt buộc phải thực hiện qua 2 bước sau:

### Bước 1: Tạo file nháp Markdown cục bộ
1. Agent đọc và phân tích file `.docx` trong thư mục `d:\BA_And_Stuff\MOM`.
2. Tạo file nháp `.md` trực tiếp trong thư mục này với tên file trùng với tên file Word gốc (ví dụ: `DailyMeeting_120626_wiki-draft.md`).
3. Thông báo cho người dùng biết vị trí của file nháp và dừng lại để người dùng tự do điều chỉnh nội dung trực tiếp trên file đó.

### Bước 2: Đăng tải sau khi có xác nhận (Confirm)
1. Khi người dùng phản hồi xác nhận (ví dụ: "publish nhé", "chốt", "đẩy lên đi", "confirm"), Agent sẽ đọc lại toàn bộ nội dung trong file `.md` đã được người dùng chỉnh sửa.
2. Chuyển đổi nội dung `.md` cuối cùng sang định dạng lưu trữ HTML của Confluence (Storage Format).
3. Đăng tải lên Confluence dưới trang cha tương ứng và trả về link trang con để người dùng kiểm chứng.

---

## 4. Bảng mapping tài khoản (User Mapping Table)

Để gắn thẻ `@mention` chính xác cho các thành viên, hãy sử dụng bảng tra cứu tài khoản dưới đây:

| Tên hiển thị trong MOM | Username / Account ID | Email đề xuất (nếu cần search) |
|-------------------------|-----------------------|--------------------------------|
| Định Quân               | `dinh.quan`           | `dinh.quan@ndsvn.vn`           |
| Huy Võ / Võ Quốc Huy    | `huy.vo`              | `huy.vo@ndsvn.vn`              |
| Hải Đào / Đào Minh Hải  | `hai.dao`             | `hai.dao@ndsvn.vn`             |
| Duy Hồ / Hồ Võ Hoàng Duy| `duy.ho`              | `duy.ho@ndsvn.vn`              |
| Khánh Đồng / Đồng Quốc Khánh| `khanh.dong`      | `khanh.dong@ndsvn.vn`          |
| Khoa Nguyễn / Nguyễn Vũ Anh Khoa| `khoa.nguyen` | `khoa.nguyen@ndsvn.vn`         |
| Trần Văn Đức            | `duc.tran`            | `duc.tran@ndsvn.vn`            |
| Hoàng Tiến              | `tien.hoang`          | `tien.hoang@ndsvn.vn`          |
| Phạm Xuân An            | `an.pham`             | `an.pham@ndsvn.vn`             |
| Trần Tiến Phong         | `phong.tran`          | `phong.tran@ndsvn.vn`          |

---

## 5. Cú pháp định dạng @mention trong Confluence

- **Storage Format (HTML/XHTML)**:
  ```html
  <ac:link><ri:user ri:username="dinh.quan" /></ac:link>
  ```
- **Atlassian Document Format (ADF - JSON)**:
  ```json
  {
    "type": "mention",
    "attrs": {
      "id": "ACCOUNT_ID",
      "text": "@Định Quân",
      "userType": "DEFAULT"
    }
  }
  ```
