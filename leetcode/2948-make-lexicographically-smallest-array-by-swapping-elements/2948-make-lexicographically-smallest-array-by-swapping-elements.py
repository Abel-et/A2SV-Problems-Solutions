from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # Sort by value while remembering original indices
        arr = sorted((value, index) for index, value in enumerate(nums))

        result = nums[:]

        start = 0

        while start < n:
            end = start

            # Find the whole connected group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Original indices in this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted because arr is sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Assign smallest values to smallest indices
            for index, value in zip(indices, values):
                result[index] = value

            start = end + 1

        return result