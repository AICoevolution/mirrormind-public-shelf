# Stage 5 recheck — UNVERIFIED delivery

The exact corrected primary MusicXML and completed Phase 1–3 review are preserved from astra_review_fresh_df17c73a88804a929458568b685d4fe2. This job independently reran consumer validation; it did not repeat or change the musical review. All required delivery gates pass.

**Final human questions: HELD-INNER and HAIRPINS remain unresolved.** See [human attention](human_attention.json) for the exact addresses, retained provisional readings, and print evidence. No human approval or musical resolution is inferred.

The production renderer now displays the hollow D3 half-note heads at P014 and P022 separately from the simultaneous filled heads. The P022 G2 head remains in place. See [P013–014](stage5/render_p13_14.png), [P022](stage5/render_p22.png), and the [complete render](stage5/production_render/full_score.png). All 22 bars and connected spans were visually rechecked against the preserved print evidence.

Fresh checks pass PROPER; all 482 playback attacks, durations, voices and source times against the independent 44-bar repeat schedule; mapping of all 482 attacks; all 274 VexFlow durations; and all 44 cross-staff beam groups / 132 stem intersections. CORE export/rebuild preserves sounding events and ties, and actual unchanged CORE Apply is byte-exact. MARKS preserves exact chord-member/slur endpoints and placement, and ROUTE preserves events.

CORE from-scratch rebuild changes staff/voice packaging and does not preserve MARKS/engraving. It is a diagnostic artifact, not a replacement primary or a general lossless-edit guarantee. Cross-beat tuplets remain in the unchanged primary XML. Five SEP staff/voice lanes represent four justified continuous musical lines, including the cross-staff arpeggio.

The former failed reports under historical/ and reviewer/stage5_blockers.json are retained historical evidence, superseded for this delivery by [recheck resolution](reviewer/stage5_recheck_resolution.json). The delivered score remains UNVERIFIED pending human listening and visual verification; nothing was published.
