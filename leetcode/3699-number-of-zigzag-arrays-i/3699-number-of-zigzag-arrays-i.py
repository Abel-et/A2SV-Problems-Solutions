class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        # Base cases for length n = 2
        # dp_inc[v] stores count of prefixes ending with an increase to value v
        # dp_dec[v] stores count of prefixes ending with a decrease to value v
        dp_inc = [v for v in range(k)]
        dp_dec = [(k - 1 - v) for v in range(k)]
        
        # Transition for lengths from 3 to n
        for i in range(3, n + 1):
            next_inc = [0] * k
            next_dec = [0] * k
            
            # Prefix sum optimization for increasing transitions
            # next_inc[v] = sum(dp_dec[0] ... dp_dec[v-1])
            running_dec_sum = 0
            for v in range(k):
                next_inc[v] = running_dec_sum % MOD
                running_dec_sum += dp_dec[v]
                
            # Suffix sum optimization for decreasing transitions
            # next_dec[v] = sum(dp_inc[v+1] ... dp_inc[k-1])
            running_inc_sum = 0
            for v in range(k - 1, -1, -1):
                next_dec[v] = running_inc_sum % MOD
                running_inc_sum += dp_inc[v]
                
            dp_inc = next_inc
            dp_dec = next_dec
            
        # Total result is the sum of all valid configurations at length n
        return (sum(dp_inc) + sum(dp_dec)) % MOD