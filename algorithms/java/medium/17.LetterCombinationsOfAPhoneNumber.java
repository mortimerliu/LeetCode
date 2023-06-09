/*
 * @lc app=leetcode id=17 lang=java
 *
 * [17] Letter Combinations of a Phone Number
 *
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (55.71%)
 * Likes:    15195
 * Dislikes: 847
 * Total Accepted:    1.6M
 * Total Submissions: 2.8M
 * Testcase Example:  '"23"'
 *
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent. Return the answer in
 * any order.
 *
 * A mapping of digits to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 *
 *
 * Example 1:
 *
 *
 * Input: digits = "23"
 * Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
 *
 *
 * Example 2:
 *
 *
 * Input: digits = ""
 * Output: []
 *
 *
 * Example 3:
 *
 *
 * Input: digits = "2"
 * Output: ["a","b","c"]
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= digits.length <= 4
 * digits[i] is a digit in the range ['2', '9'].
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits.length() == 1) {
            int n = 3, digit = Integer.valueOf(digits);
            int offset = 3 * (digit - 2);
            if (digit == 7 || digit == 9)
                n++;
            if (digit == 8 || digit == 9)
                offset++;
            for (int i = 0; i < n; i++)
                res.add("" + (char) ('a' + offset + i));
        } else if (digits.length() > 1) {
            for (String a : letterCombinations(digits.substring(0, 1))) {
                for (String b : letterCombinations(digits.substring(1))) {
                    res.add(a.concat(b));
                }
            }
        }
        return res;
    }
}
// @lc code=end
