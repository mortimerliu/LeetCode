#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (40.91%)
# Likes:    3259
# Dislikes: 173
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '"Hello World"'
#
# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
# Example 1:
#
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
#
# Example 2:
#
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
#
# Example 3:
#
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
#
#
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # find last non-space
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        # find last space before last non-space
        j = i - 1
        while j >= 0 and s[j] != " ":
            j -= 1
        return i - j


# @lc code=end
