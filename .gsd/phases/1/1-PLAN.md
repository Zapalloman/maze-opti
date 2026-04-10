---
phase: 1
plan: 1
wave: 1
---

# Plan 1.1: High-Speed CLI and HTTP Pipeline

## Objective
Establish the primary executable entry (`fast_solver.py`) which acts as the drop-in substitute for standard tests. Implement ultra-low latency HTTP calls bypassing heavy requests wrappers to rapidly retrieve the `/ascii` buffer.

## Context
- `.gsd/SPEC.md`
- `.gsd/DECISIONS.md`
- `maze_api/solver.py`

## Tasks

<task type="auto">
  <name>CLI Framework</name>
  <files>fast_solver.py</files>
  <action>
    - Create `fast_solver.py` ensuring exact mirror of `argparse` signatures found in `maze_api/solver.py` (`--file`, `--stdin`, `--size`, `--seed`).
    - Add `--host` (default `127.0.0.1`) and `--port` (default 8000) for native remote solving modes.
    - Set up a dummy solver method `solve()` that just returns an empty list of moves temporarily.
    - Output formatting must exactly match the standard benchmark output text ("Source: ... Moves: ... Elapsed seconds: ...").
  </action>
  <verify>python3 fast_solver.py --help | grep -E "(--file|--size|--host)"</verify>
  <done>Script properly initializes and understands both target CLI arguments and custom network arguments.</done>
</task>

<task type="auto">
  <name>Minimal HTTP Engine</name>
  <files>fast_solver.py</files>
  <action>
    - Implement a focused `_fetch_ascii_from_server(host, port, seed)` method using standard `http.client.HTTPConnection`.
    - Retrieve the `GET /ascii` endpoint (optionally passing seed string) and slice only the UTF-8 text grid from the response body.
    - Implement `_post_moves_to_server(host, port, moves)` method that blasts a `POST /move` sequence (either one-by-one or via raw endpoint) to validate the solution against the active server instance, depending on `maze_api` capabilities. (Read the API docs: `curl -X POST .../move -d '{"direction":"E"}'` implies we can parse moves array and do successive `http.client` POST calls utilizing connection reuse).
  </action>
  <verify>python3 -c "import fast_solver; assert hasattr(fast_solver, '_fetch_ascii_from_server')"</verify>
  <done>HTTP endpoints integrated exclusively with standard library HTTP modules.</done>
</task>

## Success Criteria
- [ ] `./fast_solver.py --help` successfully executes.
- [ ] The CLI accepts both file/stdin arguments and a network `host:port` configuration.
- [ ] Network logic uses pure stdlib module.
