class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        k = k1 + k2
        
        # If the total budget k is enough to reduce all differences to 0
        if sum(diffs) <= k:
            return 0
            
        # Binary search range for the threshold target
        low, high = 0, max(diffs)
        optimal_threshold = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total operations needed to reduce all diffs > mid down to mid
            ops_needed = sum(d - mid for d in diffs if d > mid)
            
            if ops_needed <= k:
                optimal_threshold = mid  # mid is achievable
                high = mid - 1           # Try to find a smaller threshold
            else:
                low = mid + 1            # mid is too small, we need more operations than budget
                
        # Apply the optimal threshold
        # Deduct the operations used from our budget k
        for i in range(len(diffs)):
            if diffs[i] > optimal_threshold:
                k -= (diffs[i] - optimal_threshold)
                diffs[i] = optimal_threshold
                
        # Use any leftover k to reduce elements equal to optimal_threshold down to optimal_threshold - 1
        for i in range(len(diffs)):
            if k > 0 and diffs[i] == optimal_threshold and diffs[i] > 0:
                diffs[i] -= 1
                k -= 1
                
        return sum(d * d for d in diffs)
