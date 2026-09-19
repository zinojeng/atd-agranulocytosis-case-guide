# 公開版整理說明

## 為什麼另建新 repo

原研究 repo 同時保存 multi-session workflow、runner、message transport metadata、prompts、tests、QA、研究稿與最終報告。這對稽核研究流程有用，但第一次進入 GitHub 的讀者很難判斷應先讀哪一份。

本公開 repo 把資訊改成線性閱讀順序：病例 → 臨床問題 → 文獻證據 → 會議／投稿 → 原始研究稿。檔案名稱也改成可直接理解的英文 slug，README 與每一區都提供入口。

## 保留了什麼

- 去識別化 case synopsis 與 relative-day timeline。
- 完整繁體中文病例整合報告。
- Diagnosis、Drug Safety／Infection、Definitive Therapy、HFrEF 與 expert viewpoints。
- Cross-reaction、bridge、G-CSF、lithium、RAI 與 case comparators 的文獻查核。
- MDT discussion、CARE gap 與 publication assessment。
- 第一輪與擴充輪的去識別化角色研究稿，以及最後 QA reconciliation。
- 公開網站的 generator 與 static output。

## 沒有複製什麼

- 原始病歷與檔名中的識別資訊。
- Claude session UUID、native message transport logs 與 receipts。
- Runner、resume commands、prompts、測試用 synthetic secret strings 與本機 automation settings。
- API keys、MCP configuration、absolute local paths。
- 下載的 publisher PDFs、Sci-Hub content 或 LlamaParse 全文輸出。
- 暫存檔、cache、logs 與重複的舊網站版本。

這些排除項目不影響一般讀者理解病例與證據，但可降低隱私、credential、版權與處理雜訊風險。

## 原 repo 與新位置對照

| 原內容 | 公開版位置 |
|---|---|
| `research/case_synopsis.md` | `01-case/case-summary.md` |
| `reports/expanded_case_review_zh_TW.md` | `01-case/comprehensive-review.md` |
| `roles/expanded_*` | 整理於 `02-clinical-topics/`；原稿另存 `05-original-research-notes/expanded/` |
| `research/independent_*_audit.md` | `03-evidence/` |
| `reports/conference_discussion_guide.md` | `04-meeting-and-publication/mdt-discussion-guide.md` |
| `reports/case_report_publication_assessment.md` | `04-meeting-and-publication/case-report-assessment.md` |
| `roles/*.md`、`qa/*.md` | `05-original-research-notes/` |
| website checkout | `site/` |

原始 private repo 保留完整工程與 workflow 歷史；此 repo 是供公開閱讀的 curated edition。
