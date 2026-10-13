# Schumann, Op. 15 No. 12 — Astra review

Corrected UNVERIFIED MusicXML: [primary score](delivery_final/UNVERIFIED_Schumann_Op15_12_Kind_im_Einschlummern_Astra_import.musicxml). Full independent review covers 32 printed bars on two pages. Technical delivery checks pass; Juan's musical verification remains outstanding.

Four unresolved print questions require attention; see [human_attention.json](human_attention.json):
- P011/P015 upper dyad and P012/P016 moving peak: provisional D#4 ledger-line readings.
- P018 upper sustained half note and independent quarter: provisional E4 and B3.
- P021–022 and P023–024 below-staff slurs: exact endpoint attachment remains provisional.
- Tiny lower-staff dots near P010/P018: retained as print damage/uncertain, without added staccato.

The print-grounded audit restored missing expressive marks, corrected pitches and rhythm, removed false tuplets and duplicate/phantom material, repaired beams and ties, and consolidated ten source labels into five musically justified lanes. Every source member has review coverage; every applied bar replacement includes exact before/after XML in [change_ledger.json](change_ledger.json). Provisional treatments are distinguished from confirmed corrections in the frozen findings. [ERRATUM_001](reviewer/ERRATUM_001.json) repairs A3 voice continuity at P017–018 and concurrent slur identifiers; its first failed checks remain preserved.

Validation: 467 final note/rest members; all 444 sounding attacks match an independent exact schedule, including tie durations. PROPER passes for all 32 complete 2/4 bars. CORE export/rebuild/actual Apply and MARKS export/actual Apply pass, including member ties and exact slur endpoint/placement comparison. ROUTE remains straight through P001–032 and round-trips without changing notes. Production ScoreViewer maps all 444 attacks, all 467 VexFlow durations match, and every bar is exactly two quarters. Final [render](viewer/full_score.png) and [focused visual check](validation/focused_visual_recheck.json) cover all changed contexts and connected spans.

System wrapping, measure labels, and a renderer meter reprint differ from the scan. The MusicXML meter remains 2/4 with one opening declaration. Playback uses the application's neutral 80 BPM timebase; ritardando words are retained as printed, not converted into an invented tempo curve.

All Phase 1–3 freezes and authorized source inputs are preserved. Nothing was published or promoted to human-verified status.
