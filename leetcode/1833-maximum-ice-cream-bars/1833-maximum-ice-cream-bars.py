class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        ice = 0

        for i in costs:
            if i <= coins:
                coins -= i
                ice += 1
                if coins <= 0:
                    return ice
        return ice
