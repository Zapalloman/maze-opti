# ROADMAP.md

> **Current Phase**: 3
> **Milestone**: v1.0

## Must-Haves (from SPEC)
- [ ] Ultra-fast maze text parser to 1D mapping structure.
- [x] Specialized Python standard library BFS algorithm (non-object oriented).
- [x] Direct integration block bridging the solver and `maze_api` over HTTP.

## Phases

### Phase 1: High-Speed CLI and HTTP Pipeline
**Status**: ✅ Complete
**Objective**: Build out the thin interface layer. A rapid HTTP fetch logic for `/ascii` from the API, and simple CLI mapping to load mazes locally or remotely.
**Requirements**: REQ-01, REQ-04

### Phase 2: Core Algorithm Optimization (1D BFS)
**Status**: ✅ Complete
**Objective**: Skip matrix conversion completely. Load the ASCII text directly into a 1D list and calculate neighbor widths, deploying a tightly grouped `deque` search that traces from 'P' to 'X' at blazing speeds.
**Requirements**: REQ-02, REQ-03

### Phase 3: Benchmarking and Polish
**Status**: ⬜ Not Started
**Objective**: Run the implementation iteratively against `maze_api.solver`, comparing metrics like parse latency and runtime complexity to ensure standard benchmarks are overwhelmingly beaten.
**Requirements**: REQ-03
