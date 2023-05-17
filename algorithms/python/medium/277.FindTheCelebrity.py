#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#
# https://leetcode.com/problems/find-the-celebrity/description/
#
# algorithms
# Medium (46.54%)
# Likes:    2663
# Dislikes: 255
# Total Accepted:    247.9K
# Total Submissions: 531.1K
# Testcase Example:  '[[1,1,0],[0,1,0],[1,1,1]]'
#
# Suppose you are at a party with n people labeled from 0 to n - 1 and among
# them, there may exist one celebrity. The definition of a celebrity is that
# all the other n - 1 people know the celebrity, but the celebrity does not
# know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not
# one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to
# get information about whether A knows B. You need to find out the celebrity
# (or verify there is not one) by asking as few questions as possible (in the
# asymptotic sense).
#
# You are given a helper function bool knows(a, b) that tells you whether a
# knows b. Implement a function int findCelebrity(n). There will be exactly one
# celebrity if they are at the party.
#
# Return the celebrity's label if there is a celebrity at the party. If there
# is no celebrity, return -1.
#
#
# Example 1:
#
#
# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1
# means person i knows person j, otherwise graph[i][j] = 0 means person i does
# not know person j. The celebrity is the person labeled as 1 because both 0
# and 2 know him but 1 does not know anybody.
#
#
# Example 2:
#
#
# Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
# Output: -1
# Explanation: There is no celebrity.
#
#
#
# Constraints:
#
#
# n == graph.length == graph[i].length
# 2 <= n <= 100
# graph[i][j] is 0 or 1.
# graph[i][i] == 1
#
#
#
# Follow up: If the maximum number of allowed calls to the API knows is 3 * n,
# could you find a solution without exceeding the maximum number of calls?
#
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Solution 1: Brute Force
        check every i
        Time O(n^2)
        """

        """
        Solution 2: get the most informatin gain
        
        For `knows(a, b)`:
            if the result is True, then a is not the celebrity
            if the result if False, then b is not the celebrity
        """
        # Keep a set with people def not the celebrity
        # impossible = set()
        # for i in range(n):
        #     if i in impossible:
        #         continue
        #     for j in range(n):
        #         if i != j:
        #             if knows(j, i):
        #                 impossible.add(j)
        #                 if knows(i, j):
        #                     impossible.add(i)
        #                     break
        #             else:
        #                 impossible.add(i)
        #                 break
        #     else:
        #         return i
        # return -1

        # rule out n-1 people in O(n)
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # since candidate knows i, candidate is not celebrity
                # i is the next candidate
                candidate = i
            # else: since candidate doesn't know i, i is not the celebrity
            # keep candidate as is
        # at this point, candidate is the only one possbile
        # for all i > candidate, knows(candidate, i) = False
        # otherwise, cancidate will be that i

        # just need to confirm if candidate is really the celebrity
        for i in range(n):
            if candidate == i:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate
        # one improvement is, to make knows cached
        # @lru_cache(maxsize=None)
        # def cached_knows(a, b):
        #     return knows(a, b)


# @lc code=end
