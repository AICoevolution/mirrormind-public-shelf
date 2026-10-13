# Phase 3 partial audit — NOT FROZEN

Status: INCOMPLETE_PHASE3. Astra owns all remaining audit, correction, validation and delivery work. No human answer is required to continue. No source or candidate bytes have been changed. No later-phase request, job history, provider observations outside the allowlist, or repair narrative has been opened.

Phase 1 and Phase 2 are frozen in their existing files. Current authorization matches the handoff; all three phase allowlist hash records match their live inputs.

Completed progress:
- Read complete candidate CORE across all 25 bars and compared its pitches/rhythms against the two-page print and the independent working transcription.
- Loaded the exact XML, event/mark ledgers, structural/duration reports, coverage, uncertainty report, ensemble manifest, provenance and disagreement data, and all four candidate packets under the Phase 3 allowlist.
- Candidate has 408 note elements (372 pitched, 36 rests), ten fragmented source voice labels, six encoded tie pairs and no beams or expressive marks. The correct repeat route is preserved; a passing duration report does not validate notes or voice identity.
- Confirmed every packet reader claim matches the current reader_claims record for pitch, onset, duration, staff, physical bar and tie fields. Candidate packet and candidate freeze hashes match the handoff.
- Saved partial event discrepancies in phase3_review.json. These include a systematic comparison to the working pitch inventory plus directly focused notation and cross-staff findings. The list is partial and must not be applied wholesale.
- Inspected enlarged P003/P007 grace details, P011/P015/P017 cross-staff contexts, P024 polyphony, P009 repeat capacity and P025 final capacity. Saved refinements in phase3_transcription_recheck.md.

Remaining Astra-owned work before any Phase 3 freeze:
1. Complete the event-by-event audit, including every chord member and all missing/extra events, and resolve the working transcription refinements. Use the original pixels rather than treating the working inventory as authority.
2. Audit every resolved and unresolved ensemble disagreement and reconcile provenance records with exact XML members; repeated provenance event IDs can reflect field-level records and are not by themselves a blocker.
3. Finish explicit stem/beam/grace/tie/slur endpoint, wedge, text, fermata and route coverage. Trace all continuous lines and specify a minimal topology. P011/P015 have independent sustained and ascending same-pitch lines; P017 crosses staves and has another simultaneous upper eighth. A blanket global voice merge is unsafe.
4. Freeze supported corrections and separately label any provisional choices. Carry ordinary unresolved musical questions to human_attention.json with evidence and provisional treatment, not to a repairer or an immediate human gate.
5. Only then create PHASE3_FREEZE.md and open /job/request.json. Apply corrections in this review workspace, regenerate layers, run all real consumer checks, render and recheck all changed contexts, then package the delivery and its hash closure.

No Phase 3 freeze, Stage 4 completion, Stage 5 completion, corrected primary XML or delivery readiness is claimed. The candidate remains the immutable source_agent/UNVERIFIED_source.musicxml.
