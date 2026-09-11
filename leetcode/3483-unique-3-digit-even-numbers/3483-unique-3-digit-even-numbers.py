class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        numbers = set()
        n = len(digits)

            # hundreds 
        for i in range(n):
                # in this case we don't need to start by zero
            if digits[i] == 0:
                continue
                # tens 
            for j in range(n):
                    # here we don't need to have same index with hunderds or(i)
                if j == i :
                    continue
                    # ones 
                for k in range(n):
                        # here also we don't need have the same indexes with i and j 
                    if k == j or k == i:
                        continue
                    digit = digits[i] * 100 + digits[j]*10 + digits[k]
                   
                    # check if the number is odd or its in the set
                    if digit % 2 == 1 or digit in numbers:
                            continue
                    else:
                        numbers.add(digit)
            
        return len(numbers)