# Pipeline findings

The retained historical partial audit was successfully continued without rewriting any staged bytes. The canonical checkpoint and post-release handoff validations pass.

Production rendering has two blocking staff-ownership defects documented in consumer_blockers.json. Rest-lane relocation affects the alto-clef viola across single-voice measures because the part contains a brief later second voice. Below-staff text clearance can push violin-II dolce next to viola (and, in the default diagnostic layout, below cello). These are consumer findings, not permission to change printed voice or staff ownership.

Automated rendering reports pass their narrower visibility/stave-reference checks. The independent visual check correctly remains BLOCKED. A mapped rest can still be drawn in the wrong vertical lane.

MARKS v0 cannot serialize turns and detached-legato tokens. The full XML payload survives actual Apply; raw lexical differences are element order and consistent slur-number relabeling, with exact spans preserved. Do not describe this limited textual projection as lossless.

All ordinary musical uncertainty is retained for final human review. Consumer repair should preserve primary hash199f502e50174a35b276bc98e87b863944b2ee925029bf0561161842eddd880e and all released Phase1–3 evidence, then use a separate Stage5 recheck workspace.
