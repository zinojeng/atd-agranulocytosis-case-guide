# 獨立臨床查核：cross-reaction、timing 與 case 時序

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

日期：2026-09-19。唯讀審閱 `reports/clinical_synthesis_zh_TW.md`，參照 `research/case_synopsis.md`；未開啟 private 原始病歷，亦未修改整合報告。以下行號對應本次閱讀版本。

**裁決：未發現會改變目前臨床結論的實質錯誤。** 個案六至七週時序、症狀與 ANC 確認時間的區分、停藥記載差異、resumption 與 rechallenge 的區分均一致。兩項原先未解決的文獻分母現在已核實，報告表格應更新；不應繼續將它們列為待查。

## CORRECTION：2026-09-19 書目與頁碼查核更正

本查核者先前在 `research/independent_crossreaction_audit.md` 將 Vicente 2017 的 reference 32 寫成 Meyer-Gessner 1989，這是我的書目辨識錯誤。Endocrinology／Methods sessions 提出疑義後，主協調者以 `literature/vicente2017.pdf` 第6頁的 `pdftotext` 文字及 render 影像確認，reference 32 實際是 **Meyer-Gessner 1994，DOI [10.1007/BF03344959](https://doi.org/10.1007/BF03344959)**。不能把這項錯誤歸為 Vicente 原文印刷錯誤。

下列 F1 的 1989 原始研究 p.169、5/33 整體 ADR 分母仍有獨立 PDF 視覺驗證；但 **2017→1994 的實際引用鏈需核對 1994 全文，現階段不能稱完整追源**。若報告沿用「Vicente reference 32 = 1989」或「完整追到 1989」的敘述，須更正。避免例行跨 thionamide 換藥，以及不把整體 ADR 當成 agranulocytosis-specific 再發率的核心結論不變。

另主協調者核對 [ATA 2016 原始 PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)，禁換 ATD 與 life-threatening thyroid storm 例外位於 [E6] 印刷 **p.1357**（PDF 第15頁，Recommendation 17 後、18 前）；本查核者先前在 audit 引用的 p.1358 不正確。[E7] minor reaction 換藥討論位於 p.1358。已同步修正 audit 的頁碼。

## 需更新的證據事項

### F1：第15行不再是「只有摘要、換藥分母未得」

Meyer-Gessner 1989 原始 PDF 第4頁／印刷 p.169 左欄首段，已 render 並視覺核對：

| 藥物配對 | 再有副作用的分子／換藥配對分母 | 比率 |
|---|---:|---:|
| Thiamazole（methimazole）／PTU | 4/29 | 13.8% |
| Carbimazole／PTU | 5/33 | 15.2% |
| Carbimazole／thiamazole | 11/34 | 32.4% |

13.8% 與15.2%是**不同藥物配對**，不是 MMI→PTU、PTU→MMI 的兩個方向。原文未分列方向、不同 ADR 的再發率，並明說未處理換藥前後的劑量可比性。報告「不是 agranulocytosis-specific 再發率」的結論正確，可保留。

來源：[原始研究 DOI](https://doi.org/10.1055/s-2008-1066570)，PMID [2464468](https://pubmed.ncbi.nlm.nih.gov/2464468/)；本機 `literature/meyergessner1989.pdf`。

### F2：第17行方向別分母已由原始 Table 4 核實

Otsuka 2012 原始 PDF 第4頁／印刷 p.313 Table 4及相鄰 Results：

- MMI→PTU：**14/41 = 34.2%** 有任何第二種 ATD 副作用；其中11/41因副作用停第二種ATD。
- PTU→MMI：**9/30 = 30.0%** 有任何第二種 ATD 副作用；其中6/30因副作用停第二種ATD。

不應把這些 all-ADR 比率替換成 rash 再發率。第5頁／p.314 Table 5列出的第二次 ADR 明細對應兩種藥均因副作用停用的17人，不能任意把其中5/29或3/9當作涵蓋所有新皮疹的事件率。JAMA review雖在rash語境給出30–50%並引用Otsuka，該區間本次**無法由原始Tables 4–5重現為完整rash-specific端點**。報告第16行僅把它用於追查口訣語境，並沒有將50%套入agranulocytosis，這個結論正確；可補上引用鏈尚未閉合的說明。

來源：[原始研究 DOI](https://doi.org/10.1111/j.1365-2265.2012.04365.x)，PMID [22332800](https://pubmed.ncbi.nlm.nih.gov/22332800/)；本機 `literature/otsuka2012.pdf`。Table 4與Table 5均已以render影像核對。

## 已核對且不需更改的內容

- 第8、32–40行：Day43症狀約6.1週、Day48 ANC確認約6.9週；「六至七週」合理。Day46只有WBC，未捏造同日ANC。Day47–48停藥差異保留。
- 第38行：門診lithium前FT4已下降，且第95行保留住院lithium是否真正給藥的未知；沒有把門診前當成從未暴露lithium。
- 第37、39行：ANC改善未單獨歸因G-CSF，也未拿ANC恢復取代感染清除。
- 第40行：Day64門診引用Day59檢驗，沒有假造新抽血。
- 第42行：Nakamura原始PDF p.4778的確同時出現Results n=461／55例與Figure2 caption n=458／54例，PDF視覺確認，並非只有OCR誤差；採約85%合理。總n=754與時間分析分母有區分。
- 第44行：Kobayashi resumed-course為之前未發病、重啟後首次agranulocytosis，不是已發病後安全rechallenge的證據。
- 第7、22、24行：禁例行換藥與真正thyroid storm例外有區分；allopurinol暴露未知亦保留，不宣稱carbimazole因果百分之百。

## 新找到的直接相關原始案例（補強，不是既有敘述錯誤）

第18行只列Chen1983，並如實指出其方向為PTU→MMI。Otsuka參考文獻15另提供 **Ostlere S, Apthorp GH. 1988. Recurrent agranulocytosis following carbimazole and propylthiouracil therapy. Br J Clin Pract 42(11):474–475. PMID3256337**。已核對[PubMed原始摘要](https://pubmed.ncbi.nlm.nih.gov/3256337/)，描述carbimazole與PTU依序給藥後再發。若要補強與本研究問題更接近的drug pair，可增列；仍只有case report，無法估計再發率。本次未取得其全文，不能補造詳細時間／ANC。

## 文獻解析品質附註

`literature/nakamura2013.md` 的Figure2圖轉表存在不可信數值：例如PTU多列大數、MMI隨時間規律增加，與p.4778原始圖中MMI占主要病例、PTU只少數柱段不符。Figure1／3亦不是原圖逐點忠實數據。已通知literature_pipeline；原始Markdown應保留可稽核版本，但圖轉表不得用來運算。報告目前使用原文正文與圖說的數值，未發現因此產生的錯誤。其餘圖形轉表亦應一律標示未驗證；本次未視覺核對Figure5。

`research/independent_crossreaction_audit.md` 已於同日更新F1/F2，加入全文補核紀錄與Nakamura原始PDF確認狀態；整合報告仍由主協調者修訂。

## Root整合狀態

F1/F2分母、Ostlere1988病例、ref32年份及ATA [E6]頁碼均已納入最終整合稿或原始證據表。上述行號及「需更新」描述保留當時審查快照；不代表最終稿仍缺少這些修正。
