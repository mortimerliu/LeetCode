#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (34.66%)
# Likes:    259
# Dislikes: 531
# Total Accepted:    35.2K
# Total Submissions: 101K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to the
# y-axis that reflects the given points symmetrically.
#
# In other words, answer whether or not if there exists a line that after
# reflecting all points over the given line, the original points' set is the
# same as the reflected ones.
#
# Note that there can be repeated points.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[-1,1]]
# Output: true
# Explanation: We can choose the line x = 0.
#
#
# Example 2:
#
#
# Input: points = [[1,1],[-1,-1]]
# Output: false
# Explanation: We can't choose a line.
#
#
#
# Constraints:
#
#
# n == points.length
# 1 <= n <= 10^4
# -10^8 <= points[i][j] <= 10^8
#
#
#
# Follow up: Could you do better than O(n^2)?
#
#


# @lc code=start
from collections import defaultdict


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        """
        Solution 1: group and sort

        group points by y, sort by x per group, use two pointers to check
        if there is a x such that x_low + x_high = 2x holds true for all groups

        O(nlogn) - dominated by sort
        """

        """
        Solution 2: group and check distance pairs using hashmap (find a 
        candidate x first)
        """
        # if len(points) <= 1:
        #     return True
        # groups = defaultdict(set)
        # for x, y in points:
        #     groups[y].add(x)

        # ref_x = (min(groups[y]) + max(groups[y])) / 2
        # for xs in groups.values():
        #     waiting = defaultdict(int)
        #     for x in xs:
        #         dist = x - ref_x
        #         if dist == 0:
        #             continue
        #         if waiting[-dist] > 0:
        #             waiting[-dist] -= 1
        #         else:
        #             waiting[dist] += 1
        #     if sum(waiting.values()) > 0:
        #         return False
        # return True

        # better implementation
        # if the answer is true, the x_min and x_max must come from the same
        # y group, thus we can just do min and max from all points
        # thus we can do group and check in one run
        x_min, x_max = float("inf"), float("-inf")
        points_set = set()
        for x, y in points:
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            points_set.add((x, y))
        total = x_min + x_max

        for x, y in points:
            complement = total - x
            if (complement, y) not in points_set:
                return False
        return True


# @lc code=end
