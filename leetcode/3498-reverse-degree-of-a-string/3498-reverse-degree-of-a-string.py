class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = {}
        character = 'abcdefghijklmnopqrstuvwxyz'
        interval = 71
        for i in range(len(character)):
            degree[character[i]] = ord(character[i]) - (interval + 2*i)
        ans = 0
        for index , value in enumerate(s):
            ans += (index + 1) * degree[value]
        return ans
           