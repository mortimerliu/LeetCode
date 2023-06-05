#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.80%)
# Likes:    34284
# Dislikes: 1503
# Total Accepted:    4.5M
# Total Submissions: 13.4M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        left = 0
        seen = {}
        ans = 0
        for right, c in enumerate(s):
            if c in seen:
                left = max(left, seen[c] + 1)
            ans = max(ans, right - left + 1)
            seen[c] = right
        return ans


# @lc code=end
