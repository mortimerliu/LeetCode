#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (34.83%)
# Likes:    3789
# Dislikes: 549
# Total Accepted:    379.7K
# Total Submissions: 1.1M
# Testcase Example:  '1'
#
# Given an integer columnNumber, return its corresponding column title as it
# appears in an Excel sheet.
#
# For example:
#
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
#
# Example 1:
#
#
# Input: columnNumber = 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: columnNumber = 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: columnNumber = 701
# Output: "ZY"
#
#
#
# Constraints:
#
#
# 1 <= columnNumber <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # subtract 1: though this is base 26 numbering system,
        # the digit is 1 to 26 instead of 0 to 25
        # thus, at every iteration, we minus 1 to convert the last digit
        # from 1...26 to 0...25

        # name = ""
        # while columnNumber > 0:
        #     r = columnNumber % 26
        #     if not r:
        #         r += 26
        #     name = chr(64 + r) + name
        #     columnNumber = (columnNumber - r) // 26
        # return name

        name = ""
        while columnNumber > 0:
            columnNumber -= 1
            name = chr(65 + columnNumber % 26) + name
            columnNumber //= 26
        return name


# @lc code=end
