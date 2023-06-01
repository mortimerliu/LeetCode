#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.33%)
# Likes:    7227
# Dislikes: 370
# Total Accepted:    597K
# Total Submissions: 1.5M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
#
# Example 1:
#
#
# Input: s = "aba"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer
        def helper(l, r, removed):
            while l < r:
                if s[l] != s[r]:
                    if removed:
                        return False
                    return helper(l + 1, r, True) or helper(l, r - 1, True)
                l += 1
                r -= 1
            return True

        return helper(0, len(s) - 1, False)


# @lc code=end
