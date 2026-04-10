import argparse
import sys
import time
import http.client

def parse_args():
    parser = argparse.ArgumentParser(description="Ultra-fast Python solver for ASCII mazes.")
    parser.add_argument("--file", help="Path to a text file containing the ASCII maze.")
    parser.add_argument("--stdin", action="store_true", help="Read the ASCII maze from standard input.")
    parser.add_argument("--size", type=int, help="Generate and solve a maze of size n x n.")
    parser.add_argument("--seed", type=int, default=None, help="Optional seed used with --size.")
    parser.add_argument("--host", default="127.0.0.1", help="Target API host")
    parser.add_argument("--port", type=int, default=8000, help="Target API port")
    return parser.parse_args()

def _fetch_ascii_from_server(host, port, seed=None):
    conn = http.client.HTTPConnection(host, port)
    # The API might not accept seed in GET parameters for /ascii directly, but wait - 
    # The API docs say GET /ascii returns the ascii maze... Wait, I should just fetch it. 
    # Let me just send a basic GET request.
    conn.request("GET", "/ascii")
    response = conn.getresponse()
    if response.status != 200:
        raise ValueError(f"Failed to fetch maze: HTTP {response.status}")
    return response.read().decode('utf-8')

def _post_moves_to_server(host, port, moves):
    conn = http.client.HTTPConnection(host, port)
    for move in moves:
        payload = f'{{"direction":"{move}"}}'
        conn.request("POST", "/move", body=payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        response.read() # Consume response to free connection for reuse
    conn.close()

def solve(ascii_maze):
    # Dummy implementation for Phase 1
    return []

def main():
    args = parse_args()
    
    start_time = time.perf_counter()
    source_description = ""
    
    # Fast HTTP fetch if no local source specified
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            ascii_maze = f.read()
        source_description = f"file={args.file}"
    elif args.stdin:
        ascii_maze = sys.stdin.read()
        source_description = "stdin"
    elif getattr(args, 'size', None):
        # Local size/seed is tricky if not generating locally... 
        # But if size is specified, maybe it implies local generation or HTTP server config.
        # Fallback to fetching from server if neither file nor stdin is provided
        pass
    else:
        # Fallback network execution
        ascii_maze = _fetch_ascii_from_server(args.host, args.port, args.seed)
        source_description = f"http={args.host}:{args.port}"
        
    moves = solve(ascii_maze)
    elapsed_seconds = time.perf_counter() - start_time
    
    move_string = "".join(moves)
    print(f"Source: {source_description}")
    print(f"Moves: {move_string}")
    print(f"Move count: {len(moves)}")
    print(f"Elapsed seconds: {elapsed_seconds:.9f}")
    print("Solved maze:")
    # print string locally or solved ascii if available

if __name__ == "__main__":
    main()
