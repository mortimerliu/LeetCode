#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (32.33%)
# Likes:    25651
# Dislikes: 2310
# Total Accepted:    2.7M
# Total Submissions: 8.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Solution 1: brute force O(n^3)
        """

        """
        Solution 2: Hashmap with twoSum
        
        -nums[i] = nums[j] + nums[k]
        
        use set to avoid duplicates
        
        O(n^2)
        """

        # Instead of re-populating a hashset every time in the inner loop,
        # we can use a hashmap and populate it once. Values in the hashmap
        # will indicate whether we have encountered that element in the
        # current iteration.
        def twoSum(nums, i, target, ans) -> None:
            for k in range(i, len(nums)):
                if target - nums[k] in seen and seen[target - nums[k]] == i:
                    ans.add(tuple(sorted([-target, nums[k], target - nums[k]])))
                seen[nums[k]] = i

        seen = {}
        ans = set()
        dups = set()
        for i in range(len(nums) - 2):
            if nums[i] not in dups:
                dups.add(nums[i])
                twoSum(nums, i + 1, -nums[i], ans)
        return [list(a) for a in ans]

        """
        Solution 3: sort and two pointers
        """


# @lc code=end
