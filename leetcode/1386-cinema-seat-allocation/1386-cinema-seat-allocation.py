from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        container = defaultdict(list)
    

        for row , seat in reservedSeats:
            container[row].append(seat)
        
        empty_row = n - len(container)
        total  = empty_row*2
        
        for row , seat in container.items() :

            left = not( 2 in seat or 3 in seat or 4 in seat or 5 in seat)
            middle = not (4 in seat or 5 in seat or 6 in seat or 7 in seat )
            right = not (6 in seat or 7 in seat or 8 in seat or  9 in seat)

            if left and right :
                total += 2
            elif left or right :
                total += 1
            elif middle :
                total +=1 
        
        
           
        return total 
            

