#
# @lc app=leetcode id=2047 lang=python3
#
# [2047] Number of Valid Words in a Sentence
#
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/
#
# algorithms
# Easy (29.51%)
# Likes:    239
# Dislikes: 705
# Total Accepted:    22.3K
# Total Submissions: 76.7K
# Testcase Example:  '"cat and  dog"'
#
# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'),
# hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only.
# Each sentence can be broken down into one or more tokens separated by one or
# more spaces ' '.
#
# A token is a valid word if all three of the following are true:
#
#
# It only contains lowercase letters, hyphens, and/or punctuation (no
# digits).
# There is at most one hyphen '-'. If present, it must be surrounded by
# lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
# There is at most one punctuation mark. If present, it must be at the end of
# the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not
# valid).
#
#
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
#
# Given a string sentence, return the number of valid words in sentence.
#
#
# Example 1:
#
#
# Input: sentence = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".
#
#
# Example 2:
#
#
# Input: sentence = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.
#
#
# Example 3:
#
#
# Input: sentence = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob",
# "are", and "playing".
# "stone-game10" is invalid because it contains digits.
#
#
#
# Constraints:
#
#
# 1 <= sentence.length <= 1000
# sentence only contains lowercase English letters, digits, ' ', '-', '!', '.',
# and ','.
# There will be at least 1 token.
#
#
#


# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        is_valid = True
        n = len(sentence)
        count = 0
        has_hypen = False
        for i in range(n + 1):
            char = sentence[i] if i < n else " "
            if char == " ":
                if is_valid and (i > 0 and sentence[i - 1] != " "):
                    count += 1
                is_valid = True
                has_hypen = False
            elif char in "!.," and is_valid:
                is_valid = i + 1 == n or sentence[i + 1] == " "
            elif "0" <= char <= "9":
                is_valid = False
            elif char == "-" and is_valid:
                is_valid = not has_hypen and (
                    i > 0
                    and i + 1 < n
                    and "a" <= sentence[i - 1] <= "z"
                    and "a" <= sentence[i + 1] <= "z"
                )
                has_hypen = True
        return count


# @lc c`ode=end
