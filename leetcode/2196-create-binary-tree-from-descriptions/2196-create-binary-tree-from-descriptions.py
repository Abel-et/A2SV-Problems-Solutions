# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Hash map to map node values to actual TreeNode objects
        nodes = {}
        # Hash set to track all values that are children
        children = set()
        
        # Step 1: Build the tree structure and record children
        for parent_val, child_val, is_left in descriptions:
            # Create parent node if it doesn't exist
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            # Create child node if it doesn't exist
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Connect parent to child
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Mark this node as a child
            children.add(child_val)
            
        # Step 2: Find the root (the parent node that is never a child)
        for parent_val, _, _ in descriptions:
            if parent_val not in children:
                return nodes[parent_val]
                
        return None
