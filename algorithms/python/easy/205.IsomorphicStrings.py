#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (42.61%)
# Likes:    6799
# Dislikes: 1485
# Total Accepted:    901.7K
# Total Submissions: 2.1M
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
#
#
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # same as 290
        if len(s) != len(t):
            return False
        maps = {}
        for i, (sc, tc) in enumerate(zip(s, t)):
            if maps.setdefault(f"s_{sc}", i) != maps.setdefault(f"t_{tc}", i):
                return False
        return True


# @lc code=end
