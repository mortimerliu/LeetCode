#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (37.16%)
# Likes:    15231
# Dislikes: 4135
# Total Accepted:    1M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
#
#
# For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
#
#
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
#
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
#
#
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
#
#
# Example 3:
#
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Solution:
        Step 1: starting from end, find index i such that nums[i] is the
        longest non-decreasing array
           i
        3, 4, 6, 5, 1

        Step 2: from i+1 to n-1, find j: min(j) st. nums[j] > nums[i]
           i     j
        3, 4, 6, 5, 1

        Step 3: modify inplace: swap i and j, sort nums[i+1:]
        3, 5, 6, 4, 1 -> 3, 5, 1, 4, 6

        if nums is all non-decreasing, then it's the following case:
        [3,2,1] -> [1,2,3]
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i:
            # find j can be optimized with a binary search
            j = i
            while j < n - 1 and nums[j + 1] > nums[i - 1]:
                j += 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        l, r = i, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# @lc code=end
