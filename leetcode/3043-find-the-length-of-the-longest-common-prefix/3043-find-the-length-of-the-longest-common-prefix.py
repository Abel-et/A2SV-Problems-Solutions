class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        prefixes = set()

        # Store all prefixes from arr1
        for num in arr1:
            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        longest = 0

        # Check prefixes from arr2
        for num in arr2:
            s = str(num)

            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    longest = max(longest, i)

        return longest