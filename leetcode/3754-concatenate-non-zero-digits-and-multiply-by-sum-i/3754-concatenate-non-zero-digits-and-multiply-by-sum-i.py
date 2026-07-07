class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        concat = ''

        for i in str(n) :
            if int(i) != 0:
                total += int(i)
                concat += i
        return int(concat) * total if concat != '' else  total