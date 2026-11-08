# Chuẩn bị cho sinh viên IT thời AI

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)

Talkshow 90 phút về những gì nhà tuyển dụng Fresher/Intern thực sự đánh giá — và cách chuẩn bị từ năm 3 đến khi có công việc IT đầu tiên.

Xây dựng bằng [markpress](https://github.com/davidecaminati/markpress) và impress.js.

## Bối cảnh

Thị trường IT ngày càng cạnh tranh, doanh nghiệp tuyển Fresher/Intern khắt khe hơn. Biết code và có CV tốt không còn đủ để được gọi phỏng vấn.

Buổi nói chuyện đứng về phía nhà tuyển dụng: hội đồng thực sự điền gì vào phiếu đánh giá, ứng viên bị loại ở đâu, AI đã thay đổi vòng phỏng vấn thế nào, và sinh viên có thể làm gì trong 12 tuần tới.

**Khán giả:** sinh viên IT năm 3–4 và người mới tốt nghiệp đang nộp hồ sơ.

**Bốn nội dung:**

1. Bức tranh tuyển dụng Fresher/Intern trong thời đại AI
2. Quy trình tuyển dụng và tiêu chí đánh giá ứng viên
3. Lộ trình chuẩn bị cho sinh viên năm 3, năm 4 và người mới tốt nghiệp
4. Hỏi đáp trực tiếp

## Build

```sh
npm install
npm run build      # → output/index.html và output/index.vi.html
npm run preview    # mở bản tiếng Anh
```

Cần Node.js 20. Nếu dùng [mise](https://mise.jdx.dev/), chạy `mise install` trước.

| Tệp kết quả | Ngôn ngữ |
|---|---|
| `output/index.html` | Tiếng Anh |
| `output/index.vi.html` | Tiếng Việt |
| `output/remote.html` | Remote trên điện thoại kèm speaker notes |

## Cấu trúc

| Đường dẫn | Mục đích |
|---|---|
| `slides/presentation.en.md` | Nội dung slide tiếng Anh |
| `slides/presentation.vi.md` | Nội dung slide tiếng Việt |
| `slides/images/` | Mã QR và icon |
| `research/findings.md` | Nguồn dữ liệu cho từng con số trên slide |
| `research/idea.md` | Ý tưởng, luận điểm và cấu trúc buổi nói chuyện |
| `build.cjs` | Script build và theming |
| `.agents/skills/` | Skill hướng dẫn viết và tạo style slide |

## Dàn ý

| # | Slide | Phần |
|---|---|---|
| 1–3 | Tiêu đề, câu hỏi mở, nội dung | Mở đầu |
| 4 | Ba điều các bạn từng được nghe | Mở đầu |
| 5–8 | Tỷ lệ entry-level, bậc thang ngắn lại, tiêu chuẩn mới, Việt Nam | Bức tranh |
| 9–10 | Phễu tuyển dụng, CV là bài toán xếp hạng | Quy trình |
| 11–13 | Tám ô đánh giá, tiêu chí loại trực tiếp, lý do bị loại | Tiêu chí |
| 14–15 | Cách AI được kiểm tra, công cụ phát hiện không đáng tin | Tiêu chí |
| 16–18 | Năm 3, năm 4, mới tốt nghiệp | Lộ trình |
| 19–20 | Bộ bằng chứng, 12 tuần tới | Lộ trình |
| 21 | Hỏi đáp | Kết thúc |

## Speaker notes

Speaker notes nằm trong HTML comment dưới mỗi slide. Các câu chuyện cá nhân được đánh dấu `[STORY: ...]` và cần thay bằng trường hợp thật trước khi trình bày.

## Nguồn

Mọi con số trên slide đều truy được về `research/findings.md`, tệp này cũng liệt kê những thống kê phổ biến bị loại bỏ vì không có nguồn gốc kiểm chứng được.

## Triển khai

Workflow `deploy-pages.yml` build và deploy mỗi lần push lên `main`.

Bật GitHub Pages: **Settings** → **Pages** → **Source**: `GitHub Actions`.

## Viết slide

Các slide phân tách bằng `------` (sáu dấu gạch ngang). Xem [`.agents/skills/markpress-content/SKILL.md`](.agents/skills/markpress-content/SKILL.md) để biết cách viết, và [`.agents/skills/markpress-styling/SKILL.md`](.agents/skills/markpress-styling/SKILL.md) cho phần theming.
