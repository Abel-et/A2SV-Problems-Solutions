class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        # Step 1: Generate all unique pairwise XOR combinations
        unique_pairs = set()
        for i in range(len(unique_nums)):
            for j in range(i, len(unique_nums)):
                unique_pairs.add(unique_nums[i] ^ unique_nums[j])
        
        # Step 2: Combine pairs with a third element to find unique triplets
        unique_triplets = set()
        for pair in unique_pairs:
            for num in unique_nums:
                unique_triplets.add(pair ^ num)
                
        return len(unique_triplets)