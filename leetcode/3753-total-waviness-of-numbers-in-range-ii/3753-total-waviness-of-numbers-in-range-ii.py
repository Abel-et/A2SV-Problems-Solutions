class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(X: int) -> int:
            if X < 100:
                return 0
            
            s = str(X)
            n = len(s)
            
            # Memoization table: (index, prev_digit, prev_prev_digit, is_less, is_started)
            # Using a dictionary for simplicity due to negative/placeholder values for empty digits
            memo = {}
            
            def dp(idx, prev, pprev, is_less, is_started):
                # Base Case: No more digits to place
                if idx == n:
                    return 1, 0  # (1 valid number completed, 0 additional waviness from suffix)
                    
                state = (idx, prev, pprev, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                total_count = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            # Still leading zeros
                            cnt, wav = dp(idx + 1, -1, -1, next_less, False)
                            total_count += cnt
                            total_waviness += wav
                        else:
                            # First non-zero digit placed
                            cnt, wav = dp(idx + 1, d, -1, next_less, True)
                            total_count += cnt
                            total_waviness += wav
                    else:
                        # Check if the PREVIOUS digit forms a peak or valley with pprev and current d
                        is_peak_or_valley = 0
                        if pprev != -1:
                            if (prev > pprev and prev > d) or (prev < pprev and prev < d):
                                is_peak_or_valley = 1
                        
                        cnt, wav = dp(idx + 1, d, prev, next_less, True)
                        
                        total_count += cnt
                        # Every valid suffix branch gains 'is_peak_or_valley' amount of waviness
                        total_waviness += wav + (is_peak_or_valley * cnt)
                
                memo[state] = (total_count, total_waviness)
                return memo[state]
                
            return dp(0, -1, -1, False, False)[1]

        return solve(num2) - solve(num1 - 1)

 
