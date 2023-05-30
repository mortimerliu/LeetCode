/*
 * @lc app=leetcode id=1697 lang=java
 *
 * [1697] Checking Existence of Edge Length Limited Paths
 *
 * https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
 *
 * algorithms
 * Hard (50.32%)
 * Likes:    1745
 * Dislikes: 43
 * Total Accepted:    45.5K
 * Total Submissions: 72.1K
 * Testcase Example:  '3\n[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]\n[[0,1,2],[0,2,5]]'
 *
 * An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
 * [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
 * Note that there may be multiple edges between two nodes.
 *
 * Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
 * determine for each queries[j] whether there is a path between pj and qj such
 * that each edge on the path has a distance strictly less than limitj .
 *
 * Return a boolean array answer, where answer.length == queries.length and the
 * j^th value of answer is true if there is a path for queries[j] is true, and
 * false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
 * [[0,1,2],[0,2,5]]
 * Output: [false,true]
 * Explanation: The above figure shows the given graph. Note that there are two
 * overlapping edges between 0 and 1 with distances 2 and 16.
 * For the first query, between 0 and 1 there is no path where each distance is
 * less than 2, thus we return false for this query.
 * For the second query, there is a path (0 -> 1 -> 2) of two edges with
 * distances less than 5, thus we return true for this query.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
 * [[0,4,14],[1,4,13]]
 * Output: [true,false]
 * Explanation: The above figure shows the given graph.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= n <= 10^5
 * 1 <= edgeList.length, queries.length <= 10^5
 * edgeList[i].length == 3
 * queries[j].length == 3
 * 0 <= ui, vi, pj, qj <= n - 1
 * ui != vi
 * pj != qj
 * 1 <= disi, limitj <= 10^9
 * There may be multiple edges between two nodes.
 *
 *
 */

// @lc code=start

import java.util.*;

class DisjointSet {
    private int[] groups;
    private int[] rank;

    public DisjointSet(int size) {
        groups = new int[size];
        for (int i = 0; i < size; i++) {
            groups[i] = i;
        }
        rank = new int[size];
    }

    public int find(int node) {
        int grp = groups[node];
        if (grp != node) {
            groups[node] = find(grp);
        }
        return groups[node];
    }

    public boolean union(int node1, int node2) {
        int grp1 = find(node1);
        int grp2 = find(node2);
        if (grp1 == grp2) {
            return false;
        }
        if (rank[grp1] >= rank[grp2]) {
            groups[grp2] = grp1;
            if (rank[grp1] == rank[grp2]) {
                rank[grp1]++;
            }
        } else {
            groups[grp1] = grp2;
        }
        return true;
    }

    public boolean isConnected(int node1, int node2) {
        return find(node1) == find(node2);
    }
}

class Solution {
    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        Arrays.sort(edgeList, (a, b) -> (a[2] - b[2]));
        int[][] queriesWithIndices = new int[queries.length][4];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            queriesWithIndices[i] = new int[] { query[0], query[1], query[2], i };
        }
        Arrays.sort(queriesWithIndices, (a, b) -> (a[2] - b[2]));
        boolean[] answer = new boolean[queries.length];
        DisjointSet ds = new DisjointSet(n);
        int edgeIdx = 0;
        for (int[] query : queriesWithIndices) {
            while (edgeIdx < edgeList.length && edgeList[edgeIdx][2] < query[2]) {
                ds.union(edgeList[edgeIdx][0], edgeList[edgeIdx++][1]);
            }
            answer[query[3]] = ds.isConnected(query[0], query[1]);
        }
        return answer;
    }
}
// @lc code=end
