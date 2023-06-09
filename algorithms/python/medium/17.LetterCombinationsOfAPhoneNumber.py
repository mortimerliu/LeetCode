#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.71%)
# Likes:    15195
# Dislikes: 847
# Total Accepted:    1.6M
# Total Submissions: 2.8M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            digit = int(digits)
            offset = (digit - 2) * 3
            if digit in (8, 9):
                offset += 1
            n = 3
            if digit in (7, 9):
                n = 4
            return [chr(ord("a") + offset + i) for i in range(n)]
        else:
            res = []
            for a in self.letterCombinations(digits[0]):
                for b in self.letterCombinations(digits[1:]):
                    res.append(a + b)
            return res


# @lc code=end
