from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        s = set()
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(n):
            for j in range(n):
                if (grid[i][j] == 1):
                    q.append((i, j))
                    s.add((i, j))
        
        level = -1

        while (len(q) != 0):
            d = len(q)

            for i in range(d):
                i, j = q.popleft()

                for k in ls:
                    row = i + k[0]
                    col = j + k[1]

                    if ((row < 0 or row >= n) or (col < 0 or col >= n) or (grid[row][col] != 0) or ((row, col) in s)):
                        continue
                    
                    q.append((row, col))
                    s.add((row, col))
            
            level += 1
        
        if (level != 0):
            return level
        return -1