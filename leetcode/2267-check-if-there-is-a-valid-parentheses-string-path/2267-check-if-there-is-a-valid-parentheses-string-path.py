class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        r = len(grid)
        c = len(grid[0])

        if grid[0][0] ==')' or grid[r-1][c-1] == '(':
            return False

        @cache
        def dfs(x, y , count):
            if x == r-1 and y == c-1:
                return count == 1
            
            if grid[x][y] == '(':
                if x + 1 < r and dfs(x + 1, y , count + 1):
                    return True
                if y + 1 < c and dfs(x , y + 1, count + 1):
                    return True
            else: 
                if count == 0: 
                    return False
                if x + 1 < r and dfs(x + 1, y , count -1):
                    return True
                if y + 1 < c and dfs(x, y+1 , count -1):
                    return True
            return False
        return dfs(0,0,0)