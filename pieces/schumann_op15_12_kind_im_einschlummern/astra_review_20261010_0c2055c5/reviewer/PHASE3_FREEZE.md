# Phase 3 freeze — Astra

Full print-grounded candidate audit completed across 32 physical bars, both staves, 5 systems, 2 pages. 493 source note/rest members covered individually in event_coverage.json. All 206 ensemble disagreement entries rechecked, including resolved and blocking flags, against the print specification. Source uncertainties remain historical claims, not votes. No candidate modifications or later-phase request access before this freeze.

All phase-3 allowlist hashes match. Source candidate's per-region arithmetic is not a musical certificate: it contains wrong pitches/octaves, false chord members, missing sustained notes, false tuplets at P022/P024, rhythmic errors, empty rest fragments, inconsistent voices, missing beams, and absent expressive marks. Candidate MusicXML and exact ledgers were read alongside CORE/MARKS/ROUTE and all system packet claims. Physical frame and linear route agree with print; no meter change, repeat or extra bar is authorized.

The exact correction specification is phase3_correction_spec.json: 394 grouped printed events, 467 note/rest members, 46 slurs, dynamics, accents, two staff fermatas, six diminuendi, and ritardando text. Each staff/bar before and after is in phase3_review.json; this explicitly authorizes context-scoped replacement, including corrections to stems, beams and tie member topology. Every source event is represented in the coverage table, even when pitch/duration already agree. No unprinted grace notes or tuplets remain. No cross-staff beam is printed.

Five continuous lane identities suffice: upper melody, upper sustained/inner harmony, additional independent upper moving line, lower moving line, lower bass harmony. The third upper line is required at overlapping contexts P009/P013 q1 and P017/P019/P020, not a restarted OMR label. Combine common-stem chords where printed; ties can bridge lane labels at those joins. Do not globally merge candidate voice numbers whose musical function changes. Empty lane intervals are silence via forward positioning, not added visible rests. Shared noteheads with two distinct printed stems remain two notated events where their durations differ.

Provisional decisions are explicitly frozen in ../human_attention.json. Enlarged Phase 3 readings supersede preliminary Phase 2 note guesses at P011/P012/P015/P016 and P018; the earlier freeze remains unchanged. The ambiguous lower slur endpoints and tiny dots are isolated notation questions and do not block unrelated corrections. All provisional changes must be labeled as such, not confirmed corrections.

Historical ensemble reader hash and raw-label questions do not match the migrated metadata; current handoff records the migration and controls access. Preserve that provenance limitation. Missing/misleading source support does not override independent print.

Phase 3 is frozen; Stage 4 audit complete. Stage 5 and delivery readiness are not yet established.
