class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

           # 1. Remove duplicates and sort to find unique values in ascending order
        unique_sorted = sorted(set(arr))
        
        # 2. Map each unique number to its 1-based rank
        rank_map = {num: rank + 1 for rank, num in enumerate(unique_sorted)}
        
        # 3. Rebuild the array using the rank dictionary
        return [rank_map[num] for num in arr]
