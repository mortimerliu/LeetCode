#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (30.49%)
# Likes:    7614
# Dislikes: 323
# Total Accepted:    312.6K
# Total Submissions: 1M
# Testcase Example:  '"1432219"\n3'
#
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
#
#
# Example 1:
#
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
#
# Example 2:
#
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
#
# Example 3:
#
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
#
#
#
# Constraints:
#
#
# 1 <= k <= num.length <= 10^5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Solution 1: mono stack - greedy
        - observation 1: given two sequences of digit of the same length,
          it is the leftmost distinct digits that determine the superior
          of the two numbers
        - observation 2: becuase of 1), for a sequence of digits [D1D2...DN],
          if D1 > D2, we should always remove D1, as D1D2..DN > D2D3..DN

        we can use a non-decreasing mono stack to achieve this. one
        constraint is that we can only remove k digits
        """
        if len(num) <= k:
            return "0"
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        i = 0
        while i < len(stack) - k - 1 and stack[i] == "0":
            i += 1
        return "".join(stack[i : len(stack) - k])


# @lc code=end
