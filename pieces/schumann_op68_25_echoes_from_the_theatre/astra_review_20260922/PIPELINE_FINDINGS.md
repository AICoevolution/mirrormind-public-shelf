# Pipeline findings (read-only observations)

INTEGRITY-1: question_packets/freeze.json has an audit_config.json dependency hash inconsistent with the current file and handoff. Details in reviewer/phase2_blockers.json. Review stopped, not waived.

FRAME-PROSE-1: P010 rhythm is dotted sixteenth plus thirty-second on both staves; frame prose says two sixteenths. Capacity 1/2 quarter unit is still correct. This is print-grounded, not reader/model voting.

READER-MAP-1: supplied correspondence explicitly remains unmapped; first system packet exposes empty claim arrays. Subsequent review must establish musical correspondence rather than equating raw measure labels.

INFRA-1: default shell, Node REPL, and image reader failed Windows sandbox initialization (deny-read ACL helper). Narrow elevated shell reads/writes succeeded. Image review used in-memory JPEG previews of the verified PNGs; seven lossless derived PNG crops remain in the reviewer directory. No production code or frozen source files were changed.