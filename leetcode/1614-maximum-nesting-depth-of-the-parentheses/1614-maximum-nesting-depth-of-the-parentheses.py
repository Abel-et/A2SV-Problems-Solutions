class Solution:
    def maxDepth(self, s: str) -> int:
        max_num , num = 0, 0 

        for i in s:
            if i == '(':
                num += 1
            elif i == ')':
                num -= 1
            max_num = max(num , max_num)
        return max_num