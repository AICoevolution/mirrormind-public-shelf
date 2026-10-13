# Astra Stage 5 recheck

The repaired consumer passes all five required delivery gates against the **unchanged** UNVERIFIED primary XML. The prior independent print review, corrections, errata, and Phase 1–3 hashes are preserved. This recheck makes no new musical decisions.

Human questions remain **UNRESOLVED**: ATT-SLUR-FINAL (final chord member), ATT-HAIRPIN-ENDPOINTS (inter-note wedge anchors), and ATT-STACCATO-16 (small printed dot). See [human_attention.json](human_attention.json) for their unchanged provisional treatments and print evidence. No human answer is inferred.

[Primary MusicXML](delivery_final/UNVERIFIED_Schumann_Op15_10_Fast_zu_ernst_Astra_import.musicxml) retains SHA-256 `9d76fde77f5f113d1b2f8fa7c147aba4f6a7d546ff4f2d1412d83756ac3ac318`.

PROPER passes; all 425 independent playback attacks match in pitch, onset and duration. Production viewer mapping, VexFlow durations and cursor capacities pass at 1200px and 1500px. The repaired final slur ends 3.491px above G#4, and its two 1500px segments stay in separate systems. See [geometry](recheck/slur_geometry.json) and [focused visual check](validation/focused_visual_recheck.json). Pixel differences from the previous complete renders are confined to this slur.

The prior shared-notehead finding remains an engraving limitation: independent sustained unison voices display adjacent heads instead of one shared head. Both musical lines and their exact durations remain represented; this does not block essential notation or playback. CORE standalone rebuild still fails; exact CORE Apply with every duration directive retained passes. MARKS and ROUTE Apply preserve musical events and slur-member styles. No lossless standalone CORE claim is made.

The carried review covered 58 physical regions and six print systems; the final score has 567 note/rest members and five justified musical roles. This job owns only consumer revalidation. Historical blocker/render evidence remains in the copied workspace; current gate decisions are the evidence cited by FINAL_FREEZE.json. See [prior review](recheck/prior_REVIEW.md) and [integrity receipt](recheck/integrity.json).

Nothing has been published. The deterministic post-Astra gate decides readiness for human verification.
