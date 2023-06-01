/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Find the Index of the First Occurrence in a String
 *
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
 *
 * algorithms
 * Medium (37.65%)
 * Likes:    3571
 * Dislikes: 187
 * Total Accepted:    1.8M
 * Total Submissions: 4.4M
 * Testcase Example:  '"sadbutsad"\n"sad"'
 *
 * Given two strings needle and haystack, return the index of the first
 * occurrence of needle in haystack, or -1 if needle is not part of
 * haystack.
 *
 *
 * Example 1:
 *
 *
 * Input: haystack = "sadbutsad", needle = "sad"
 * Output: 0
 * Explanation: "sad" occurs at index 0 and 6.
 * The first occurrence is at index 0, so we return 0.
 *
 *
 * Example 2:
 *
 *
 * Input: haystack = "leetcode", needle = "leeto"
 * Output: -1
 * Explanation: "leeto" did not occur in "leetcode", so we return -1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= haystack.length, needle.length <= 10^4
 * haystack and needle consist of only lowercase English characters.
 *
 *
 */

// @lc code=start
class Solution {
    int B1 = 26;
    int MOD1 = 1_000_000_033;
    int B2 = 27;
    int MOD2 = 2_147_483_647;

    public int strStr(String haystack, String needle) {
        // rabin-karp double hashing
        int m = needle.length(), n = haystack.length();

        long factor1 = 1, factor2 = 1;
        for (int i = 0; i < m; i++) {
            factor1 = (factor1 * B1) % MOD1;
            factor2 = (factor2 * B2) % MOD2;
        }

        long needleHash1 = hash(needle, m, B1, MOD1);
        long needleHash2 = hash(needle, m, B2, MOD2);
        long haystackHash1 = 0, haystackHash2 = 0;
        for (int i = 0; i <= n - m; i++) {
            if (i == 0) {
                haystackHash1 = hash(haystack, m, B1, MOD1);
                haystackHash2 = hash(haystack, m, B2, MOD2);
            } else {
                haystackHash1 = ((haystackHash1 * B1) % MOD1 - ((haystack.charAt(i - 1) - 'a') * factor1) % MOD1
                        + (haystack.charAt(i + m - 1) - 'a') + MOD1) % MOD1;
                haystackHash2 = ((haystackHash2 * B2) % MOD2 - ((haystack.charAt(i - 1) - 'a') * factor2) % MOD2
                        + (haystack.charAt(i + m - 1) - 'a') + MOD2) % MOD2;
            }
            if (haystackHash1 == needleHash1 && haystackHash2 == needleHash2 && check(haystack, needle, i)) {
                return i;
            }
        }
        return -1;
    }

    private long hash(String string, int m, int B, int MOD) {
        long value = 0;
        long factor = 1;
        for (int i = m - 1; i >= 0; i--) {
            value += (int) ((string.charAt(i) - 'a') * factor) % MOD;
            factor = (factor * B) % MOD;
        }
        return value % MOD;
    }

    private boolean check(String haystack, String needle, int i) {
        for (int j = 0; j < needle.length(); j++) {
            if (haystack.charAt(i + j) != needle.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
