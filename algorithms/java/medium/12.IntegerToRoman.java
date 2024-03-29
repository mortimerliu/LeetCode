/*
 * @lc app=leetcode id=12 lang=java
 *
 * [12] Integer to Roman
 *
 * https://leetcode.com/problems/integer-to-roman/description/
 *
 * algorithms
 * Medium (61.54%)
 * Likes:    5706
 * Dislikes: 5115
 * Total Accepted:    998.4K
 * Total Submissions: 1.6M
 * Testcase Example:  '3'
 *
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 *
 *
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 *
 * For example, 2 is written as II in Roman numeral, just two one's added
 * together. 12 is written as XII, which is simply X + II. The number 27 is
 * written as XXVII, which is XX + V + II.
 *
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making
 * four. The same principle applies to the number nine, which is written as IX.
 * There are six instances where subtraction is used:
 *
 *
 * I can be placed before V (5) and X (10) to make 4 and 9. 
 * X can be placed before L (50) and C (100) to make 40 and 90. 
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 *
 *
 * Given an integer, convert it to a roman numeral.
 *
 *
 * Example 1:
 *
 *
 * Input: num = 3
 * Output: "III"
 * Explanation: 3 is represented as 3 ones.
 *
 *
 * Example 2:
 *
 *
 * Input: num = 58
 * Output: "LVIII"
 * Explanation: L = 50, V = 5, III = 3.
 *
 *
 * Example 3:
 *
 *
 * Input: num = 1994
 * Output: "MCMXCIV"
 * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= num <= 3999
 *
 *
 */

// @lc code=start

import java.util.*;

class Solution {
    // private static final String[] thousands = { "", "M", "MM", "MMM" };
    // private static final String[] hundreds = { "", "C", "CC", "CCC", "CD", "D",
    // "DC", "DCC", "DCCC", "CM" };
    // private static final String[] tens = { "", "X", "XX", "XXX", "XL", "L", "LX",
    // "LXX", "LXXX", "XC" };
    // private static final String[] ones = { "", "I", "II", "III", "IV", "V", "VI",
    // "VII", "VIII", "IX" };
    private static final int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    private static final String[] symbols = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

    public String intToRoman(int num) {
        // Map<Integer, String[]> mapping = new HashMap<>();
        // mapping.put(1000, new String[] { "M", "-", "-", "-" });
        // mapping.put(100, new String[] { "C", "CD", "D", "CM" });
        // mapping.put(10, new String[] { "X", "XL", "L", "XC" });
        // mapping.put(1, new String[] { "I", "IV", "V", "IX" });

        // StringBuilder sb = new StringBuilder();
        // for (int denom = 1000; denom > 0; denom /= 10) {
        // String[] letters = mapping.get(denom);
        // int digit = num / denom % 10;
        // if (digit == 9) {
        // sb.append(letters[3]);
        // } else {
        // if (digit >= 5) {
        // sb.append(letters[2]);
        // digit -= 5;
        // }
        // if (digit == 4) {
        // sb.append(letters[1]);
        // } else {
        // for (int j = 0; j < digit; j++)
        // sb.append(letters[0]);
        // }
        // }
        // }
        // return sb.toString();

        // return thousands[num / 1000] + hundreds[num % 1000 / 100] + tens[num % 100 /
        // 10] + ones[num % 10];
        StringBuilder sb = new StringBuilder();
        // Loop through each symbol, stopping if num becomes 0.
        for (int i = 0; i < values.length && num > 0; i++) {
            // Repeat while the current symbol still fits into num.
            while (values[i] <= num) {
                num -= values[i];
                sb.append(symbols[i]);
            }
        }
        return sb.toString();
    }
}
// @lc code=end
