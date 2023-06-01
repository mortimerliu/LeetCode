/*
 * @lc app=leetcode id=680 lang=java
 *
 * [680] Valid Palindrome II
 *
 * https://leetcode.com/problems/valid-palindrome-ii/description/
 *
 * algorithms
 * Easy (39.33%)
 * Likes:    7227
 * Dislikes: 370
 * Total Accepted:    597K
 * Total Submissions: 1.5M
 * Testcase Example:  '"aba"'
 *
 * Given a string s, return true if the s can be palindrome after deleting at
 * most one character from it.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "aba"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: s = "abca"
 * Output: true
 * Explanation: You could delete the character 'c'.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "abc"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 *
 *
 */

// @lc code=start
class Solution {
    public boolean validPalindrome(String s) {
        return isValid(s, 0, s.length() - 1, false);
    }

    private boolean isValid(String s, int i, int j, boolean removed) {
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                if (removed) {
                    return false;
                }
                return isValid(s, i + 1, j, true) || isValid(s, i, j - 1, true);
            }
            i++;
            j--;
        }
        return true;
    }
}
// @lc code=end
