#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (43.71%)
# Likes:    6881
# Dislikes: 7096
# Total Accepted:    2M
# Total Submissions: 4.4M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ascii: 0 - 48; A - 65; a - 97
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                vl = ord(s[l])
                if vl >= 97:
                    vl -= 32
                vr = ord(s[r])
                if vr >= 97:
                    vr -= 32
                if vl != vr:
                    return False
                l += 1
                r -= 1
        return True


# @lc code=end
