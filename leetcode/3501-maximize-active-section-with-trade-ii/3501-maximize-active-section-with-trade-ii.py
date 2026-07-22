import bisect
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        

            
        # Step 1: Extract all blocks of 1s
        blocks = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '1':
                st = i
                while i < n and s[i] == '1':
                    i += 1
                blocks.append((st, i - 1))
            else:
                i += 1
                
        m = len(blocks)
        if m == 0:
            return [0] * len(queries)
            
        total_ones = s.count('1')
        
        # Precalculate intrinsic zeros for interior blocks
        # zeros = st_{k+1} - ed_{k-1} - ed_k + st_k - 2
        intrinsic_zeros = [0] * m
        for k in range(m):
            st_k, ed_k = blocks[k]
            # boundaries
            st_next = blocks[k+1][0] if k < m - 1 else n
            ed_prev = blocks[k-1][1] if k > 0 else -1
            intrinsic_zeros[k] = st_next - ed_prev - ed_k + st_k - 2

        # Build a Sparse Table for RMQ on intrinsic_zeros
        # Since we need RMQ, let's build it
        K = m.bit_length()
        st_table = [[0] * K for _ in range(m)]
        for i in range(m):
            st_table[i][0] = intrinsic_zeros[i]
        for j in range(1, K):
            for i in range(m - (1 << j) + 1):
                st_table[i][j] = max(st_table[i][j-1], st_table[i + (1 << (j-1))][j-1])
                
        def query_rmq(L, R):
            if L > R:
                return 0
            j = (R - L + 1).bit_length() - 1
            return max(st_table[L][j], st_table[R - (1 << j) + 1][j])

        # Extract block starts and ends for binary search
        block_starts = [b[0] for b in blocks]
        block_ends = [b[1] for b in blocks]
        
        ans = []
        for l, r in queries:
            # Find the range of blocks completely inside [l+1, r-1]
            # st_k >= l+1 and ed_k <= r-1
            first_idx = bisect.left_bound = bisect.bisect_left(block_starts, l + 1)
            last_idx = bisect.bisect_right(block_ends, r - 1) - 1
            
            if first_idx > last_idx:
                ans.append(total_ones)
                continue
                
            max_zeros = 0
            
            if first_idx == last_idx:
                # Only one block inside
                k = first_idx
                st, ed = blocks[k]
                L = max(l, blocks[k-1][1] + 1) if k > 0 else l
                R = min(r, blocks[k+1][0] - 1) if k < m - 1 else r
                zeros = (R - L + 1) - (ed - st + 1)
                max_zeros = max(max_zeros, zeros)
            else:
                # first_idx < last_idx
                # Handle first_idx
                k = first_idx
                st, ed = blocks[k]
                L = max(l, blocks[k-1][1] + 1) if k > 0 else l
                R = blocks[k+1][0] - 1 # since k+1 <= last_idx, blocks[k+1][0]-1 <= r-1 < r
                zeros = (R - L + 1) - (ed - st + 1)
                max_zeros = max(max_zeros, zeros)
                
                # Handle last_idx
                k = last_idx
                st, ed = blocks[k]
                L = blocks[k-1][1] + 1 # since k-1 >= first_idx, blocks[k-1][1]+1 >= l+1 > l
                R = min(r, blocks[k+1][0] - 1) if k < m - 1 else r
                zeros = (R - L + 1) - (ed - st + 1)
                max_zeros = max(max_zeros, zeros)
                
                # Handle strict interior
                if first_idx + 1 <= last_idx - 1:
                    max_zeros = max(max_zeros, query_rmq(first_idx + 1, last_idx - 1))
                    
            ans.append(total_ones + max_zeros)
            
        return ans

