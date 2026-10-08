class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []

        for i in s:
            if i == '(':
                if depth > 0:
                    result.append(i)
                depth += 1
            else:
                depth -=1
                if depth > 0:
                    result.append(i)
        return ''.join(result)
                
        
