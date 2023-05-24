#
# @lc app=leetcode id=1488 lang=python3
#
# [1488] Avoid Flood in The City
#
# https://leetcode.com/problems/avoid-flood-in-the-city/description/
#
# algorithms
# Medium (26.12%)
# Likes:    1358
# Dislikes: 257
# Total Accepted:    31.1K
# Total Submissions: 117.2K
# Testcase Example:  '[1,2,3,4]'
#
# Your country has an infinite number of lakes. Initially, all the lakes are
# empty, but when it rains over the nth lake, the nth lake becomes full of
# water. If it rains over a lake that is full of water, there will be a flood.
# Your goal is to avoid floods in any lake.
#
# Given an integer array rains where:
#
#
# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake
# this day and dry it.
#
#
# Return an array ans where:
#
#
# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
#
#
# If there are multiple valid answers return any of them. If it is impossible
# to avoid flood return an empty array.
#
# Notice that if you chose to dry a full lake, it becomes empty, but if you
# chose to dry an empty lake, nothing changes.
#
#
# Example 1:
#
#
# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.
#
#
# Example 2:
#
#
# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another
# acceptable scenario.
#
#
# Example 3:
#
#
# Input: rains = [1,2,0,1,2]
# Output: []
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one
# lake in the third day.
# After that, it will rain over lakes [1,2]. It's easy to prove that no matter
# which lake you choose to dry in the 3rd day, the other one will flood.
#
#
#
# Constraints:
#
#
# 1 <= rains.length <= 10^5
# 0 <= rains[i] <= 10^9
#
#
#


# @lc code=start
from collections import deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """
        Solution 1: brute force

        use a dict to record full lakes with last day filled
        use a array to keep the days with no rain

        when there is rain for a full lake, find the smallest dry day
        that is after the previous filled day

        Time O(n^2) Space O(n)
        """

        def get_dry(i):
            # return the smallest after i from drys

            # the search can be optimized using binary search
            # but the `pop` operation still takes O(n)
            # so overall time still be O(n^2)
            for j, dry in enumerate(drys):
                if dry > i:
                    return drys.pop(j)
            return 0  # no dry day

        full = {}
        drys = []
        ans = [-1] * len(rains)
        for i in range(len(rains)):
            lake = rains[i]
            if lake > 0:
                if lake in full:
                    dry = get_dry(full[lake])
                    if dry == 0:
                        return []
                    else:
                        ans[dry] = lake
                full[lake] = i
            else:
                ans[i] = 1
                drys.append(i)
        return ans

        """
        Solution 2: Priority Queue (Balanced BST)

        to find the smallest dry day, we can use priority queue to
        optimize the search speed:
        O(logn) for insert, delete and search

        There is no easy way to implement this in Python. See java implementation.
        """


# @lc code=end
