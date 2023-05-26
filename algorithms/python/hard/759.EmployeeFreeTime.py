#
# @lc app=leetcode id=759 lang=python3
#
# [759] Employee Free Time
#
# https://leetcode.com/problems/employee-free-time/description/
#
# algorithms
# Hard (71.73%)
# Likes:    1749
# Dislikes: 120
# Total Accepted:    132.7K
# Total Submissions: 184.7K
# Testcase Example:  '[[[1,2],[5,6]],[[1,3]],[[4,10]]]'
#
# We are given a list schedule of employees, which represents the working time
# for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals
# are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free
# time for all employees, also in sorted order.
#
# (Even though we are representing Intervals in the form [x, y], the objects
# inside are Intervals, not lists or arrays. For example, schedule[0][0].start
# = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we
# wouldn't include intervals like [5, 5] in our answer, as they have zero
# length.
#
#
# Example 1:
#
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
#
#
# Example 2:
#
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
#
#
#
# Constraints:
#
#
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8
#
#
#

# @lc code=start
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        """
        Solution 1: flatten, sort, merge, find gap
        """

        """
        Solution 2: line sweep

        O(nlogn)
        """
        # events = []
        # for emp in schedule:
        #     for interval in emp:
        #         events.append((interval.start, -1))
        #         events.append((interval.end, 1))
        # events.sort()

        # count = 0
        # free = []
        # for i, (time, cnt) in enumerate(events):
        #     if i > 0 and count == 0:
        #         free.append(Interval(events[i - 1][0], time))
        #     count -= cnt
        # return free

        # better implementation
        intervals = [interval for emp in schedule for interval in emp]
        intervals.sort(key=lambda x: x.start)

        free = []
        end = intervals[0].end
        for interval in intervals:
            if end < interval.start:
                free.append(Interval(end, interval.start))
            end = max(end, interval.end)
        return free


# @lc code=end
