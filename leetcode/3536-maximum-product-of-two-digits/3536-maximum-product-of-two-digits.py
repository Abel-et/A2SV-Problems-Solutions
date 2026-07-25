class Solution:
    def maxProduct(self, n: int) -> int:
        k = [int(i) for i in  str(n)]
        first  = max(k)
        k.remove(first)

        second = max(k)

        return first * second