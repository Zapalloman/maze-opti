---
phase: 2
plan: 1
wave: 1
---

# Plan 2.1: 1D BFS Algorithm

## Objective
Implement an intensely optimized graph search replacing the matrix traversal in the default solver. It will search directly on the 1D representation of the ASCII buffer using Python `str.find` and `collections.deque`, achieving massive computing gains.

## Context
- `.gsd/SPEC.md`
- `fast_solver.py`
- `maze_api/solver.py` (specifically `_normalize_lines` shapes)

## Tasks

<task type="auto">
  <name>1D BFS Initialization</name>
  <files>fast_solver.py</files>
  <action>
    - Within `fast_solver.py` inside `solve()`, analyze the incoming `ascii_maze` string directly.
    - Calculate `line_width` (including newline character).
    - Find the start point `P` using `ascii_maze.find('P')`. If `start_index == -1`, find `S` instead.
    - Check for goal `X`.
    - Establish `collections.deque` and a linear array or simply `visited = set()` storing indices. Do not parse the string into a nested list or objects.
    - Use `time.perf_counter()` to accurately measure execution time independent of file-read/HTTP time.
  </action>
  <verify>python3 -c "import fast_solver; assert 'collections.deque' in open('fast_solver.py').read()"</verify>
  <done>Algorithm loop replaces dummy handler, implementing native 1D structural loops tracking offsets like `index - 2 * width` for UP/NORTH.</done>
</task>

<task type="auto">
  <name>1D Traversal & Offset Mapping</name>
  <files>fast_solver.py</files>
  <action>
    - Ensure offsets align with the 1D ASCII layout for `N`, `S`, `E`, `W`. In `maze_api`, cells are surrounded by walls. Vertically they are spaced 2 lines apart, horizontally 4 columns apart.
    - Before stepping to an offset index, simply check the ASCII char exactly in between `current_index` and `offset_index` in the 1D string to verify if it is an open path ` ` or a wall `-` / `|`. 
    - Trace the path backwards upon reaching the boundary or `X` and return the `moves` array. Record purely the algorithm compute time separately from I/O if necessary.
  </action>
  <verify>python3 fast_solver.py --size 5 --seed 42</verify>
  <done>Solver successfully solves local procedural mazes using 1D strings accurately outputting move length.</done>
</task>

## Success Criteria
- [ ] `./fast_solver.py --size 8 --seed 123` returns correct sequence without crashing.
- [ ] 1D text offsets perfectly handle 'N', 'S', 'E', 'W' discovery without allocating arrays or splitting lines.
