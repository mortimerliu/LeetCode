/*
 * @lc app=leetcode id=1274 lang=java
 *
 * [1274] Number of Ships in a Rectangle
 *
 * https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/
 *
 * algorithms
 * Hard (69.40%)
 * Likes:    486
 * Dislikes: 53
 * Total Accepted:    25K
 * Total Submissions: 36.2K
 * Testcase Example:  '[[1,1],[2,2],[3,3],[5,5]]\n[4,4]\n[0,0]'
 *
 * (This problem is an interactive problem.)
 *
 * Each ship is located at an integer point on the sea represented by a
 * cartesian plane, and each integer point may contain at most 1 ship.
 *
 * You have a function Sea.hasShips(topRight, bottomLeft) which takes two
 * points as arguments and returns true If there is at least one ship in the
 * rectangle represented by the two points, including on the boundary.
 *
 * Given two points: the top right and bottom left corners of a rectangle,
 * return the number of ships present in that rectangle. It is guaranteed that
 * there are at most 10 ships in that rectangle.
 *
 * Submissions making more than 400 calls to hasShips will be judged Wrong
 * Answer. Also, any solutions that attempt to circumvent the judge will result
 * in disqualification.
 *
 *
 * Example :
 *
 *
 * Input:
 * ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
 * Output: 3
 * Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 *
 *
 * Example 2:
 *
 *
 * Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * On the input ships is only given to initialize the map internally. You must
 * solve this problem "blindfolded". In other words, you must find the answer
 * using the given hasShips API, without knowing the ships position.
 * 0 <= bottomLeft[0] <= topRight[0] <= 1000
 * 0 <= bottomLeft[1] <= topRight[1] <= 1000
 * topRight != bottomLeft
 *
 *
 */

// @lc code=start
/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Sea {
 * public boolean hasShips(int[] topRight, int[] bottomLeft);
 * }
 */

class Solution {
    public int countShips(Sea sea, int[] topRight, int[] bottomLeft) {
        // Time: let M be length, N be width of the rectangle, S be # of ships
        // O(S * log_2(max(M, N)) - log_4(S))
        // Worse case scenario: we need at least S calls to split S ships
        // to S regions such that each region contains one ship, at that time,
        // we are at log_4(S) level of recursion. Total level of recursion is
        // log_2(max(M, N)). Then for each region containing one ship, we need
        // to go through all the remaining level fo recursion to find the ship
        // Gaurantee that < 400 calls: M, N < 1000, thus total level of recursion
        // < 10. Since we have at most 10 ships and to find each ship, we need
        // at most 40 calls (each level with 4 calls, 1 return True, 3 return
        // False); thus total # of calls < 10 * 40 = 400
        if (bottomLeft[0] > topRight[0] || bottomLeft[1] > topRight[1])
            return 0;
        if (!sea.hasShips(topRight, bottomLeft))
            return 0;

        // If the rectangle represents a single point, a ship is located
        if (topRight[0] == bottomLeft[0] && topRight[1] == bottomLeft[1])
            return 1;
        int midX = (topRight[0] + bottomLeft[0]) / 2;
        int midY = (topRight[1] + bottomLeft[1]) / 2;
        return countShips(sea, new int[] { midX, midY }, bottomLeft) +
                countShips(sea, topRight, new int[] { midX + 1, midY + 1 }) +
                countShips(sea, new int[] { midX, topRight[1] }, new int[] { bottomLeft[0], midY + 1 }) +
                countShips(sea, new int[] { topRight[0], midY }, new int[] { midX + 1, bottomLeft[1] });
    }
}
// @lc code=end
