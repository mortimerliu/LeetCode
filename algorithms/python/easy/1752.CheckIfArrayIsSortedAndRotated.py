#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
#
# algorithms
# Easy (49.33%)
# Likes:    1794
# Dislikes: 81
# Total Accepted:    91.3K
# Total Submissions: 182.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# Given an array nums, return true if the array was originally sorted in
# non-decreasing order, then rotated some number of positions (including zero).
# Otherwise, return false.
#
# There may be duplicates in the original array.
#
# Note: An array A rotated by x positions results in an array B of the same
# length such that A[i] == B[(i+x) % A.length], where % is the modulo
# operation.
#
#
# Example 1:
#
#
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of
# value 3: [3,4,5,1,2].
#
#
# Example 2:
#
#
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make
# nums.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#


# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Solution 1: check every position
        O(n^2)
        """

        """
        Solution 2: from two ends
        """
        # n = len(nums)
        # left = 0
        # while left < n - 1 and nums[left] <= nums[left + 1]:
        #     left += 1
        # if left == n - 1:
        #     return True
        # right = n - 1
        # while right > 0 and nums[right - 1] <= nums[right]:
        #     right -= 1
        # if left + 1 < right or nums[0] < nums[-1]:
        #     return False
        # return True

        """
        Solution 3: treat the array as a circle and consider nums[0] as
        the next element of nums[-1]
        then we can only have at most 1 time of the case where
        nums[i] > nums[i-1]
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False
        return True


# @lc code=end
