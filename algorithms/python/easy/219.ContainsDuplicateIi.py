#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (42.30%)
# Likes:    4836
# Dislikes: 2616
# Total Accepted:    670.3K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Solution 1: Brute Force - check all subarrays with length k
        Time Complexity: O(nk) Space O(1)
        """
        """
        Solution 2: hashSet
        Time O(n) Space O(min(n,k))
        """
        if k == 0:
            return False

        seen = set()
        for i, v in enumerate(nums):
            if v in seen:
                return True
            if i >= k:
                seen.remove(nums[i - k])
            seen.add(v)
        return False

        # hashmap
        # hashmap = {}
        # for n in range(len(nums)):
        #     if nums[n] in hashmap and n-hashmap[nums[n]]<=k :
        #         return True
        #     else:
        #         hashmap[nums[n]] = n

        # return False


# @lc code=end
