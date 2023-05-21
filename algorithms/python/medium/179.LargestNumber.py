#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (34.07%)
# Likes:    6927
# Dislikes: 566
# Total Accepted:    395.1K
# Total Submissions: 1.1M
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of
# an integer.
#
#
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        First thing is that this question is actually asking to sort the nums
        in a special way: maximize the concatenated number

        To achieve this, for pairwise comparision during sorting of a and b,
        checking str(a) + str(b) < str(b) + str(a) instead of a < b,

        this comparator is transitive:
            if a > b, b > c, then a > c
        """

        class LargerNumKey(str):
            def __lt__(x, y):
                return x + y > y + x

        strings = [str(n) for n in nums]
        strings.sort(key=LargerNumKey)
        largest_num = "".join(strings)

        return "0" if largest_num[0] == "0" else largest_num


# @lc code=end
