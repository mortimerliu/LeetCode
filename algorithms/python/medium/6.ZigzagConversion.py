#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (43.19%)
# Likes:    6214
# Dislikes: 12384
# Total Accepted:    1M
# Total Submissions: 2.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        n = len(s)
        step = 2 * numRows - 2
        for row in range(numRows):
            first = row
            while first < n:
                res.append(s[first])
                second = first + 2 * (numRows - row) - 2
                if 0 < row < numRows - 1 and second < n:
                    res.append(s[second])
                first += step
        return "".join(res)


# @lc code=end
