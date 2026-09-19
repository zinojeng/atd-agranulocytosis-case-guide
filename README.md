# ATD agranulocytosis 跨專科病例指南

這是一份以繁體中文整理的公開、去識別化臨床研究資料庫。主題是 severe antithyroid drug（ATD）associated agranulocytosis 發生後，如何重新評估 drug causality、infection、HFrEF、thyroid nodules、non-thionamide bridge，以及 thyroidectomy／I-131 兩條 definitive treatment 路徑。

Medical terms 與 drug names 保留 English，方便與原始文獻核對。內容供病例討論與研究教育使用，不是個別病人的處方或醫療指示。

## 第一次閱讀：從這三份開始

1. [START HERE：五分鐘閱讀地圖](START_HERE.md)
2. [去識別化病例摘要](01-case/case-summary.md)
3. [完整病例研究與臨床問題](01-case/comprehensive-review.md)

如果只想比較各專家的觀點，可直接閱讀[多方專家共識、分歧與交叉質疑](02-clinical-topics/expert-consensus.md)。

## Repo 結構

| 目錄 | 內容 | 適合誰 |
|---|---|---|
| [`01-case/`](01-case/) | 病例摘要、relative-day timeline、完整整合報告 | 第一次接觸本案的讀者 |
| [`02-clinical-topics/`](02-clinical-topics/) | Diagnosis、drug safety、infection、Lithium、I-131、surgery、HFrEF 與專家論點 | 臨床討論與教學 |
| [`03-evidence/`](03-evidence/) | Literature map、cross-reaction、G-CSF、bridge、case comparators 與來源查核 | 想核對證據與分母的讀者 |
| [`04-meeting-and-publication/`](04-meeting-and-publication/) | MDT 議程、CARE 缺口、投稿可行性與待補資料 | 會議主持、病例寫作與投稿 |
| [`05-original-research-notes/`](05-original-research-notes/) | 去識別化角色原稿與 QA reconciliation | 想追溯研究過程的讀者 |
| [`site/`](site/) | 公開網站的 generator 與靜態輸出 | 想重建或檢視網站的人 |

## 目前最重要的臨床結論

- Carbimazole 是時間關係最強的可疑藥物，但 allopurinol 的實際 exposure 尚未重建，因此不能寫成已證明的唯一原因。
- ANC 50/µL 符合 severe agranulocytosis。Carbimazole 起始後約第六至七週發病，位於常見時序內；文獻中的「約 85% 在 90 天內」是已發病病例的時間分布，不是服藥者的 absolute risk。
- Severe agranulocytosis 後通常不應常規改用 PTU。15.2%、30–34% 或 50% 等常見數字都不是可直接套用於本案的 agranulocytosis-specific recurrence rate。
- Day 51 ANC recovery、Day 54 CRP decline 與 pneumonia resolution 是不同終點。Day 57 仍有 necrotizing pneumonia 接近 abscess 的紀錄。
- FT4 在可確認的門診 lithium prescription 前已下降。缺 medication administration、服藥次數與 level timing 時，不能把 hormone improvement 歸因於 lithium。
- I-131 不是只看停 iodide 幾天。近期 Lugol、iodinated contrast、renal clearance、urinary iodine／RAIU 與等待期間能否控制 thyrotoxicosis都會影響 readiness。
- EF 約 32% 仍缺 updated echocardiography 與 etiologic workup。Thyroid function 改善後 EF 是否恢復，會同時改變 surgery risk 與等待 I-131 的風險。
- Thyroidectomy 與 I-131 都是條件式選項。選擇應納入 infection、cardiac status、uptake、nodules、bridge toxicity、治療速度與 patient preference。
- 目前沒有 Day 64 後 definitive treatment 與長期 outcome，因此適合 teaching analysis；尚不能寫成 successful case report 或宣稱「第一例」。

## 公開網站

- [病例指南首頁](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/)
- [多方專家論點與交叉審查](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/experts.html)
- [Lithium、停碘與 I-131](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/i131.html)
- [HFrEF 風險重評](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/cardiac.html)
- [來源索引](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/sources.html)

## 公開版資料邊界

本 repo 不包含病歷號、姓名、院所、醫護人員姓名、絕對就醫日期、原始病歷、Claude session identifiers、API keys、MCP 設定、付費解析服務設定、下載的全文 PDF 或機器解析全文。病例改用 Day 0 起算的 relative-day timeline，年齡只保留為五十多歲。

去識別化不等於已取得病例投稿同意。若要正式發表，仍需臨床團隊核對原始病歷、完成 institution／journal 要求、取得 patient consent，並重新評估罕見特徵組合造成的間接識別風險。

研究方法、資料保留原則與原 repo 對照見 [METHODS.md](METHODS.md) 與 [PUBLIC_RELEASE_NOTES.md](PUBLIC_RELEASE_NOTES.md)。
