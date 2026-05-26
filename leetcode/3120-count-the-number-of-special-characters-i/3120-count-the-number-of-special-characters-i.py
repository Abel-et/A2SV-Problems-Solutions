from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        words = Counter(word)
        cnt = 0
        for i in words.keys():
            if i.islower() and i.upper() in words:
                cnt += 1        
        return cnt


