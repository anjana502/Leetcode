class Solution:
    def isSubsequence(self, t, s):
        prev = -1

        for i in range(len(t)):
            index = s.find(t[i], prev + 1)

            if (index == -1):
                return False
            
            prev = index
        
        return True
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        for t in words:
            if (self.isSubsequence(t, s) == True):
                count += 1
            
            print("--------------------")
        
        return count