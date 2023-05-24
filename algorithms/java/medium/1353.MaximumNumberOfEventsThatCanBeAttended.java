/*
 * @lc app=leetcode id=1353 lang=java
 *
 * [1353] Maximum Number of Events That Can Be Attended
 *
 * https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
 *
 * algorithms
 * Medium (32.88%)
 * Likes:    2417
 * Dislikes: 325
 * Total Accepted:    69.5K
 * Total Submissions: 214K
 * Testcase Example:  '[[1,2],[2,3],[3,4]]'
 *
 * You are given an array of events where events[i] = [startDayi, endDayi].
 * Every event i starts at startDayi and ends at endDayi.
 *
 * You can attend an event i at any day d where startTimei <= d <= endTimei.
 * You can only attend one event at any time d.
 *
 * Return the maximum number of events you can attend.
 *
 *
 * Example 1:
 *
 *
 * Input: events = [[1,2],[2,3],[3,4]]
 * Output: 3
 * Explanation: You can attend all the three events.
 * One way to attend them all is as shown.
 * Attend the first event on day 1.
 * Attend the second event on day 2.
 * Attend the third event on day 3.
 *
 *
 * Example 2:
 *
 *
 * Input: events= [[1,2],[2,3],[3,4],[1,2]]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= events.length <= 10^5
 * events[i].length == 2
 * 1 <= startDayi <= endDayi <= 10^5
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public int maxEvents(int[][] events) {
        // priority queue
        PriorityQueue<Integer> started = new PriorityQueue<>();
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));
        int ans = 0, i = 0, day = 0, n = events.length;
        while (i < n || !started.isEmpty()) {
            if (i < n && events[i][0] <= day) {
                started.add(events[i][1]);
                i++;
            } else {
                while (!started.isEmpty() && started.peek() < day) {
                    started.poll();
                }
                if (!started.isEmpty()) {
                    started.poll();
                    ans++;
                    day++;
                } else {
                    if (i < n) {
                        day = events[i][0];
                    } else {
                        day = -1;
                    }

                }
            }
        }
        return ans;
    }
}
// @lc code=end
