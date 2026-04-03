class Solution:
    def minDistance1(self, n, m, word1, word2, mat):
        if (n == 0):
            return m
        if (m == 0):
            return n
        
        if (mat[n][m] != -1):
            return mat[n][m]
        
        if (word1[n - 1] == word2[m - 1]):
            mat[n][m] = self.minDistance1(n - 1, m - 1, word1, word2, mat)
        else:
            mat[n][m] = 1 + min(self.minDistance1(n - 1, m, word1, word2, mat), self.minDistance1(n, m - 1, word1, word2, mat), self.minDistance1(n - 1, m - 1, word1, word2, mat))
        
        return mat[n][m]
    
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        mat = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        return self.minDistance1(n, m, word1, word2, mat)