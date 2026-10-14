class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # 1. Edge Case Check: If the target sum is impossible to achieve
        if sum > 9 * num or sum < 1:
            return ""
        
        # 2. Find out how many '9's we can fit, and what the leftover remainder is
        nines_count, remainder = divmod(sum, 9)
        
        # 3. Create the segments of our string
        nines_segment = "9" * nines_count
        remainder_segment = str(remainder) if remainder > 0 else ""
        
        # 4. Calculate how many zeros are needed to reach exactly `num` digits
        zeros_count = num - len(nines_segment) - len(remainder_segment)
        zeros_segment = "0" * zeros_count
        
        # Combine them: Largest digits first ensures maximum score and value
        return nines_segment + remainder_segment + zeros_segment
