# Review stopped — Phase 2 integrity conflict

Phase 1 print-only inventory is frozen. Phase 2 is incomplete and NOT frozen as a successful checkpoint. Phase 3 and Stage 5 were not entered. No candidate, ensemble provenance, disagreements, or source XML was inspected; no corrected delivery is claimed.

The authorization is valid and every top-level Phase 1/2 handoff allowlist hash matches. However, the allowlisted question_packets/freeze.json binds audit_config.json to SHA-256:

3160f8a6ae6ff27cbf1c8285b05370932d94b8e34765754ca09b07167fc1afec

The current audit_config.json and both handoff allowlists bind it to:

8a63c5668701c36380dabb26a9f8741281ec8c9e49ac752567e2c23ded0314d3

This is a stale or inconsistent frozen dependency. The explicit instruction to stop if a hash is wrong applies; matching the outer handoff does not repair the contradictory inner freeze. No attempt was made to infer which historical configuration was intended. Further phase-evidence inspection stopped on discovery.

## Work preserved

- PHASE1_FREEZE.md: full-page structure, capacity, MARKS, ROUTE inventory, with seven derived print system PNGs.
- phase1_hashes.json: launch-gate and eight source hashes plus Phase 1 artifact hashes.
- phase2_hashes.json: all 24 allowlisted Phase 2 source hashes, checked before semantic review; matching these is not a completion certificate.
- phase2_blockers.json: exact conflicting hashes and required repair.

## Preliminary Phase 2 observations — not a completed review

Reader correspondence is explicitly unmapped for all three readers and all 33 physical regions. The first reader-only packet contains empty per-reader claim arrays. Count equality alone is not correspondence; no mapping has been certified here. Deterministic priority questions include raw-label comparisons between zero-based Audiveris labels and one-based labels; they require correspondence before acceptance. The parent controls are assertions, not trusted passes. These observations were obtained before the integrity conflict was found; full control assessment and priority resolution remain undone.

## Attention required

1. Reconcile the frozen audit_config dependency (INTEGRITY-1). Only the authorized preparer/human may repair the prepared package; Astra has left it untouched. A changed handoff requires renewed matching authorization before resumed evidence access.
2. Preserve the print-grounded P010 finding: page 2/system 3/both staves use dotted sixteenth + thirty-second, not two equal sixteenths. Capacity remains one eighth. It is not yet compared to the candidate.

No musical corrections, voice topology, final XML, layer exports, consumer checks, rendering of corrected XML, or final delivery freeze exist. Juan's review and publication remain pending. Do not treat this workspace as a finished score.