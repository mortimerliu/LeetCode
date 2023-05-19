#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (28.55%)
# Likes:    4714
# Dislikes: 460
# Total Accepted:    393.1K
# Total Submissions: 1.4M
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given an integer array nums and an integer k, return true if nums has a good
# subarray or false otherwise.
#
# A good subarray is a subarray where:
#
#
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
#
#
# Note that:
#
#
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n
# * k. 0 is always a multiple of k.
#
#
#
# Example 1:
#
#
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
# to 6.
#
#
# Example 2:
#
#
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
# elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
#
# Example 3:
#
#
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Solution 1: brute force
        check every subarray nums[i:j]
        O(n^3)
        """

        """
        Solution 2: prefix array - TLE
        sum(nums[i:j]) = sum(nums[j]) - sum(nums[i]) 
        """
        # n = len(nums)
        # if n < 2:
        #     return False
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]
        # for i in range(n + 1):
        #     for j in range(n + 1):
        #         if i + 1 < j and (prefix[j] - prefix[i]) % k == 0:
        #             return True
        # return False

        """
        Solution 3: 
        sum(nums[i:j]) = sum(nums[j]) - sum(nums[i])
        if sum(nums[i:j]) % k == 0
        then sum(nums[j]) % k == sum(nums[i]) % k
        
        thus we can convert the question to: find if there are two prefix sum
        that has same remainder.
        
        one trick is that, given the length of two requirement, the two prefix
        sum cannot be contiguous. We can use a hashmap to do this. 
        """
        if len(nums) < 2:
            return False

        prev_remainder = 0
        remainder = {0: -1}
        for i in range(len(nums)):
            prev_remainder = (prev_remainder + nums[i]) % k
            if prev_remainder in remainder:
                if remainder[prev_remainder] + 1 < i:
                    return True
            else:
                remainder[prev_remainder] = i
        return False


# @lc code=end
