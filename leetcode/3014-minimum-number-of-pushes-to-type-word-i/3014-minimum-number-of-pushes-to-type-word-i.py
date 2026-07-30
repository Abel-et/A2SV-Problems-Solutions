class Solution:
    def minimumPushes(self, word: str) -> int:
        #  length of word less than or equal to 8
        if len(word) <= 8:
            return len(word)
        
        # length of word greater than 8 and less than or equal to 16 
        # formula = 8 + 2*(len(word) - 8)
        elif len(word) > 8 and len(word) <= 16:
            return 8 + 2*(len(word) - 8)
        
        # lenght of word greater than 16 and less than or equal to 24 
        #formula = 8 + 16 + 3*(len(word) - 16 )
        elif len(word) > 16 and len(word) <= 24:
            return 8 + 16 + 3*(len(word) - 16)
        
        # else if len greater than 24 
        # formula  = 8 + 16 + 24 + 4*(len(word) - 24)
        else:
            return 8 + 16 + 24 + 4*(len(word) - 24)