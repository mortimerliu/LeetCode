#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (31.96%)
# Likes:    1632
# Dislikes: 422
# Total Accepted:    105.4K
# Total Submissions: 339.7K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# You are given an integer array deck where deck[i] represents the number
# written on the i^th card.
#
# Partition the cards into one or more groups such that:
#
#
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
#
#
# Return true if such partition is possible, or false otherwise.
#
#
# Example 1:
#
#
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#
#
# Example 2:
#
#
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Constraints:
#
#
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4
#
#
#


# @lc code=start
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Solution 1: Hashmap + GCA

        Count all the numbers in the deck and store them in a hashmap.
        Find the greatest common divisor of all the counts.

        Time:
        """

        def gca(a, b):
            """calcualte the greatest common divisor of a and b

            Time: O(log(min(a, b)))
            Space: O(1)
            """
            if b == 0:
                return a
            return gca(b, a % b)

        count = Counter(deck)
        curr_gcd = None
        for key in count:
            if curr_gcd is None:
                curr_gcd = count[key]
            else:
                curr_gcd = gca(curr_gcd, count[key])
            if curr_gcd == 1:
                return False
        return True


# @lc code=end
