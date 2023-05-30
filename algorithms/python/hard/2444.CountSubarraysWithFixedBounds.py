#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
#
# algorithms
# Hard (43.15%)
# Likes:    2155
# Dislikes: 46
# Total Accepted:    56.9K
# Total Submissions: 92K
# Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
#
# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following
# conditions:
#
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
#
#
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
# possible subarrays.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6
#
#
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # sliding window / two pointers
        # TC: O(n)
        # count = 0
        # n = len(nums)
        # i = min_idx = max_idx = -1
        # for j in range(n + 1):
        #     num = nums[j] if j < n else maxK + 1
        #     if num <= minK or num >= maxK:
        #         if min_idx >= 0 and max_idx >= 0:
        #             left = min(min_idx, max_idx)
        #             right = max(min_idx, max_idx)
        #             count += (j - right) * (left - i)
        #         if num < minK or num > maxK:
        #             i = j
        #             min_idx = max_idx = -1
        #         if num == minK:
        #             min_idx = max(min_idx, j)
        #         if num == maxK:
        #             max_idx = max(max_idx, j)
        # return count

        # better implementation
        count = 0
        i = min_idx = max_idx = -1
        for j, num in enumerate(nums):
            if num < minK or num > maxK:
                i = j
            if num == minK:
                min_idx = max(min_idx, j)
            if num == maxK:
                max_idx = max(max_idx, j)
            count += max(0, min(min_idx, max_idx) - i)
        return count


# @lc code=end
