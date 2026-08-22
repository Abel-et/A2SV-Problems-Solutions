class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n < 10:
            return False
        
        num = str(n)
        product , sum = 1, 0

        for i in num:
            product *= int(i)
            sum += int(i)
        
        return True if n % (product + sum) == 0 else False