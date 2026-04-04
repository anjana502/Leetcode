class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        mat = [[" " for j in range(cols)] for i in range(rows)]
        i = -1
        j = 0

        for k in range(n):
            if (k % cols == 0):
                i += 1
                j = 0
            
            mat[i][j] = encodedText[k]
            j += 1
        
        originalText = ""
        k = 0

        while (k < cols):
            s = ""
            i = 0
            j = k

            while (i < rows and j < cols):
                s += mat[i][j]
                
                i += 1
                j += 1
            
            originalText += s
            k += 1
        
        return originalText.rstrip()