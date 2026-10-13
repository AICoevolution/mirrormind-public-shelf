# Astra final delivery — UNVERIFIED

The corrected primary is [UNVERIFIED_Schumann_Op68_25_Echoes_from_the_Theatre_Astra_import.musicxml](UNVERIFIED_Schumann_Op68_25_Echoes_from_the_Theatre_Astra_import.musicxml). SHA-256 `8a8bdcb0b30f01372dea70f2ecd08042d996cd31edd305906bb4b87155485912`.

The three independent review phases are frozen, all 33 physical regions on two pages/seven systems were reviewed, and all 564 source note/rest elements were checked. The final XML contains 557 elements: 553 pitched elements and four printed rests. It preserves the printed 2/4 meter, quarter=96, and the four partial-region capacities. Three musical lines occupy four justified staff/voice lanes; no unexplained empty lane or fragment remains.

Corrections restore sounding pitches, accidental glyphs, durations, beams, stems, chord membership, all expressive marks and phrase/tie spans. There are 1,177 frozen review records, plus two frozen placement/identifier errata. Exact before/after values and source review links are in correction_history.json. The seven deleted source elements and every final element are reconciled in the application check.

| Delivery layer/check | Outcome |
|---|---|
| Primary MusicXML | Ready for Juan's verification; remains UNVERIFIED |
| Structural and duration | PASS: no overflow, overlap or cursor slip; printed partials retained |
| Independent playback vs ScoreAnalyzer | PASS: all 1,094 attacks, six tie chains each repeat, all 66 region visits; quarter=96 |
| Installed viewer mapping | PASS: 1094 / 1094 notes mapped |
| VexFlow duration | PASS: 553 checked, zero mismatches |
| Complete cursor onset checks | PASS: 176 buckets, zero mismatches |
| CORE | Four correct lanes; actual unchanged Apply is byte-exact. Standalone rebuild is **not ready**: shifts P001/P010 pickups |
| MARKS | Exported; **Apply not ready**: cross-voice slur mispairing at P018/P020/P022 |
| ROUTE | PASS: export/Apply semantic fixpoint; P001–P009 twice, P010–P033 twice |
| Rendered evidence | Complete; known cresc. collisions at P006/P030 in installed viewer |

No lossless SEP reconstruction/application certification is issued. The failed rebuilt/applied diagnostic XMLs under checks are not delivery alternatives. These narrow representation failures do not waive any primary playback or cursor failure: those primary gates actually pass.

Juan's focused attention: **P008**, **P018–P022**, **P031**; also inspect the viewer text spacing at **P006/P030**. No damaged-print interpretation remains unresolved by Astra. Human listening, visual/structural verification and publication remain Juan's. Nothing was published.

Open [review index](review_index.html) for paired printed and corrected contexts. Full installed-viewer evidence is ../render_checks/final_05/. All source evidence used is copied under ../evidence_inputs/ with verified original hashes. Reader failures and all 118 ensemble disagreements are preserved in ../reviewer/.

The workspace's older root REVIEW.md/BLOCKED_FREEZE.json are immutable historical evidence of the earlier stale Phase2 freeze. This delivery_final/REVIEW.md and ../FINAL_FREEZE.json supersede their status without modifying them. The repaired launch authorization was verified before resumed phase evidence, and the original prepared candidate and all protected inputs remain unchanged.
