class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ls = sorted(nums)
        left = -1
        right = -1

        for i in range(len(nums)):
            if (nums[i] != ls[i]):
                left = i
                break

        if (left == -1):
            return 0

        for j in range(len(nums) - 1, -1, -1):
            if (nums[j] != ls[j]):
                right = j
                break

        print((right, left))

        d = (right - left + 1)

        return d    