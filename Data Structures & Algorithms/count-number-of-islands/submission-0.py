class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid)-1, len(grid[0])-1
        islandCount = 0

        def dfs(grid, i, j):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            if i != 0 and grid[i-1][j] == '1':
                dfs(grid, i-1, j)
            if j != 0 and grid[i][j-1] == '1':
                dfs(grid, i, j-1)
            if i != n and grid[i+1][j] == '1':
                dfs(grid, i+1, j)
            if j != m and grid[i][j+1] == '1':
                dfs(grid, i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                dfs(grid, i, j)
                islandCount += 1

        return islandCount

    