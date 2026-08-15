class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def convetIntoBinary(num ):
            s = 0
            while num >=1:
                b = num % 2
                if b == 1:
                    s += 1
                num = num // 2
            return s

        return [convetIntoBinary(i) for i in range(n+1)]