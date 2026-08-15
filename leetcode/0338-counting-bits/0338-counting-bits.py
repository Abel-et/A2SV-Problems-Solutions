class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []

        def convetIntoBinary(num ):
            s = []

            while num >=1:
                b = num % 2
                s.append(b)
                num = num // 2
            return s

        for i in range(n+1):
            arr = convetIntoBinary(i)

            ones = arr.count(1)
            ans.append(ones)

        return ans