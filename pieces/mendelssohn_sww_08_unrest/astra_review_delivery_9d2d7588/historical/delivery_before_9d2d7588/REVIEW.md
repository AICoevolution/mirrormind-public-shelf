# Unrest — UNVERIFIED corrected review

The 109-region independent audit is complete and corrections have been applied. The primary passes PROPER, MusicXML 4.0 validation, independent playback (1,793 attacks) and production viewer identity/mapping (1,760 graphical note/rest members in each of two layouts).

Stage 5 cannot be declared complete: the runtime lacks `domains.music.omr.sfc.attention_policy`, required for canonical attention-index creation and validation. The draft index and authoritative questions are prepared. This is the only execution dependency remaining; no additional musical audit or primary change is requested. See validation/attention_index_dependency.json.

Human verification remains mandatory; nothing is published or stamped. The following unresolved decisions are preserved:

- **MUS-P006-042-077** — P006/P042/P077 upper inner F4 at q0 and q3/4: Is the same-pitch curve a phrase with reattack, or a tie across the intervening accompaniment? Retained: Retain phrase/slur and both attacks; do not invent a sustained tie.

- **MUS-P049** — P049 lower staff, independent inner Bb3 line: Confirm lower voice timing: two 32nds after q1/2, then three 16ths from q3/4, versus an earlier/different subdivision. Retained: Eb3 dotted quarter; D4/Eb4 dotted eighths at q0/q3/4; Bb3 at q1/2,q5/8 as 32nds and q3/4,q1,q5/4 as 16ths. No inferred tuplets.

- **MUS-P093** — P093 lower staff chord members, q1/4 through q5/4: Confirm all lower chord members against the dense print, especially the final F3/A3/C4 then A3/C4/Eb4 chords. Retained: Retain G3/Bb3/C4 at q1/4,q1/2; F3 at q3/4; F3/A3/C4 at q1; A3/C4/Eb4 at q5/4. Separate dotted-eighth C3 and F3 bass line preserved.

- **MUS-P052** — P052 lower F3 at q0, printed 4/5 and curved 1: Confirm whether curved 1 is a transfer/substitution for the held F3 or belongs to a neighboring line. Retained: Preserve 4, alternate 5, and provisional alternate 1 on F3; no new sounding attack. Production digits are stacked and do not reproduce the curved guide.

- **VIEW-P050-053** — P050 upper Gb4 q0 to lower Eb4 q3/4; P053 lower C4 q1/2 to upper F4 q3/4: Choose a faithful visible representation of the diagonal hand-change guides, and verify the continuing inner line across the system break. Retained: Voice 3 and exact note timings/staff changes retained; guide endpoints preserved in MusicXML miscellaneous fields. No invented glissando. Diagonal guides are not painted in the viewer; bound source remains necessary.

- **VIEW-P040-DIM** — P040 upper staff q1, dim., layouts 1350/1 and 900/1: Confirm upper-staff ownership and adjust the low dim. word placement before publication. Retained: Retain upper-staff below placement; word is visible between staves but fails the shared geometric lane criterion.

- **VIEW-P082-DASHES** — P082-P084 upper staff ritard. e cresc. and dashes: Separate continuation dashes from the word baseline and verify the mark is unambiguous. Retained: Words and dashes remain at their exact source onsets/endpoints. In both layouts the dashed continuation crosses the readable text at P082.

- **VIEW-P052-FINGERING** — P052 lower staff F3 at q0: After resolving MUS-P052, choose readable transfer-fingering placement and curved-guide representation. Retained: Retain the exact technical/fingering values and alternate flags. Production stacks 1/5/4 and omits the source curved association.

- **SEP-MARKS-NORMALIZATION** — MARKS Apply, 287 anchored note payloads: Validate MARKS no-op normalization before using its output as a publication revision. Retained: Primary remains unchanged. Applied copy reorders children, renumbers slurs and adds empty notations; exact slur endpoint/styles and articulation placement remain equal. Fingering/arpeggio payloads remain after normalization.

The complete frozen specification and per-reader/provenance/quality review remain under reviewer/. Historical partial files are unchanged; PHASE3_FREEZE.md identifies the completed additive evidence. Source candidate and frozen inputs were never edited. Corrections and serialization repairs are in correction_ledger.json.

CORE rebuild preserves musical projection; correct CORE Apply including Pickup is byte exact. The legacy diagnostic helper dropped Pickup and is retained as a diagnostic failure only. MARKS Apply has explicit normalization differences; ROUTE Apply preserves all anchored note payloads. The primary is the notation authority. Blank candidate metadata is not hand patched: delivery_final/namecard.json supplies printed title and rights with absent creator fields empty for the pipeline exporter.
