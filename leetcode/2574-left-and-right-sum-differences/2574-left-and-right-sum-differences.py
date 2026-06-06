class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        # Step 1: Initialize the total sum and the running left sum
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        # Step 2: Iterate through the array to build the answer
        for num in nums:
            # right_sum is total minus left_sum and the current element
            right_sum = total_sum - left_sum - num
            
            # Append the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum for the next iteration
            left_sum += num
            
        return answer
