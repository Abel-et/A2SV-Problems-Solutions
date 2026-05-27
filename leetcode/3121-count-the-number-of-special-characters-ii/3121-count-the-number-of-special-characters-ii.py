class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char = {}
        cnt = 0

        for i in range(len(word)):
            if word[i] not in char:
                char[word[i]] = [i]
            else:
                char[word[i]].append(i)
      

        for j in set(word):
            if j.islower() and j.upper() in char:
                if (max(char[j]) < max(char[j.upper()])) and (min(char[j.upper()]) > max(char[j])):
                    cnt += 1
        return cnt

