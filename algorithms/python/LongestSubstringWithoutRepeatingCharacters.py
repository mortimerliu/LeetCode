"""
[Medium] 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3

Example 2:

Input: s = "pwwkew"
Output: 3

Constraints:

* 0 <= s.length <= 5 * 104
* s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    """
    Time: O(n)
    Space: O(m) where m is the size of character set
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = -1
        lastIndex = {}

        for end, char in enumerate(s):
            start = max(start, lastIndex.get(char, -1))
            ans = max(ans, end - start)
            lastIndex[char] = end

        return ans
