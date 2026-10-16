class SegmentTree:
    def __init__(self, n):
        self.n = n
        # Padding size to 4 * n + 5 ensures no index boundary issues for small inputs
        size = 4 * n + 5
        self.sum_x = [0] * size   
        self.sum_x2 = [0] * size  
        self.lazy = [0] * size    

    def _push(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        lazy_val = self.lazy[node]
        mid = (start + end) // 2
        left_len = mid - start + 1
        right_len = end - mid
        
        # Update left child
        self.sum_x2[2 * node] += 2 * lazy_val * self.sum_x[2 * node] + lazy_val * lazy_val * left_len
        self.sum_x[2 * node] += lazy_val * left_len
        self.lazy[2 * node] += lazy_val
        
        # Update right child
        self.sum_x2[2 * node + 1] += 2 * lazy_val * self.sum_x[2 * node + 1] + lazy_val * lazy_val * right_len
        self.sum_x[2 * node + 1] += lazy_val * right_len
        self.lazy[2 * node + 1] += lazy_val
        
        self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            self.sum_x2[node] += 2 * val * self.sum_x[node] + val * val * (end - start + 1)
            self.sum_x[node] += val * (end - start + 1)
            self.lazy[node] += val
            return
            
        self._push(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            # FIX: The right segment range must begin at mid + 1
            self.update(2 * node + 1, mid + 1, end, l, r, val)
            
        self.sum_x[node] = self.sum_x[2 * node] + self.sum_x[2 * node + 1]
        self.sum_x2[node] = self.sum_x2[2 * node] + self.sum_x2[2 * node + 1]

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        total_ans = 0
        current_running_sum = 0
        MOD = 10**9 + 7
        
        for i, num in enumerate(nums):
            prev_idx = last_seen.get(num, -1)
            left_bound = prev_idx + 1
            right_bound = i
            
            # Fetch specific integer value at root index 1
            old_root_sum2 = tree.sum_x2[1]
            tree.update(1, 0, n - 1, left_bound, right_bound, 1)
            new_root_sum2 = tree.sum_x2[1]
            
            current_running_sum = (current_running_sum + (new_root_sum2 - old_root_sum2)) % MOD
            total_ans = (total_ans + current_running_sum) % MOD
            
            last_seen[num] = i
            
        return total_ans
