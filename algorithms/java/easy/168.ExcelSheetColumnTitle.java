/*
 * @lc app=leetcode id=168 lang=java
 *
 * [168] Excel Sheet Column Title
 *
 * https://leetcode.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (34.83%)
 * Likes:    3789
 * Dislikes: 549
 * Total Accepted:    379.7K
 * Total Submissions: 1.1M
 * Testcase Example:  '1'
 *
 * Given an integer columnNumber, return its corresponding column title as it
 * appears in an Excel sheet.
 *
 * For example:
 *
 *
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
 *
 *
 *
 * Example 1:
 *
 *
 * Input: columnNumber = 1
 * Output: "A"
 *
 *
 * Example 2:
 *
 *
 * Input: columnNumber = 28
 * Output: "AB"
 *
 *
 * Example 3:
 *
 *
 * Input: columnNumber = 701
 * Output: "ZY"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= columnNumber <= 2^31 - 1
 *
 *
 */

// @lc code=start
class Solution {
    public String convertToTitle(int columnNumber) {
        // subtract 1: though this is base 26 numbering system,
        // the digit is 1 to 26 instead of 0 to 25
        // thus, at every iteration, we minus 1 to convert the last digit
        // from 1...26 to 0...25
        StringBuilder sb = new StringBuilder();
        while (columnNumber-- > 0) {
            sb.append((char) (columnNumber % 26 + 'A'));
            columnNumber /= 26;
        }
        return sb.reverse().toString();
    }
}
// @lc code=end
