# Root reconciliation：研究爭點、修正與未決資料

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

本文件記錄第一輪整合裁決，不把訊息送出當作對方同意。原始Claude session logs保留本機，`sessions/native_messages.json`是native SendMessage之message hash、ID與transport metadata匯出，預設不含原始訊息本文。公開於 repo 的少數歷史對話引文已依使用者更正作局部遮蔽，因此不再是完全逐字稿。最新個案判讀以`reports/expanded_case_review_zh_TW.md`優先。

## 已完成的證據裁決

| 議題 | 裁決／已實作修正 | 可核對的證據／角色往返 |
|---|---|---|
| Agranulocytosis後換PTU | 避免例行換另一thionamide，保留ATA life-threatening storm極有限例外；不以50%或15.2%當再發率 | CHALLENGE-hematology-001 → RESPONSE-endo-to-hema-001；ATA2016 E6；主稿第1節 |
| 15.2%來源／分母 | Root更正：Vicente2017原PDF第6頁ref32確為Meyer-Gessner1994，先前Director說1989是錯誤；1989原文另可獨立確認CBZ/PTU5/33的整體ADR，1994→1989引用鏈未完成。不得推估agranu約15%風險 | Endocrinology／Methods反駁Director；root以Vicente PDF第6頁視覺核對，接受專家對書目的質疑；Meyer1989 p169數據另行成立 |
| Otsuka換藥分母 | Table4 MMI→PTU14/41、PTU→MMI9/30；都是allADR。Table5停第二藥的17人不能當全部rash事件率 | 獨立QA F2、PDF p313–314；主稿證據表已更新 |
| 50%口訣 | JAMA2015 rash語境引用可追；尚未確認原始rash分母，不能說毫無二手來源，也不能套agranulocytosis | CHALLENGE-methods-001 → RESPONSE-endo-to-methods-001；獨立crossreaction audit |
| 發病時間 | 本案約43–48天，屬六至七週；Nakamura總754與時序n461/458分開，約85%且揭露原文差異 | Methods/Hematology交互查核；root與independent reviewer直接看PDF p4778 |
| G-CSF | 小型n24 RCT未顯示恢復時間效益，不能當成證實全無效；觀察研究不能證明本案before-after因果，更不能直接推出死亡率效益 | CHALLENGE-methods-002 ↔ CHALLENGE-hematology-002；RESPONSE from Hematology；原稿中唯一／無效的過強語氣被更正 |
| Lithium | 不能用單次低濃度追精神科目標；不能說完全沒有comparative／cohort資料；特定AKI＋HFrEF多藥安全性仍有證據缺口 | CHALLENGE-nuclear_surgery-001 → RESPONSE-endo-to-nucsurg-001；label及bridge audit |
| RAI／surgery | Lugol後仍可RAI；Lugol2–3wk、contrast6–8wk是一般準備框架且後者假设normal renal function；uptake與臨床狀態優先 | NuclearSurgery↔Methods cases外推挑戰；root PDF Table1視覺查核；independent_bridge_review無blocking finding |
| 原已撤回縮寫 | 已依使用者更正自臨床研究文件移除；hydrocortisone 僅依病歷獨立核對 | 使用者更正 |
| AKI現況 | 病史Cr已下降，不能稱當前仍unresolved AKI；保留近期AKI史及最新renal stability待補 | Root對NuclearSurgery初稿的修正；final review指令 |
| PDF轉MD | 11篇成功解析不等於全內容科學驗證；Nakamura Figures1/2/3圖轉表已證實不可靠，Figure5未驗證 | retrieval_report及source_manifest QC欄位；圖轉表數字未用於主稿 |

## 本機資料治理修正

第一輪某角色為確認治理狀態而違反brief，讀取原始檔頭並將來源檔名放入memo；其他角色也轉述了該檔名。root已要求清除識別資料並在最後出版前統一檢查；原始工具logs保持ignored，不公開。原始病歷原位置保留以尊重使用者檔案，另有private normalized copy；不能將「只有private/能有檔案」當作刪除使用者原稿的理由。最終repo只提交最小化識別資料摘要，仍維持private。

第二輪launcher移除Bash，限制可用built-in tools，並明列拒讀private與原始數字命名病歷。角色未再需要原始病歷即可完成研究。使用者後來指出舊來源其實是 RTF，並指定真正的 UTF-8 Markdown 病歷；root 在本機重新核對 Markdown 後改寫相對日摘要，再供擴充研究角色使用。這是來源與操作邊界的修正，不掩蓋第一輪違規。

## 保留OPEN的臨床事項

- Lugol配方濃度、完整最後用藥時間，以及所有iodine exposure。
- Allopurinol／其他藥物實際暴露；住院lithium MAR與採血時間。
- 最新renal function／Na／volume status；Cardiology與Anesthesia風險評估。
- Pneumonia的當前臨床／影像恢復程度。
- Thyroid nodule原始影像、LN與必要細胞學，病因確立度。
- Nakamura原文數字不一致是否另有正式erratum。

研究整理可以完成；這些臨床資料缺口不能由session投票關閉。個別訊息沒有獲得回覆的部分亦保留在原始對話中，不宣稱所有議題有全員一致同意。

## 最後書目更正（Root承擔錯誤）

Director第一輪曾要求將Vicente2017 ref32改成1989，該要求本身錯誤。Endocrinology與Methods堅持原PDF觀察，root最終對`literature/vicente2017.pdf`第6頁render確認ref32為Meyer-Gessner1994、DOI10.1007/BF03344959。因此不把多agent或root指令當作科學事實；1989的5/33直接證據保留，1994全文引用鏈仍OPEN。歷史訊息的錯誤判斷由此明確supersede，經局部遮蔽的 repo 引文不應誤認為原始逐字稿；角色成稿修正錯誤書目，沒有假造作者同意。

## 最後執行與來源定位

四個專科各兩輪、Director兩次，共10次invocations皆回傳success，對應5個獨立Claude UUID。共57次native SendMessage呼叫，49次回報排隊成功、8次失敗，57次均有transport結果；排隊不代表對方同意，對話檔中的實際回覆才構成往返。最終角色成稿另經root原PDF更正，並未冒稱專家對root編輯內容重新表決。

ATA 2016 [E6] contraindication及thyroid storm短期PTU例外，root已核对[原始PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)：印刷p.1357／PDF第15頁、Recommendation17之後、18之前。早期memo的p.1358 locator有誤；E7 minor-rash討論才位於p.1358。此來源定位缺口已關閉，病人是否符合危急例外並未因此獲確認。
