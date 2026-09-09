class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0                         # Left end of window
        window_sum = 0                   # Sum of current window
        min_len = float('inf')           # Store minimum length

        for right in range(len(nums)):   # Move right through array
            window_sum += nums[right]    # Add current element

            while window_sum >= target:  # If sum reaches target
                min_len = min(min_len, right - left + 1)  # Update minimum
                window_sum -= nums[left] # Remove left element
                left += 1                # Move left forward

        if min_len == float('inf'):      # No valid subarray found
            return 0                     # Return 0

        return min_len                   # Return minimum length