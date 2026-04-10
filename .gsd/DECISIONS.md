# ADR Log

## Phase 1 Decisions

**Date:** 2026-04-09

### Scope
- Output Behavior: "Maybe both" — the solver will print the final standard output trace (matching the baseline solver text) AND support POSTing the calculated move sequence back through the API if run against the server.
- CLI Compatibility: "Yes" — the new CLI will strictly mimic the same arguments (`--file`, `--stdin`, `--size`, `--seed`) as `maze_api.solver` for a perfect drop-in replacement.

### Approach
- Selected: Raw `http.client` connection (or lightweight socket wrapped connection).
- Reason: Designed to pursue the lowest possible latency standard-Python approach over `localhost`, bypassing heavy wrapper code.

### Constraints
- Fast endpoint parsing required: The algorithm must rapidly isolate raw maze strings and discard HTTP header padding.
