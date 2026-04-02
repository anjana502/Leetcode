from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] != 0):
            return -1
        
        n = len(grid)
        q = deque()
        ls = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, 1], [1, -1], [1, 1], [-1, -1]]
        s = set()
        q.append((0, 0, 1))
        s.add((0, 0))

        while (len(q) != 0):
            i, j, d = q.popleft()

            if ((i, j) == (n - 1, n - 1)):
                return d
            
            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= n) or ((row, col) in s) or (grid[row][col] != 0)):
                    continue
                
                q.append((row, col, d + 1))
                s.add((row, col))
        
        return -1