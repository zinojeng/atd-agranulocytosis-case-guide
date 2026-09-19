# Independent bridge／RAI／surgery review

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

查核日期：2026-09-19。審查者：independent bridge auditor。

審查版本：`reports/clinical_synthesis_zh_TW.md`，SHA-256 `cb2e9b4a843ecdf993288b1d06912dff36fdabc96129435f2ec4061026dc566b`。本次唯讀審查報告，未修改報告；個案資訊僅讀 `research/case_synopsis.md`，未讀 `private/` 原始病歷。

## 結論

**在 bridge／RAI／thyroidectomy 的受託範圍內，未發現需要阻擋整合或必須修正的實質醫療錯誤。** 關鍵限制均已保留，沒有把 case reports 升級成通用處方，也沒有將 Lugol 暴露誤寫為永久 RAI 禁忌。這個判定不是對實際治療適切性的簽核；目前資料仍不足以決定個案 definitive treatment 或日期。

## 已逐項確認

| 項目 | 審查結果 | 報告定位／依據 |
|---|---|---|
| Lugol 與 RAI | 正確說明 Lugol/KI 可先做 bridge，再停碘評估 RAI；並非永久排除 RAI。 | 報告 lines 9、50、71–75；[EANM 2023](https://doi.org/10.1007/s00259-023-06274-5) Table 1及preparation section。 |
| Contrast／AKI clearance | 2–3週 Lugol/SSKI、6–8週 water-soluble IV contrast 與後者 normal renal function 前提均正確。已有要求綜合 iodine exposures、RAIU、必要時尿碘，未用日曆直接宣告安全。 | 報告 line73；本機 `literature/eanm2023.md` lines104、112–113、124、256。 |
| 本案腎功能 | 摘要記初期Cr1.53、之後0.59；報告用「recent／曾AKI」，沒有捏造 persistent renal failure。最終RAI或lithium計畫仍應看最新趨勢。 | 報告 lines9、53、73、95；case synopsis。 |
| Lithium 效果與 level | 已區分Day57門診起用與先前住院不確定給藥；沒有把整條FT4下降歸功lithium，亦未把一次<0.2當作追求psychiatric range的依據。 | 報告 lines38、53、95；case synopsis。 |
| HFrEF 與beta-blocker | 有區分stable狀態與low-output／shock，沒有僅因tachycardia建議高劑量propranolol。 | 報告 line52；[JTA/JES2016 Recommendation8](https://doi.org/10.1507/endocrj.EJ16-0336)。 |
| 手術優先評估 | 使用條件式語言；未把EF32%、雙側hypoechoic nodules或既往ANC50當成立即手術單一指標。 | 報告 lines77–87；[ATA2016 Recommendation26](https://doi.org/10.1089/thy.2016.0229)。 |
| 感染與ANC | 明確指出ANC recovery不等於pneumonia clearance，保留cardiopulmonary／infection／anesthesia評估。 | 報告 timeline Day57、lines84–87、98；case synopsis。 |
| Case系列的受限推論 | Knight未完全euthyroid手術不被泛化；Calissendorff的Lugol3天未誤寫washout3天；Rami case2未混入case1 heart failure。 | 報告 lines63–66；[Knight2017](https://doi.org/10.1530/EDM-17-0071)、[Calissendorff2017](https://doi.org/10.1530/EC-17-0025)、[Rami2024](https://doi.org/10.1186/s13256-024-04480-9)。 |
| RAI案例的證據等級 | Sazon標記conference abstract；Tamura160/185未誤稱agranulocytosis subgroup成功率；2026 neutropenia abstract未列作agranulocytosis成功病例。 | 報告 lines65、67、69；[Sazon2024](https://doi.org/10.1210/jendso/bvae163.2078)、[Tamura2024](https://doi.org/10.1007/s00259-023-06523-7)、[Fahmi2026](https://doi.org/10.1093/ejendo/lvag096.1837)。 |

## 實質修正清單

無。

## 後續編輯需維持的界線

- 不要把「曾AKI、需查最新腎功能」升級成「目前仍AKI」；反之，單次Cr改善亦不等於已證實iodine pool完全清除。
- 不要把核醫的個別RAIU判斷替換成固定等待天數；EANM對contrast exposure情境明確要求RAIU，尿碘是補充而非替代。本稿現有寫法可接受。
- 不要把「surgery值得優先評估」改成「一定首選／立即手術」，除非後續補足感染恢復、anesthesia、nodule與病人偏好資料。
- 不要從FT4下降推論確定thyrotoxicosis已完全解決；仍需reference interval、FT3、clinical status及當時用藥。報告目前已要求補最新資料。

範圍限制：本次不重新裁決cross-reaction歷史分母與Nakamura時間分析；該部分由另一份independent cross-reaction audit負責。Case數值僅比對假名化摘要，無法代替原始MAR、影像或檢驗時間戳查核。部分case fulltext由先前publisher／PubMed查核提供，尚未就pipeline未完成的每份LlamaParse產物逐字核對。
