from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Step 1: Map each row to a bitmask representing reserved seats
        # We only care about seats 2 to 9
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                # Set the bit corresponding to the seat position (0-indexed shift)
                row_masks[row] |= (1 << (seat - 2))
        
        # Step 2: Define masks for the three valid 4-seat blocks
        # Seats 2,3,4,5 correspond to the first 4 bits -> binary 00001111 -> decimal 15
        left_mask = 0b00001111   
        # Seats 6,7,8,9 correspond to the last 4 bits -> binary 11110000 -> decimal 240
        right_mask = 0b11110000  
        # Seats 4,5,6,7 correspond to the middle 4 bits -> binary 00111100 -> decimal 60
        middle_mask = 0b00111100 
        
        # Start by assuming all completely empty rows get 2 groups each
        empty_rows = n - len(row_masks)
        total_groups = empty_rows * 2
        
        # Step 3: Check rows that have at least one reservation
        for mask in row_masks.values():
            cnt = 0
            # Check left block (2,3,4,5)
            left_free = (mask & left_mask) == 0
            # Check right block (6,7,8,9)
            right_free = (mask & right_mask) == 0
            
            if left_free:
                cnt += 1
            if right_free:
                cnt += 1
                
            # If neither left nor right blocks are fully free, check middle block (4,5,6,7)
            if not left_free and not right_free:
                if (mask & middle_mask) == 0:
                    cnt += 1
                    
            total_groups += cnt
            
        return total_groups
