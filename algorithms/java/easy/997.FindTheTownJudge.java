/*
 * @lc app=leetcode id=997 lang=java
 *
 * [997] Find the Town Judge
 *
 * https://leetcode.com/problems/find-the-town-judge/description/
 *
 * algorithms
 * Easy (49.29%)
 * Likes:    5557
 * Dislikes: 447
 * Total Accepted:    409.5K
 * Total Submissions: 827.3K
 * Testcase Example:  '2\n[[1,2]]'
 *
 * In a town, there are n people labeled from 1 to n. There is a rumor that one
 * of these people is secretly the town judge.
 * 
 * If the town judge exists, then:
 * 
 * 
 * The town judge trusts nobody.
 * Everybody (except for the town judge) trusts the town judge.
 * There is exactly one person that satisfies properties 1 and 2.
 * 
 * 
 * You are given an array trust where trust[i] = [ai, bi] representing that the
 * person labeled ai trusts the person labeled bi. If a trust relationship does
 * not exist in trust array, then such a trust relationship does not exist.
 * 
 * Return the label of the town judge if the town judge exists and can be
 * identified, or return -1 otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 2, trust = [[1,2]]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 3, trust = [[1,3],[2,3]]
 * Output: 3
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 3, trust = [[1,3],[2,3],[3,1]]
 * Output: -1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 1000
 * 0 <= trust.length <= 10^4
 * trust[i].length == 2
 * All the pairs of trust are unique.
 * ai != bi
 * 1 <= ai, bi <= n
 * 
 * 
 */

// @lc code=start

class Solution {
    public int findJudge(int n, int[][] trust) {
        // hashmap - graph indegree outdegree
        // int[] indegree = new int[n + 1];
        // int[] outdegree = new int[n + 1];
        // for (int[] edge : trust) {
        // indegree[edge[1]]++;
        // outdegree[edge[0]]++;
        // }
        // for (int i = 1; i <= n; i++) {
        // if (indegree[i] == n - 1 && outdegree[i] == 0) {
        // return i;
        // }
        // }
        // return -1;

        // just one array
        int[] diff = new int[n + 1];
        for (int[] edge : trust) {
            diff[edge[1]]++;
            diff[edge[0]]--;
        }
        for (int i = 1; i <= n; i++) {
            if (diff[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
}
// @lc code=end
