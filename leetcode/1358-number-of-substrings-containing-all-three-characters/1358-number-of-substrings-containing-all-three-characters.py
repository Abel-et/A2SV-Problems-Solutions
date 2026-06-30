class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        counts = {'a':0,'b':0,'c':0}
        cnt = 0
        left = 0
        n = len(s)

        for right in range(n):
            counts[s[right]] += 1
            while counts['a'] > 0 and counts['b'] > 0 and counts['c'] > 0 :
                cnt += (n-right)
                counts[s[left]] -=1
                left += 1
            
        return cnt