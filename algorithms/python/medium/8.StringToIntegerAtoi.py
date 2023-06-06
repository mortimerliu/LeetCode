#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (16.63%)
# Likes:    3318
# Dislikes: 10218
# Total Accepted:    1.3M
# Total Submissions: 7.6M
# Testcase Example:  '"42"'
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-'
# or '+'. Read this character in if it is either. This determines if the final
# result is negative or positive respectively. Assume the result is positive if
# neither is present.
# Read in next the characters until the next non-digit character or the end of
# the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
# digits were read, then the integer is 0. Change the sign as necessary (from
# step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -2^31 should be clamped to -2^31, and integers greater
# than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
#
#
# Note:
#
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of
# the string after the digits.
#
#
#
# Example 1:
#
#
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the
# current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# ⁠        ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# ⁠        ^
# Step 3: "42" ("42" is read in)
# ⁠          ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
#
#
# Example 2:
#
#
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
# ⁠           ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
# ⁠            ^
# Step 3: "   -42" ("42" is read in)
# ⁠              ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
#
#
# Example 3:
#
#
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "4193 with words" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next
# character is a non-digit)
# ⁠            ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ',
# '+', '-', and '.'.
#
#
#

# @lc code=start
from enum import Enum

State = Enum("State", ["q0", "q1", "q2", "qd"])


class StateMachine:
    def __init__(self):
        self.state: State = State.q0
        self.sign: int = 1
        self.value: int = 0
        self.MAX_VALUE = pow(2, 31) - 1  # MAX_VALUE = 2147483647
        self.MIN_VALUE = -pow(2, 31)  # MIN_VALUE = -2147483648
        self.LIMIT = self.MAX_VALUE // 10

    def to_q1(self, char: str):
        if char == "-":
            self.sign = -1
        self.state = State.q1

    def to_q2(self, char: str):
        digit = ord(char) - ord("0")
        self.state = State.q2
        self.append_digit(digit)

    def to_qd(self):
        self.state = State.qd

    def append_digit(self, digit: int):
        if self.value > self.LIMIT or (self.value == self.LIMIT and digit > 7):
            if self.sign == 1:
                self.value = self.MAX_VALUE
            else:
                self.value = self.MIN_VALUE
                self.sign = 1
            self.to_qd()
        else:
            self.value = self.value * 10 + digit

    def transition(self, char: str):
        if self.state == State.q0:
            if char in "+-":
                self.to_q1(char)
            elif char.isdigit():
                self.to_q2(char)
            elif char != " ":
                self.to_qd()
        elif self.state in (State.q1, State.q2):
            if char.isdigit():
                self.to_q2(char)
            else:
                self.to_qd()

    def get_value(self):
        return self.sign * self.value


class Solution:
    def myAtoi(self, s: str) -> int:
        # MAX_VALUE = 2147483647
        # MIN_VALUE = -2147483648

        # i = 0
        # n = len(s)
        # while i < n and s[i] == " ":
        #     i += 1

        # ops = {
        #     "+": lambda x, y: x * 10 + y,
        #     "-": lambda x, y: x * 10 - y,
        # }
        # largers = {
        #     "+": lambda x: x > MAX_VALUE,
        #     "-": lambda x: x < MIN_VALUE,
        # }
        # limits = {
        #     "+": MAX_VALUE,
        #     "-": MIN_VALUE,
        # }
        # if i < n and s[i] in "+-":
        #     op = ops[s[i]]
        #     larger = largers[s[i]]
        #     limit = limits[s[i]]
        #     i += 1
        # else:
        #     op = ops["+"]
        #     larger = largers["+"]
        #     limit = limits["+"]

        # value = 0
        # while i < n and s[i].isdigit():
        #     value = op(value, int(s[i]))
        #     if larger(value):
        #         return limit
        #     i += 1
        # return value
        """
        Solution: State Machine
        """
        Q: StateMachine = StateMachine()
        for char in s:
            Q.transition(char)
            if Q.state == State.qd:
                break
        return Q.get_value()


# @lc code=end
