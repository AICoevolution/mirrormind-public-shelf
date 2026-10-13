# Schumann Op.68 No.29 — Astra review delivery

The corrected UNVERIFIED MusicXML and complete review package are frozen. Human readiness is **BLOCKED_TECHNICAL** by one installed-viewer defect: at P091 the literal **Coda** heading is rendered as **To + coda sign**. The XML contains only the correct words, and the independent playback route is correct. Production code was not changed.

Primary: `delivery_final/UNVERIFIED_Schumann_Op68_29_Strange_Man_Astra.musicxml`  
SHA-256: `9f31620532194580033e5f5c68dcdca0adf55d1f6b76ceb7066dddef8f67f350`

All three strictly separated phases are frozen in `reviewer/revision_02/`. The previous source-frame blocker remains preserved in `reviewer/`; the repaired frame passed the new authorization/hash gate. The print comprises 107 full 2/4 regions, three pages and 15 systems. All 1,388 candidate note/rest elements, all 351 disagreements and 769 provenance entries were reviewed. The final XML has 1,332 note/rest elements and four justified musical voices. Only fingerings were omitted.

Frozen corrections restore pitches, accidentals, octaves, missing chord members, exact rhythm, voice continuity, beams/ties, 244 mark inventory records, and the second-ending route. Erratum001 explicitly places the 144 accent/strong-accent attachments above the staff after rendering exposed automatic placement errors. Every applied change has before/after values and lineage in `delivery_final/applied_changes.json`. The source and prepared candidate were not altered.

| Check | Result |
|---|---|
| Duration/PROPER | PASS; no overflow, shortage or cursor slip |
| CORE | PASS; exactly four justified lanes; rebuild sounding projection and actual Apply byte-exact |
| MARKS | PASS with sibling-articulation-order-only exception; attachment/type/placement multiplicities exact |
| ROUTE | PASS; 158 visits; actual Apply event projection and text fixpoint exact |
| Independent playback schedule | PASS; all 1,683 attacks, durations and source positions match |
| ScoreAnalyzer tempo | 126 BPM; consumer schedule uses its documented neutral 80-BPM timebase |
| Installed viewer mapping | PASS; all 302 printed onset buckets |
| VexFlow duration checks | PASS; 1157 pitched glyph timings, no mismatch |
| Essential notation/focused visual readiness | BLOCKED at P091 Coda heading substitution |

The four voices are two principal hand lines plus real sustained inner lines. P030 and P088 sound all four simultaneously. Global OMR label maps were unsafe; exact regional corrections supply the topology. Sparse sustained lines are not empty lanes. CORE's heuristic warning about these sparse lines is rebutted by the print and `voice_topology.json`.

Juan's remaining print questions are the tiny dot next to fingering3 at P102 LH q0.75 (possible staccato, left unadded) and between-attack hairpin endpoint placement. The frozen hairpin list and actual print/render images are in `focused_visual_recheck.json`; P038/P054 double wedges and P095–096 long crescendo are useful anchors for checking the convention. No damaged-print uncertainty was converted into a rhythm repair.

`evidence_inputs/` contains hash-verified phase-allowlisted source material. `render_checks/run02/` contains the final installed-viewer render, per-region crops and exact consumer observations. `application_history/` and run01 preserve pre-erratum results. `artifact_manifest.json` and `FINAL_HASHES.json` close the package with SHA-256 hashes. The final XML remains UNVERIFIED; listening, human visual/structural verification and publication remain Juan's. Nothing was published.
