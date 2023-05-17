#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (49.08%)
# Likes:    40464
# Dislikes: 1302
# Total Accepted:    8.3M
# Total Submissions: 17M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Solution 1: Brute Force
        check every pair - Time O(n^2)
        """

        """
        Solution 2: Sort first
        """
        # nums_sorted = sorted([(i, n) for i, n in enumerate(nums)], key=lambda x: x[1])
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     sum_ = nums_sorted[i][1] + nums_sorted[j][1]
        #     if sum_ == target:
        #         return nums_sorted[i][0], nums_sorted[j][0]
        #     elif sum_ < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return -1, -1

        """
        Solution 3: HashMap
        """
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return i, seen[target - n]
            else:
                seen[n] = i
        return -1, -1


# @lc code=end
