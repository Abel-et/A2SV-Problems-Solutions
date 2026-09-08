class Solution:
    def countCommas(self, n: int) -> int:
        length = len(str(n))

        if length < 4:
            return 0
        
        return int(str(n)[1:]) + 1  if n < 2000 else int(str(n)) + 1 -1000