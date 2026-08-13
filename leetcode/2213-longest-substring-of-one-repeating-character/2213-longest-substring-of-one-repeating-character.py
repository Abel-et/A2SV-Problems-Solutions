class Node:
    def __init__(self, char=None):
        # If it's a single character leaf node
        if char is not None:
            self.max_len = 1
            self.pref_len = 1
            self.suff_len = 1
            self.left_char = char
            self.right_char = char
            self.size = 1
        else:
            self.max_len = 0
            self.pref_len = 0
            self.suff_len = 0
            self.left_char = ''
            self.right_char = ''
            self.size = 0

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        # Segment tree array size allocation
        tree = [None] * (4 * n)
        
        # Helper function to merge two adjacent segment tree nodes
        def merge(left: Node, right: Node) -> Node:
            parent = Node()
            parent.size = left.size + right.size
            parent.left_char = left.left_char
            parent.right_char = right.right_char
            
            # Default prefix and suffix lengths from children
            parent.pref_len = left.pref_len
            parent.suff_len = right.suff_len
            
            # Default max length is the best of either child
            parent.max_len = max(left.max_len, right.max_len)
            
            # Check if characters meet at the boundary line
            if left.right_char == right.left_char:
                # If left child is entirely made of the same character
                if left.pref_len == left.size:
                    parent.pref_len = left.size + right.pref_len
                
                # If right child is entirely made of the same character
                if right.suff_len == right.size:
                    parent.suff_len = right.size + left.suff_len
                    
                # A new combined substring is formed across the middle boundary
                parent.max_len = max(parent.max_len, left.suff_len + right.pref_len)
                
            return parent

        # Build the initial segment tree
        def build(node_idx, start, end):
            if start == end:
                tree[node_idx] = Node(s[start])
                return
            mid = (start + end) // 2
            build(2 * node_idx, start, mid)
            build(2 * node_idx + 1, mid + 1, end)
            tree[node_idx] = merge(tree[2 * node_idx], tree[2 * node_idx + 1])

        # Update a single character in the segment tree
        def update(node_idx, start, end, target_idx, val):
            if start == end:
                tree[node_idx] = Node(val)
                return
            mid = (start + end) // 2
            if target_idx <= mid:
                update(2 * node_idx, start, mid, target_idx, val)
            else:
                update(2 * node_idx + 1, mid + 1, end, target_idx, val)
            tree[node_idx] = merge(tree[2 * node_idx], tree[2 * node_idx + 1])

        # 1. Build the tree out of the original string
        build(1, 0, n - 1)
        
        # 2. Process each query
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            
            # Update the character at the specified index
            update(1, 0, n - 1, idx, char)
            
            # The root node (index 1) always holds the maximum for the whole string
            ans.append(tree[1].max_len)
            
        return ans
