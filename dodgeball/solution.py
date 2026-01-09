import sys

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def get_direction(dx, dy):
    if dx == 0 and dy == 0:
        return None
    
    if dx == 0:
        return 'N' if dy > 0 else 'S'
    if dy == 0:
        return 'E' if dx > 0 else 'W'
    
    if abs(dx) != abs(dy):
        return None
    
    if dx > 0 and dy > 0:
        return 'NE'
    if dx > 0 and dy < 0:
        return 'SE'
    if dx < 0 and dy < 0:
        return 'SW'
    if dx < 0 and dy > 0:
        return 'NW'
    
    return None

def distance_sq(dx, dy):
    return dx * dx + dy * dy

def solve_game(players, start_dir, start_player):
    active = set(players.keys())
    current_player = start_player
    received_from = start_dir
    throws = 0
    
    while True:
        cx, cy = players[current_player]
        
        # Get the starting search direction (next clockwise from received direction)
        start_idx = (DIRECTIONS.index(received_from) + 1) % 8
        
        found_target = None
        found_dir = None
        
        # Try all 8 directions clockwise starting from start_idx
        for i in range(8):
            search_dir = DIRECTIONS[(start_idx + i) % 8]
            
            # Find nearest player in this direction
            best_player = None
            best_dist = float('inf')
            
            for pid in active:
                if pid == current_player:
                    continue
                px, py = players[pid]
                dx, dy = px - cx, py - cy
                
                direction = get_direction(dx, dy)
                if direction == search_dir:
                    dist = distance_sq(dx, dy)
                    if dist < best_dist:
                        best_dist = dist
                        best_player = pid
            
            if best_player is not None:
                found_target = best_player
                found_dir = search_dir
                break
        
        if found_target is None:
            return throws, current_player
        
        throws += 1
        active.remove(current_player)
        
        # The new player receives from the opposite direction
        opposite_idx = (DIRECTIONS.index(found_dir) + 4) % 8
        received_from = DIRECTIONS[opposite_idx]
        current_player = found_target

def main():
    input_data = sys.stdin.read().split('\n')
    idx = 0
    
    T = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        
        players = {}
        for p in range(1, N + 1):
            parts = input_data[idx].split()
            x, y = int(parts[0]), int(parts[1])
            players[p] = (x, y)
            idx += 1
        
        start_dir = input_data[idx].strip()
        idx += 1
        
        start_player = int(input_data[idx])
        idx += 1
        
        throws, last_player = solve_game(players, start_dir, start_player)
        results.append(f"{throws} {last_player}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
