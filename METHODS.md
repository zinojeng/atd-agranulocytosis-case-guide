# 研究方法與證據邊界

## Case reconstruction

臨床資料先由本機原始 UTF-8 Markdown 病歷核對，再製作去識別化摘要。公開資料只保留 relative days、必要的 laboratory／imaging values 與會影響推理的紀錄歧異。原始病歷從未納入本公開 repo，也沒有送交文獻搜尋或 PDF 解析服務。

## Multi-role review

研究曾分別以 Endocrinology、Hematology／Drug Safety、Nuclear Medicine／Surgery、Case Diagnosis、Infection／Clinical Pharmacology、Definitive Therapy 與 Evidence／Publication Methods 視角分析。公開主閱讀區將這些內容重新整理為臨床主題；原始去識別化角色稿保留在 [`05-original-research-notes/`](05-original-research-notes/)，供需要追溯的人閱讀。

## Source hierarchy

1. Guideline／consensus：界定一般準備、contraindications 與 safety framework。
2. Randomized trial／cohort：提供群體效果與平均結果；仍需核對 inclusion／exclusion。
3. Case series／case report：證明某個路徑曾被採用，不能估算本案成功率。
4. 本案推論：把外部證據套回個案，必須標示資料缺口與條件。

重要數字盡量回到 original paper、guideline 或 official drug label，並記錄分母、研究設計與 locator。LlamaParse／OCR 文字只作搜尋索引；若圖表解析與原始 PDF 不一致，以原始 PDF 視覺核對為準。

## 這不是 systematic review

本研究採 targeted literature review，聚焦 thionamide cross-reaction、agranulocytosis timing、G-CSF、non-thionamide bridge、lithium、iodide washout、thyroidectomy／I-131、HFrEF 與 case-report comparators。不能主張檢索已窮盡所有文獻，也不主張病例是 first／unique。

## 公開版重新整理原則

- 保留可理解病例與證據所需的 Markdown 內容。
- 主要閱讀區移除 session transport、message IDs、runner 操作、prompt、測試與下載暫存等處理細節。
- 原始角色稿與 QA correction 保留在最後一區，並標明是歷史研究紀錄。
- 不公開 session UUID、raw logs、API credentials、MCP configuration、absolute local paths、原始病歷與 copyrighted full-text PDFs。
- 所有正式結論以 `01-case/comprehensive-review.md` 與主題整理稿為優先；archive 中被後續 QA 更正的早期句子不能覆蓋 final synthesis。

## Clinical and publication boundary

本 repo 供教育、研究與 MDT discussion 使用，不提供個別 dosing。正式病例投稿仍需要 patient perspective、publication consent、institutional requirements、完整 outcome 與再識別風險審查。
