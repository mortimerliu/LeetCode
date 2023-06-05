#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (32.41%)
# Likes:    25382
# Dislikes: 1492
# Total Accepted:    2.4M
# Total Submissions: 7.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Solution 1: brute force
        check every substring TC O(N^3)

        Solution 2: dp

        dp(i, length) = whether s[i:i+length] is a palindrome
        dp(i, length) = dp(i+1, lenght-2) and s[i] == s[i+length-1]
        dp(i, 0) = dp(i, 1) = True

        Solution 3: center
        see java
        """
        n = len(s)
        prev2 = [True] * n
        prev1 = [True] * n
        ans = (1, 0)
        for length in range(2, n + 1):
            cur = [False] * n
            for i in range(n - length + 1):
                cur[i] = prev2[i + 1] and s[i] == s[i + length - 1]
                if cur[i]:
                    ans = (length, i)
            prev2 = prev1
            prev1 = cur
        return s[ans[1] : ans[1] + ans[0]]


# @lc code=end
