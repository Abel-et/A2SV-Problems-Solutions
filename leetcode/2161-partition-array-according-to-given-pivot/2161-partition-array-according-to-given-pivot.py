class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equl , less, greater = [], [ ], [ ]

        for i in nums:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equl.append(i)
        return less + equl + greater
        