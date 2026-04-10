import sys
import time
from maze_api.server import MazeGame
import maze_api.solver as standard_solver
import fast_solver

def run_benchmark():
    sizes = [10, 20, 30, 40, 50]
    num_seeds_per_size = 10
    
    total_fast_time = 0.0
    total_standard_time = 0.0
    
    print("Starting Benchmark: fast_solver vs maze_api.solver")
    print("-" * 60)
    
    for size in sizes:
        for seed in range(num_seeds_per_size):
            game = MazeGame(size=size, seed=seed)
            ascii_maze = game.ascii_maze()
            
            # --- Fast Solver ---
            t0 = time.perf_counter()
            fast_moves = fast_solver.solve(ascii_maze)
            fast_time = time.perf_counter() - t0
            
            # --- Standard Solver ---
            # solve_ascii_maze actually wraps the parsing AND solving.
            # to be fair, we will test the entire solve_ascii_maze execution.
            t1 = time.perf_counter()
            standard_result = standard_solver.solve_ascii_maze(ascii_maze)
            standard_time = time.perf_counter() - t1
            
            total_fast_time += fast_time
            total_standard_time += standard_time
            
            # Validation
            assert len(fast_moves) == len(standard_result.moves), f"Mismatch in length: Fast={len(fast_moves)}, Standard={len(standard_result.moves)}"
            assert fast_moves == standard_result.moves, "Mismatch in move sequence!"

        print(f"Size {size}x{size} verified across {num_seeds_per_size} seeds recursively.")
        
    print("-" * 60)
    print("Aggregate Statistics:")
    print(f"Total Fast Solver Time: {total_fast_time:.6f}s")
    print(f"Total Standard Solver Time: {total_standard_time:.6f}s")
    
    if total_fast_time > 0:
        multiplier = total_standard_time / total_fast_time
        print(f"CONCLUSION: fast_solver is {multiplier:.2f}x faster than the baseline!")
    else:
        print("CONCLUSION: fast_solver is infinitely faster! (time < precision)")

if __name__ == "__main__":
    run_benchmark()
