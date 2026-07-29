class Solution:
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in prefix:
                count += prefix[prefixSum - k]

            prefix[prefixSum] = prefix.get(prefixSum, 0) + 1

        return count