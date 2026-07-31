from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        # the problem needs to sort the give letters by ther frequency
        freq = Counter(word).most_common()
        
        ans = 0
        for i in range(len(freq)):
            if i < 8:
                ans += freq[i][1]
            elif i > 7 and i <= 15:
                ans += freq[i][1] * 2
            elif i > 15 and i <=23:
                ans += freq[i][1] * 3
            else:
                ans += freq[i][1] * 4
        return ans
           
