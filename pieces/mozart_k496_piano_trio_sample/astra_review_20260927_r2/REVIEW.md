# Mozart K.496 review

Print review and correction are complete. Delivery is **BLOCKED_TECHNICAL**: the installed notation renderer does not faithfully display several required details. Stage 4 is complete; Stage 5 readiness is incomplete. The primary remains UNVERIFIED pending Juan.

Primary: `delivery_final/UNVERIFIED_mozart_k496_piano_trio_sample.musicxml`

SHA-256: `7260d5c2e3c685a8dd40378536edb63ea40c8e6e63ba4c8c06940b767527a5ff`

All 194 bars, 39 systems and four staves were reviewed. The frozen correction history contains 6,136 issue records; the corrected XML contains 4,639 note/rest elements. Five continuous musical lines use six staff/voice lanes, including one intermittent piano inner/pedal line. No unexplained auxiliary or all-rest lane remains. Phases 1-3, numbered errata and exact correspondence are retained under reviewer/. Authorized source inputs are copied under frozen_inputs/.

PROPER, exact event and member-level mark comparisons, CORE rebuild and actual Apply, ROUTE Apply, independent repeat/playback comparison, production bar mapping and VexFlow durations/cursor all pass. Playback expands to 388 bars and 8,020 attacks. Tempo 80 is the consumer default, not a printed metronome marking. MARKS is PARTIAL because turns, sfp and ornament accidentals exceed its token vocabulary; primary XML preserves them. A MARKS Apply preserves the exact existing slur notehead endpoints and placement, but that does not make its standalone text a lossless representation of all notation.

The full visual recheck is complete, with the following delivery blockers:

- Bar 1: piano Allegro appears above violin; lower-piano legato is inside the staff.
- Bar 22: lower-piano legato overlaps the staff/notation.
- Bars 111-113: bass clef at bar 111 q1.5 is displayed late in bar 113, causing excessive ledger lines.
- Bars 1 and 18: printed parentheses around f are not shown.

See technical_reports/final_xml/focused_visual_recheck.json and viewport_system_*.png for evidence. Tall full-page screenshot capture is unreliable near its bottom; individually captured viewport evidence confirms the ending. No production code was changed to force a pass.

Juan's remaining print questions are bar 33 piano RH (small arc endpoint), bar 47 violin (long arc start), bar 65 piano LH (damaged glyph), bar 102 piano RH (ascending arc start), and bar 193 cello (speck beside quarter F-sharp). Frozen working readings remain explicit; none is converted into certainty by arithmetic.

This freeze is not READY_FOR_HUMAN and nothing was published. Consumer repair must be followed by a new immutable Stage 5 recheck workspace with unchanged primary XML and review hashes, as required by the staged prompt.
