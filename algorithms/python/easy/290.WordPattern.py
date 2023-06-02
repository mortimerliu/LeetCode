#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (40.43%)
# Likes:    6288
# Dislikes: 756
# Total Accepted:    528.9K
# Total Submissions: 1.3M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Solution 1: two hash map

        Solution 2: one hash map
            if s follows pattern, then first occurrence of each word of
            should match the first occurrence of each char in pattern
            see java implementation
        """
        p2w = {}
        w2p = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for p, word in zip(pattern, words):
            if (p in p2w and word != p2w[p]) or (word in w2p and w2p[word] != p):
                return False
            p2w[p] = word
            w2p[word] = p
        return True


# @lc code=end
