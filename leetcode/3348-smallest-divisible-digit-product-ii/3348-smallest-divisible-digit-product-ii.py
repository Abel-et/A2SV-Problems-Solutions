class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Extract prime factors of t
        temp_t = t
        target_2 = target_3 = target_5 = target_7 = 0
        
        while temp_t % 2 == 0: target_2 += 1; temp_t //= 2
        while temp_t % 3 == 0: target_3 += 1; temp_t //= 3
        while temp_t % 5 == 0: target_5 += 1; temp_t //= 5
        while temp_t % 7 == 0: target_7 += 1; temp_t //= 7
        
        if temp_t > 1:
            return "-1"

        # Hardcode prime factors for single digits 1-9 to save dict lookup memory
        # Format: (factor_2, factor_3, factor_5, factor_7)
        digit_factors = [
            (0, 0, 0, 0),  # 0 (unused)
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        # Greedy logic to find the minimum digits needed for a specific factor set
        def get_min_needed_digits(f2, f3, f5, f7):
            f2, f3, f5, f7 = max(0, f2), max(0, f3), max(0, f5), max(0, f7)
            res = []
            
            res.extend(['7'] * f7)
            res.extend(['5'] * f5)
            
            cnt9 = f3 // 2
            f3 %= 2
            
            cnt8 = f2 // 3
            f2 %= 3
            
            if f3 == 1 and f2 >= 1:
                res.append('6')
                f3 -= 1
                f2 -= 1
            if f3 == 1:
                res.append('3')
            if f2 == 2:
                res.append('4')
            elif f2 == 1:
                res.append('2')
                
            res.extend(['9'] * cnt9)
            res.extend(['8'] * cnt8)
            
            res.sort()
            return "".join(res)

        n = len(num)
        
        # Step 2: Use highly efficient primitive flat lists instead of dictionaries
        pref2 = [0] * (n + 1)
        pref3 = [0] * (n + 1)
        pref5 = [0] * (n + 1)
        pref7 = [0] * (n + 1)
        
        first_zero = -1
        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break
            d = int(ch)
            f2, f3, f5, f7 = digit_factors[d]
            pref2[i + 1] = pref2[i] + f2
            pref3[i + 1] = pref3[i] + f3
            pref5[i + 1] = pref5[i] + f5
            pref7[i + 1] = pref7[i] + f7

        # Case A: If original number has no zeros and already clears requirements
        if first_zero == -1:
            if pref2[n] >= target_2 and pref3[n] >= target_3 and pref5[n] >= target_5 and pref7[n] >= target_7:
                return num

        # Step 3: Backtrack from right to left
        limit = first_zero if first_zero != -1 else n - 1
        
        for i in range(limit, -1, -1):
            curr_d = int(num[i])
            for d in range(curr_d + 1, 10):
                f2, f3, f5, f7 = digit_factors[d]
                
                rem_2 = target_2 - pref2[i] - f2
                rem_3 = target_3 - pref3[i] - f3
                rem_5 = target_5 - pref5[i] - f5
                rem_7 = target_7 - pref7[i] - f7
                
                min_suffix = get_min_needed_digits(rem_2, rem_3, rem_5, rem_7)
                rem_len = n - 1 - i
                
                if len(min_suffix) <= rem_len:
                    num_ones = rem_len - len(min_suffix)
                    return num[:i] + str(d) + ('1' * num_ones) + min_suffix

        # Step 4: Fallback to scaling out length if length n is insufficient
        base_suffix = get_min_needed_digits(target_2, target_3, target_5, target_7)
        target_len = max(n + 1, len(base_suffix))
        
        return '1' * (target_len - len(base_suffix)) + base_suffix
