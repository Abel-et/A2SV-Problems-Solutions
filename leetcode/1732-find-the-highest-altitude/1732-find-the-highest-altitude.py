class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        for i in range(len(gain)):
            last = arr[-1] + gain[i]
            arr.append(last)
        return max(arr)