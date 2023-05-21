#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
#
# algorithms
# Medium (32.88%)
# Likes:    2417
# Dislikes: 325
# Total Accepted:    69.5K
# Total Submissions: 214K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# You are given an array of events where events[i] = [startDayi, endDayi].
# Every event i starts at startDayi and ends at endDayi.
#
# You can attend an event i at any day d where startTimei <= d <= endTimei. You
# can only attend one event at any time d.
#
# Return the maximum number of events you can attend.
#
#
# Example 1:
#
#
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
#
#
# Example 2:
#
#
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 10^5
#
#
#


# @lc code=start
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Solution 1: Priority Queue

        Intuition: we want to attend the event starting earlier by the one
        starting later
        => sort events by start date
        Intuition: for events open concurrently, we want to first attend
        the one that ends earliest.
        => use a PQ to keep track of the earliest ending event

        O(nlogn)
        """

        n = len(events)
        events.sort()
        started = []
        res = day = i = 0
        while i < n or started:
            if i < n and day >= events[i][0]:
                heapq.heappush(started, events[i][1])
                i += 1
            else:
                while started and started[0] < day:
                    heapq.heappop(started)
                if started:
                    heapq.heappop(started)
                    res += 1
                    day += 1
                else:
                    day = events[i][0] if i < n else -1
        return res


# @lc code=end
