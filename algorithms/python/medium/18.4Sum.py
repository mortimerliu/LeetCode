#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (36.42%)
# Likes:    9282
# Dislikes: 1100
# Total Accepted:    740.6K
# Total Submissions: 2.1M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k, i):
            if k == 2:
                return twoSum(nums, target, i)

            avg = target // k

            res = []
            if i >= len(nums) or (avg < nums[i] or nums[-1] < avg):
                return res

            for j in range(i, len(nums)):
                if (j == i or nums[j - 1] != nums[j]) and nums[j] <= avg:
                    for subset in kSum(nums, target - nums[j], k - 1, j + 1):
                        res.append([nums[j]] + subset)
            return res

        def twoSum(nums, target, i):
            res = []
            seen = set()
            for j in range(i, len(nums)):
                if not res or res[-1][-1] != nums[j]:
                    if target - nums[j] in seen:
                        res.append([target - nums[j], nums[j]])
                seen.add(nums[j])
            return res

        nums.sort()
        return kSum(nums, target, 4, 0)


# @lc code=end
