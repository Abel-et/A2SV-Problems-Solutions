class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s = str(n)
            if len(s) < 2:
                if n % t == 0:
                    return n
                n += 1
                continue
            else:
                left = int(s[0])
                right = int(s[1])
                if left * right % t == 0:
                    return int(s)
                else :
                    n += 1