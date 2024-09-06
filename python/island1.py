class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid)

        self.visited = dict()
        self.grid = grid

        numIslands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if (grid[row][col] == "1"):
                    key = f"{row}:{col}"
                    if not key in self.visited:
                        numIslands += 1
                        self.scanAndMarkIsland(row, col, numIslands) 
        
        return numIslands

    def scanAndMarkIsland(self, r, c, islandId):
        key = f"{r}:{c}"
        if key in self.visited:
            return
        self.visited[key] = islandId
        
        #left
        if c-1>=0 and grid[r][c-1] == "1":
            self.scanAndMarkIsland(r, c-1, islandId)

        #top
        if r-1>=0 and grid[r-1][c] == "1" :
            self.scanAndMarkIsland(r-1, c, islandId)

        #right
        if c+1 < self.cols and grid[r][c+1] == "1":
            self.scanAndMarkIsland(r, c+1, islandId)

        #bottom
        if r+1 < self.rows and grid[r+1][c] == "1":
            self.scanAndMarkIsland(r+1, c, islandId)

    def print(self):
         for row in range(self.rows):
            rowv = []
            for col in range(self.cols):
                if (self.grid[row][col] == "1"):
                    key = f"{row}:{col}"
                    rowv.append(str(self.visited[key]))
                else:
                    rowv.append("0")
            print(",".join(rowv))
s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

numIslands = s.numIslands(grid)

print(f"number of islands : {numIslands}")

#print the grid island ids
s.print()
