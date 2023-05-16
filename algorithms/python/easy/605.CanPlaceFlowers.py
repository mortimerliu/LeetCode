#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (32.89%)
# Likes:    4931
# Dislikes: 837
# Total Accepted:    433.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and
# false otherwise.
#
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
#
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#
#
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Solution 1: count 0's  and place as dense as possible

        for m consecutive 0's, we can place (m-1)//2 flowers at most
        """
        # m, k = len(flowerbed), 1  # put zero on left end
        # for i in range(m + 1):
        #     if i == m or flowerbed[i] == 0:
        #         k += 1
        #     if i == m or flowerbed[i] == 1:
        #         n -= max(k - 1, 0) // 2
        #         if n <= 0:
        #             return True
        #         k = 0
        # return False

        # same idea, use two pointers
        # padding both ends with 0's
        m = len(flowerbed)
        left = -1
        for i in range(m + 1):
            if i == m or flowerbed[i] == 1:
                if i == m:
                    i += 1
                n -= (i - left - 1) // 2
                if n <= 0:
                    return True
                left = i + 1
        return False

        # use strings - slow
        # padding both ends with 0's
        # string = "0{}0".format("".join([str(i) for i in flowerbed]))
        # segment = string.split("1")
        # capacity = sum(max(len(seg) - 1, 0) // 2 for seg in segment)
        # return capacity >= n


# @lc code=end
