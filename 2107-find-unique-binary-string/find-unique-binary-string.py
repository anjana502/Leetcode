class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        n = len(nums[0])
        ls = [i for i in range(2 ** n)]

        for i in range(len(nums)):
            if (int(nums[i], 2) != ls[i]):
                s = bin(ls[i])[2:]
                d = n - len(s)
                s = ("0" * d) + s

                return s
        
        s = bin(ls[i + 1])[2:]
        d = n - len(s)
        s = ("0" * d) + s
        
        return s