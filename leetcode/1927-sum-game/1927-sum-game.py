class Solution:
    def sumGame(self, num: str) -> bool:
        n , half = len(num) , len(num)//2
        sum1, sum2, count1, count2 = 0, 0 ,0 ,0

        for i in range(n):
            if i < half:
                if num[i].isdigit() :
                    sum1 += int(num[i])
                else:
                    count1 += 1
            else:
                if num[i].isdigit() :
                    sum2 += int(num[i])
                else: 
                    count2 += 1
        sum_diff = sum1 - sum2
        count_diff = count1 - count2

        result = (sum_diff + (count_diff/2) * 9) == 0

        return not result

