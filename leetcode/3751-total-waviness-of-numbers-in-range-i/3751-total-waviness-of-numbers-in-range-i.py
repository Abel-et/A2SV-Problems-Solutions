class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        if num2 <= 100 :
            return 0
        total_waviness = 0 
        
        # Iterate through every number in the inclusive range
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Numbers with fewer than 3 digits have a waviness of 0
            if n < 3:
                continue
                
            # Check every internal digit (ignoring the first and last digits)
            for i in range(1, n - 1):
                prev_digit = int(s[i - 1])
                curr_digit = int(s[i])
                next_digit = int(s[i + 1])
                
                # Check for Peak
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # Check for Valley
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness
