# Phase 2 reader-evidence freeze

Status: READER_REVIEW_FROZEN. No assembled candidate, ensemble ledger, source-agent output, or independent source-model content has been opened. Phase 1 was frozen before any reader content access. Phase 2 allowlist hashes all match.

## Correspondence: every physical region

phase2_correspondence.json records all 57 regions, systems, reader part/ordinal/raw-label addresses, and actual print evidence. SmartScore has TWO parts of 57 elements each; its 114 rows must not be read as 114 bars. P1 is RH and P2 is LH; normalized staff fields reflect this. PlayScore has one two-staff part of 57 elements. Their physical correspondence is ordinal=physical bar, confirmed against actual local rhythm/contour/clef/route anchors across all twelve systems, not accepted merely from labels.

Audiveris ordinals1-32 correspond to physical P001-P032; it omits P033 entirely. Ordinals33-56 correspond to P034-P057. Raw labels start at0, duplicate17 for physical P018 and P019, skip31, and end55. P033 omission is proven by the transition from P032 LH B2/A2 offbeats to ordinal33 LH dotted-quarter A2 with RH tenuto D4/F#4 and stepwise chords (physical P034); the intervening printed G#2/B2 LH and sixteenth-figure RH region is absent. From there each region's local contour was reidentified through the terminal fermatas, including the true P052 bass-to-treble bar at ordinal51/raw50. This is an omission, not an absent printed bar or a global clef transposition.

All 36 priority questions are answered individually in phase2_priority_answers.json. Most are contaminated by raw-label comparison. The one CONTENT question at P013 onset2 confuses a sustained C#5/E5 quarter chord with the D5/F#5 attack actually at2.5, due to SmartScore's false tuplets and Audiveris label displacement. A unanimous-looking question premise is not accepted.

## Deterministic controls

question_packets/controls.json is empty: no controls can be claimed from it. All three parent controls fail direct print review, including the one still marked pass. control-1: P001 opening D4 duration1/4, then D3 duration1/4; it is not one eighth D4. control-2: P010 first attack is B4/D5 sixteenth chord, then D4 sixteenth; D5 duration1/4, not1/2. control-3: P057 upper chord F#4/A4 dotted quarter, duration3/2, not F4 dotted half duration3. Preserve both withdrawn controls and the newly failed control-2 as useful negative evidence. No control implies whole-score correctness.

## Reader omissions, disagreements, and shared blind spots

All reader-only system packets were inspected; their claims arrays are empty, so they do not supply local event evidence. The full reader_claims.json is the usable per-element evidence source. The supplied correspondence left Audiveris unmapped; the reviewer map above resolves it without changing the prepared files. Baseline duration assertions use raw labels/full-meter assumptions and are not independent proof against legitimate pickup/partial regions. The baseline base selection PlayScore is not a musical authority.

CORE risks observed while establishing correspondence: SmartScore adds D5 in P002, invents tuplets in P011/P013, misses the P014 LH clef, misreads P050 F#2 as F2, and serializes overlapping P051 LH notes into six quarter units. PlayScore shortens the first P011 LH chord, flattens the tied G# at P016, and has duplicated P053 bass notes. Audiveris has missed effective clefs, added notes, wrong durations and the P033 omission. All readers require print-led tie accidental handling at P014-P016, and real voice separation at P017 and P041-P056. The absence of a disagreement is not evidence of correctness.

MARKS were compared with the Phase 1 table over every region: SmartScore often substitutes ties for slurs with intervening different pitches (P001, P019, P024-P025, P035-P036, P037) and truncates cross-system slurs (P005-P006, P027-P028, P047-P048). It duplicates articulations across chord notes, omits many dynamics and both text instructions, and has false tuplets/fingering-derived text. PlayScore retains many slur shapes but represents several real lower-note ties as slurs in P014-P017; its RH strong accents are missing at P004/P011/P014/P015/P018, P003 mf is missing, P021 mp becomes p, tempo/metronome and the complete P024/P037 text are absent. Its diminuendo at P034 immediately starts and stops; other hairpin endpoints leave the printed regions. Audiveris adds an opening staccato, splits pp into p events, mangles tempo/text, omits ff, invents dynamics at P028/P037, substitutes breath marks at P018/P051/P056, and breaks or reclassifies long bass ties and closing RH ties. Fermatas and terminal-rest attachment must be retained from the print even when the reader's associated pitch or duration is wrong.

Shared blind spots: complete tempo/metronome text; P024 poco a poco piu p; P037 dim. sempre; accurate hairpin endpoints; RH strong accent at P015@0; P018 RH strong accent; LH short tie P029@1->1.5; lower RH tie P055@2.5->P056@0. These require direct print corrections if the candidate omits them. The small P018 staccatissimo is supported by PlayScore and the print, but remains medium-confidence scan detail until focused recheck. Faint P004 residual ink must not become a spurious slur/dynamic.

ROUTE: all three reader event streams, once mapped by physical ordinal, contain backward after P009, forward before P010, backward after P018, and final double after P057. No reader route element authorizes skipping physical P033. No endings/navigation signs are printed. Reader agreement here was independently checked against both-staff barline pixels in S2/S3/S4/S12.

## Coverage and next phase

57 physical regions, 12 systems, 3 readers; SmartScore 114 part-measure rows, PlayScore57, Audiveris56 inspected. Every priority answered; three parent controls failed; no Phase 3 evidence yet accessed. Print ambiguities A1-A3 remain. Nothing in this freeze certifies the candidate. The full candidate audit must inspect every pitch/duration/voice/mark/route event, including reader-unanimous claims and locations not in any disagreement list.
