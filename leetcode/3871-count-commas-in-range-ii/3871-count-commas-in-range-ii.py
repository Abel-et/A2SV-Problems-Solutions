class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        
        # Check thresholds for 10^3, 10^6, 10^9, 10^12, 10^15
        for i in range(1, 6):
            threshold = 10 ** (3 * i)
            if n >= threshold:
                total_commas += (n - threshold + 1)
            else:
                break
                
        return total_commas
