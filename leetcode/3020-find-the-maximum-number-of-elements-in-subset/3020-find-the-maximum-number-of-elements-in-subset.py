from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        cnt = 0
        for i in count:
            length = 0
            if i == 1:
                cnt = max(cnt, count[1] if count[1] % 2 else count[1] - 1)
                continue
            current = i
            
            while count[current] >=2:
                length += 2
                current = current **2
            if count[current] == 1:
                length += 1
            else:
                length -=1 
            cnt = max(cnt, length)
        return cnt

                    
                    


                
            