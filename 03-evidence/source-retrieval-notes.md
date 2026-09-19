# 文獻取得與 LlamaParse 解析紀錄

執行日期：2026-09-19（Asia/Taipei；UTC 記錄跨 2026-09-18）。本輪完成 **11 篇有效 PDF、11 篇 LlamaParse Markdown**。完整檔案位於本機 `literature/`，PDF 與全文 Markdown 不加入 GitHub；可版本控管的 `research/source_manifest.json` 保留 DOI、來源、逐次取得狀態、頁數、檔案大小及 SHA-256。

## 重要解析品質限制

**Nakamura 2013 的 LlamaParse 輸出含不可靠的圖轉表數字。** 獨立 reviewer 對照原始 PDF 後，確認 PDF 第 3 頁 Figure 1、2、3 的機器生成數值表不是忠實轉錄，**禁止據此引用數字或再分析**。Figure 5 尚未完成視覺核對，不能宣稱已確認錯誤；其圖轉表數字同樣不得在未核實前取數。保留原始解析檔及 hash 作為稽核記錄；取數應直接回到 PDF。這與原文自身的分母差異是兩件事：正文／Figure 2 分別出現 461／458、超過 4 個月 55／54；abstract／正文另有 84.5%／84.6% 差異，應保留差異而非擅自修正。

**Parse completed ≠ scientifically validated。** LlamaParse 的「已完成」只表示服務成功回傳 Markdown，**不代表 OCR、圖表或醫學內容已全部通過人工驗證**。所有文章均已做 PDF signature、可讀頁數、標題／DOI 身分核對及 hash 檢查；關鍵表格、圖形、分母與劑量需以 PDF 再核對。

已完成的重點視覺查核：Nakamura PDF 第 3 頁 Results／Figure 2（root 與 crossreaction reviewer）；EANM PDF 第 3 頁 Table 1（root）；Meyer-Gessner 期刊第 169 頁與 Otsuka 第 313–314 頁（crossreaction reviewer）；Wiberg PDF 第 1 頁文章身分（retrieval operator）；Vicente PDF 第6頁 reference32年份（root）。這些都是局部查核，不能推論所有機器解析內容均已驗證。

## 取得清單

| ID | 文獻 | PDF 頁數 | 實際成功管道 | LlamaParse |
|---|---|---:|---|---|
| `eta2018` | [ETA 2018 Graves guideline](https://doi.org/10.1159/000490384) | 20 | direct_open_access | 已完成 |
| `eanm2023` | [EANM 2023 RAI guideline](https://doi.org/10.1007/s00259-023-06274-5) | 25 | direct_open_access | 已完成 |
| `nakamura2013` | [Nakamura 2013（754 cases）](https://doi.org/10.1210/jc.2013-2569) | 8 | research_hub.download_papers_batch | 已完成 |
| `wiberg1972` | [Wiberg & Nuttall 1972](https://doi.org/10.7326/0003-4819-77-3-414) | 3 | research_hub.download_papers_batch | 已完成 |
| `knight2017` | [Knight 2017（multi-drug bridge→thyroidectomy）](https://doi.org/10.1530/EDM-17-0071) | 7 | institutional_repository_figshare | 已完成 |
| `prakash2015` | [Prakash 2015（Lithium）](https://doi.org/10.1155/2015/869343) | 5 | scihub.download_pdf | 已完成 |
| `vicente2017` | [Vicente 2017（narrative review）](https://doi.org/10.1007/s40268-017-0172-1) | 6 | direct_open_access | 已完成 |
| `meyergessner1989` | [Meyer-Gessner 1989（德文原始研究）](https://doi.org/10.1055/s-2008-1066570) | 6 | research_hub.download_papers_batch | 已完成 |
| `otsuka2012` | [Otsuka 2012（rash/hepatotoxicity）](https://doi.org/10.1111/j.1365-2265.2012.04365.x) | 6 | research_hub.download_papers_batch | 已完成 |
| `lugol2017` | [Calissendorff 2017（Lugol’s solution）](https://doi.org/10.1530/EC-17-0025) | 17 | scihub.download_pdf | 已完成 |
| `ki_rai2024` | [Tamura 2024（KI→RAI）](https://doi.org/10.1007/s00259-023-06523-7) | 10 | scihub.download_pdf | 已完成 |

版本差異：Prakash PDF 為 4 頁文章加 1 頁出版社廣告；廣告不是臨床證據。Knight PDF 含 1 頁 institutional repository 封面，PDF 第 2–7 頁才是文章第 1–6 頁。Lugol 研究取得 17 頁 publish-ahead-of-print 版本，期刊正式頁碼為 200–205。其餘頁數以實際 PDF 計算。

## 管道與失敗紀錄

1. 透過使用者已設定的 `research_hub` MCP 執行 DOI batch download；首批 MCP 自稱 4 篇成功，但 EANM/Vicente 兩個檔案實際為 HTML challenge。驗證器拒絕視為 PDF，也未上傳給 LlamaParse，之後從公開可取得的 PDF 來源補齊。
2. 對未取得的文獻使用已獲授權的 `scihub` MCP fallback。Prakash、Lugol 與 KI→RAI 最終由此取得有效 PDF。某些 PMC、出版社與 Sci-Hub 回應未提供有效 PDF，逐筆記錄仍保留，不能以 MCP 的成功字樣作為取證依據。
3. Knight 文獻由 institution Figshare 提供的 PDF 補齊，下載檔案 MD5 與 repository API 公開的 MD5 相符；詳見 manifest 的 repository_record。
4. 透過 `llamaparse` MCP 呼叫 LlamaParse REST job API，將 11 篇已驗證的公開文獻轉成 Markdown。新 API key 僅存在執行程序環境，不寫入腳本、manifest、報告或 Git。
5. 本流程沒有讀取或上傳病歷。上傳範圍限定 manifest 中的 `literature/<id>.pdf`。

這是以臨床爭點為導向的 targeted retrieval，並非完整 systematic review；文獻沒有因下載順序取得更高的證據等級。尤其 case report、rash/hepatotoxicity switch cohort 與 agranulocytosis 再暴露風險不能混成相同分母。

## 重跑方式

原研究環境使用 `mcp`、`httpx`、`pypdf`／`pdfinfo` 與 LlamaParse。公開版不保留本機 interpreter path、MCP configuration 或 credentials；解析輸出只作定位索引，關鍵結果仍需回到 publisher PDF 或官方 HTML 視覺核對。

```bash
python scripts/literature_pipeline.py audit
python scripts/literature_pipeline.py download --ids eta2018 eanm2023
python scripts/literature_pipeline.py download --ids knight2017 --scihub
# 先在呼叫程序的環境中安全設定 LLAMA_CLOUD_API_KEY，再執行：
python scripts/literature_pipeline.py parse
```

腳本具已完成結果的 hash 檢查，PDF 未更改且 Markdown hash 相同時不重複送出解析。若新版本 PDF 取代舊檔，會重新解析；任何文字的再產生仍需保留上述人工品質限制。驗證包含 `python -m py_compile`、全數 `audit`、11 組 PDF/Markdown hash 重算，以及 LlamaParse 返回結果與落地檔案一致性檢查。
