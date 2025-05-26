class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2  # Placeholder for you to implement the solution


# Test cases
test_cases = [
    # Example 1
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),

    # Example 2
    ([1], 1),

    # Example 3
    ([5, 4, -1, 7, 8], 23),

    # Additional test cases
    ([-1, -2, -3, -4], -1),  # Single negative number
    ([2, 1, 3, 4], 10),  # All positive numbers
    ([0, 0, 0, 0], 0),  # All zeros
    ([-2, -1, -3, 4, -1, 2, 1, -5, 4], 6),  # Subarray with both positive and negative values
    ([-2, 1, -3, 4, -1, 2, 1], 6)  # Another example of mix of positive and negative numbers
]

# Running the test cases
sol = Solution()
for i, (nums, expected) in enumerate(test_cases):
    result = sol.maxSubArray(nums)
    print(f"Test case {i + 1}: {'Pass' if result == expected else 'Fail'}")
    print(f"Expected: {expected}, Got: {result}")