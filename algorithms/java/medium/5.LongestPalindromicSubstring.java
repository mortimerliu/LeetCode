/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (32.41%)
 * Likes:    25382
 * Dislikes: 1492
 * Total Accepted:    2.4M
 * Total Submissions: 7.5M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, return the longest palindromic substring in s.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "cbbd"
 * Output: "bb"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 1000
 * s consist of only digits and English letters.
 *
 *
 */

// @lc code=start

class Bound {
    int left;
    int right;

    public Bound(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public int length() {
        return right - left;
    }
}

class Solution {
    public String longestPalindrome(String s) {
        // expand center TC O(N^2)
        Bound ans = new Bound(0, 1);
        for (int i = 0; i < s.length(); i++) {
            Bound res = search(s, i, i);
            if (res.length() > ans.length()) {
                ans = res;
            }
            res = search(s, i, i + 1);
            if (res.length() > ans.length()) {
                ans = res;
            }
        }
        return s.substring(ans.left, ans.right);
    }

    private Bound search(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return new Bound(left + 1, right);
    }
}
// @lc code=end
