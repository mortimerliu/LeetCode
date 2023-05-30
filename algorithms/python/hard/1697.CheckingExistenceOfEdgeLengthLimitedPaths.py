#
# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
#
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
#
# algorithms
# Hard (50.32%)
# Likes:    1745
# Dislikes: 43
# Total Accepted:    45.5K
# Total Submissions: 72.1K
# Testcase Example:  '3\n[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]\n[[0,1,2],[0,2,5]]'
#
# An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
# [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
# Note that there may be multiple edges between two nodes.
#
# Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
# determine for each queries[j] whether there is a path between pj and qj such
# that each edge on the path has a distance strictly less than limitj .
#
# Return a boolean array answer, where answer.length == queries.length and the
# j^th value of answer is true if there is a path for queries[j] is true, and
# false otherwise.
#
#
# Example 1:
#
#
# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
# [[0,1,2],[0,2,5]]
# Output: [false,true]
# Explanation: The above figure shows the given graph. Note that there are two
# overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is
# less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with
# distances less than 5, thus we return true for this query.
#
#
# Example 2:
#
#
# Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
# [[0,4,14],[1,4,13]]
# Output: [true,false]
# Explanation: The above figure shows the given graph.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
# 1 <= edgeList.length, queries.length <= 10^5
# edgeList[i].length == 3
# queries[j].length == 3
# 0 <= ui, vi, pj, qj <= n - 1
# ui != vi
# pj != qj
# 1 <= disi, limitj <= 10^9
# There may be multiple edges between two nodes.
#
#
#


# @lc code=start


class DisjointSet:
    def __init__(self, nodes=None):
        self.groups = {}
        self.counts = {}
        # self._ncomps = 0
        if nodes:
            for node in nodes:
                self.insert(node)

    def insert(self, node):
        if node in self.groups:
            return False
        self.groups[node] = node
        self.counts[node] = 1
        # self._ncomps += 1
        return True

    def find(self, node):
        # w/ path compression
        grp = self.groups[node]
        if grp != node:
            self.groups[node] = self.find(grp)
        return self.groups[node]

    def union(self, node1, node2):
        # w/ union by count
        grp1, grp2 = self.find(node1), self.find(node2)
        if grp1 == grp2:
            return False
        if self.counts[grp1] < self.counts[grp2]:
            grp1, grp2 = grp2, grp1
        self.groups[grp2] = grp1
        self.counts[grp1] += self.counts[grp2]
        # self._ncomps -= 1
        return True

    # @property
    # def num_components(self):
    #     return self._ncomps


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        """
        Solution 1: Union-find / disjoint set
        """
        edgeList.sort(key=lambda x: x[2])
        queries = [(q[2], q, i) for i, q in enumerate(queries)]
        queries.sort()
        res = [False] * len(queries)
        ds = DisjointSet(list(range(n)))
        i = 0
        for _, (p, q, limit), j in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                ds.union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[j] = ds.find(p) == ds.find(q)

        return res


# @lc code=end
