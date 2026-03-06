class Solution:
    def countSubarrays(self, nums, goal):
        sum1 = 0
        j = 0
        count = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            while (j <= i and sum1 > goal):
                sum1 -= nums[j]
                j += 1
            
            count += (i - j + 1)
        
        return count
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count1 = self.countSubarrays(nums, goal)
        count2 = self.countSubarrays(nums, goal - 1)

        d = count1 - count2

        return d