class Solution:
    def twoSum(self, nums, target):
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in visited:
                return [visited[diff], i]

            visited[nums[i]] = i