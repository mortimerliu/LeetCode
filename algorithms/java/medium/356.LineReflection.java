/*
 * @lc app=leetcode id=356 lang=java
 *
 * [356] Line Reflection
 *
 * https://leetcode.com/problems/line-reflection/description/
 *
 * algorithms
 * Medium (34.66%)
 * Likes:    259
 * Dislikes: 531
 * Total Accepted:    35.2K
 * Total Submissions: 101K
 * Testcase Example:  '[[1,1],[-1,1]]'
 *
 * Given n points on a 2D plane, find if there is such a line parallel to the
 * y-axis that reflects the given points symmetrically.
 *
 * In other words, answer whether or not if there exists a line that after
 * reflecting all points over the given line, the original points' set is the
 * same as the reflected ones.
 *
 * Note that there can be repeated points.
 *
 *
 * Example 1:
 *
 *
 * Input: points = [[1,1],[-1,1]]
 * Output: true
 * Explanation: We can choose the line x = 0.
 *
 *
 * Example 2:
 *
 *
 * Input: points = [[1,1],[-1,-1]]
 * Output: false
 * Explanation: We can't choose a line.
 *
 *
 *
 * Constraints:
 *
 *
 * n == points.length
 * 1 <= n <= 10^4
 * -10^8 <= points[i][j] <= 10^8
 *
 *
 *
 * Follow up: Could you do better than O(n^2)?
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public boolean isReflected(int[][] points) {
        int xMin = Integer.MAX_VALUE, xMax = Integer.MIN_VALUE;
        Set<String> pointsSet = new HashSet<>();
        for (int[] point : points) {
            pointsSet.add(Arrays.toString(point));
            xMax = Math.max(xMax, point[0]);
            xMin = Math.min(xMin, point[0]);
        }
        // int range: -2,147,483,648 to 2,147,483,647
        // x range: -10^8 to 10^8
        int sum = xMin + xMax;
        for (int[] point : points) {
            int[] comp = new int[] { sum - point[0], point[1] };
            if (!pointsSet.contains(Arrays.toString(comp))) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
