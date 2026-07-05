class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # Initialize DP tables
        # max_score stores the max score from (r, c) to (0, 0). -1 means unreachable.
        max_score = [[-1] * n for _ in range(n)]
        # paths stores the number of paths yielding that max score.
        paths = [[0] * n for _ in range(n)]
        
        # Base case at 'E' (0,0)
        max_score[0][0] = 0
        paths[0][0] = 1
        
        # Fill the DP table row by row from top to bottom, left to right
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'X' or (r == 0 and c == 0):
                    continue
                
                # Check the 3 incoming directions: Up, Left, Up-Left
                # From current cell perspective looking back to already calculated cells:
                # We look at (r-1, c), (r, c-1), and (r-1, c-1)
                best_prev_score = -1
                current_paths = 0
                
                directions = [(r - 1, c), (r, c - 1), (r - 1, c - 1)]
                
                for pr, pc in directions:
                    if 0 <= pr < n and 0 <= pc < n and max_score[pr][pc] != -1:
                        if max_score[pr][pc] > best_prev_score:
                            best_prev_score = max_score[pr][pc]
                            current_paths = paths[pr][pc]
                        elif max_score[pr][pc] == best_prev_score:
                            current_paths = (current_paths + paths[pr][pc]) % MOD
                
                # If at least one previous cell was reachable, update current cell
                if best_prev_score != -1:
                    cell_value = 0 if board[r][c] == 'S' else int(board[r][c])
                    max_score[r][c] = best_prev_score + cell_value
                    paths[r][c] = current_paths
                    
        # The result is stored at the bottom-right corner 'S' (n-1, n-1)
        if max_score[n-1][n-1] == -1:
            return [0, 0]
            
        return [max_score[n-1][n-1], paths[n-1][n-1]]