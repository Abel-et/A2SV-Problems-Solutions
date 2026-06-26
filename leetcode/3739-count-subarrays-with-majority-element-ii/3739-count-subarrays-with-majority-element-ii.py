class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Fenwick Tree (Binary Indexed Tree) to count smaller prefix sums
        # Prefix sum range can be from -n to n. 
        # Shift everything by (n + 1) to keep indices positive.
        tree_size = 2 * n + 2
        bit = [0] * tree_size
        
        def update(idx, val):
            while idx < tree_size:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        ans = 0
        prefix_sum = 0
        offset = n + 1  # Shifts -n to 1
        
        # Add the initial prefix sum of 0 to the BIT
        update(0 + offset, 1)
        
        for num in nums:
            # Map target to +1, others to -1
            prefix_sum += 1 if num == target else -1
            
            # Count how many previous prefix sums are strictly smaller than the current one
            ans += query(prefix_sum + offset - 1)
            
            # Store the current prefix sum in the BIT
            update(prefix_sum + offset, 1)
            
        return ans
