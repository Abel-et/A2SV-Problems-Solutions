from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        count = {}

        for j , c in enumerate(s):
            count[c] = count.get(c,0) +1
            while count[c] > 2:
                count[s[left]] -=1 
                left += 1
            ans = max(ans, j - left + 1)
        return ans