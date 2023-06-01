#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (40.82%)
# Likes:    14029
# Dislikes: 3974
# Total Accepted:    2.4M
# Total Submissions: 5.9M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # this can be solved using divide & conquer, binary search
        if not strs:
            return ""
        all_same = True
        i = 0
        while i < len(strs[0]):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    all_same = False
            if not all_same:
                break
            i += 1
        return strs[0][:i]


# @lc code=end
