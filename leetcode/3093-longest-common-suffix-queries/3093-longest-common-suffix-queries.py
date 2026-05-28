class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the best matching container word for this suffix path
        self.best_idx = -1 

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # Helper function to check if string 'i' is a better choice than string 'j'
        def is_better(i, j):
            if j == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return True
            if len(wordsContainer[i]) == len(wordsContainer[j]) and i < j:
                return True
            return False

        # Find the overall best default index for the root node
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if is_better(i, global_best_idx):
                global_best_idx = i
        root.best_idx = global_best_idx

        # Insert all container words into the Trie in reverse order
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Traverse backward to process suffixes as prefixes
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                # Update the node's best index if the current word is a better match
                if is_better(idx, curr.best_idx):
                    curr.best_idx = idx

        # Process each query
        ans = []
        for query in wordsQuery:
            curr = root
            # Traverse backward to match the suffix
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break # No deeper common suffix exists
            ans.append(curr.best_idx)
            
        return ans
