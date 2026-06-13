class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
           
        s = ''
        max_wight = ord('z')
        for word in words :
            val = 0 
            for letter in word:
                # acessing index form weights  
                index_weights = ord(letter) - ord('a')
                val += weights[index_weights]
         
            s +=  chr(max_wight - val%26)
        return s