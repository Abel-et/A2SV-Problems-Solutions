class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        has_n = False
        for idx, _ in restrictions:
            if idx == n:
                has_n = True
                break

        if not has_n:
            restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # Left -> Right
        for i in range(1, m):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + d
            )

        # Right -> Left
        for i in range(m - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + d
            )

        ans = 0

        for i in range(m - 1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]

            d = x2 - x1

            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)

        return ans