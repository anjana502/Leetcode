class Solution:
    def isSubsequence1(self, s, t, i, j):
        if (i == len(s)):
            return True
        if (j == len(t)):
            return False
        
        if (s[i] == t[j]):
            return self.isSubsequence1(s, t, i + 1, j + 1)
        return self.isSubsequence1(s, t, i, j + 1)
    
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.isSubsequence1(s, t, 0, 0)