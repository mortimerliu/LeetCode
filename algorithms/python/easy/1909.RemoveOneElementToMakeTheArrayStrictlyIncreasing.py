#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/
#
# algorithms
# Easy (26.05%)
# Likes:    996
# Dislikes: 287
# Total Accepted:    46.6K
# Total Submissions: 178K
# Testcase Example:  '[1,2,10,5,7]'
#
# Given a 0-indexed integer array nums, return true if it can be made strictly
# increasing after removing exactly one element, or false otherwise. If the
# array is already strictly increasing, return true.
#
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index
# (1 <= i < nums.length).
#
#
# Example 1:
#
#
# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.
#
#
# Example 2:
#
#
# Input: nums = [2,3,1,2]
# Output: false
# Explanation:
# [3,1,2] is the result of removing the element at index 0.
# [2,1,2] is the result of removing the element at index 1.
# [2,3,2] is the result of removing the element at index 2.
# [2,3,1] is the result of removing the element at index 3.
# No resulting array is strictly increasing, so return false.
#
# Example 3:
#
#
# Input: nums = [1,1,1]
# Output: false
# Explanation: The result of removing any element is [1,1].
# [1,1] is not strictly increasing, so return false.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
#
#
#


# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        ## Solution 1: Brute Force
        ## for i in range(n), remove i, see if all increasing. if any,
        ## return True; otherwise, return False.

        ## Solution 2: Two increasing arrays from left and right
        # n = len(nums)
        # if n <= 2:
        #     return True
        # left, right = 0, n - 1
        # while left + 1 < n and nums[left] < nums[left + 1]:
        #     left += 1
        # if left == n - 1:
        #     return True

        # while right - 1 >= 0 and nums[right] > nums[right - 1]:
        #     right -= 1

        # if left + 1 < right:
        #     return False

        # if (
        #     left == 0
        #     or nums[left - 1] < nums[right]
        #     or right == n - 1
        #     or nums[left] < nums[right + 1]
        # ):
        #     return True

        # return False

        ## Solution 3: from left to right
        removed = False
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] < nums[i]:
                cur = i
            else:
                if removed:
                    return False
                else:
                    removed = True
                    if cur == 0 or nums[cur - 1] < nums[i]:
                        cur = i
        return True


# @lc code=end
