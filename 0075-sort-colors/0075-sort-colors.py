class Solution:
    def sortColors(self, nums):
        c = [0, 0, 0]

        for x in nums:
            c[x] += 1

        i = 0
        for x in range(3):
            for _ in range(c[x]):
                nums[i] = x
                i += 1