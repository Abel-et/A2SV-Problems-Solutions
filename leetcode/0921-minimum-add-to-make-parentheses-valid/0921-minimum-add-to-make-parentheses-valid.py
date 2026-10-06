class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s :
            return 0
        

        stack = []

        for i in s:
            #  if the current bracket is open append to stack
            if i == '(':
                stack.append(i)
            
            # if the current bracket is closed 
            # check the last stack element is opened
                # if it is opend pop the from the stack
                # else if it the stack is empty or closed bracket add to the stack
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)
