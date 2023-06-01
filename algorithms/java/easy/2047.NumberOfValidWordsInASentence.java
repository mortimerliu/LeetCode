/*
 * @lc app=leetcode id=2047 lang=java
 *
 * [2047] Number of Valid Words in a Sentence
 *
 * https://leetcode.com/problems/number-of-valid-words-in-a-sentence/description/
 *
 * algorithms
 * Easy (29.51%)
 * Likes:    239
 * Dislikes: 705
 * Total Accepted:    22.3K
 * Total Submissions: 76.7K
 * Testcase Example:  '"cat and  dog"'
 *
 * A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'),
 * hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only.
 * Each sentence can be broken down into one or more tokens separated by one or
 * more spaces ' '.
 *
 * A token is a valid word if all three of the following are true:
 *
 *
 * It only contains lowercase letters, hyphens, and/or punctuation (no
 * digits).
 * There is at most one hyphen '-'. If present, it must be surrounded by
 * lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not
 * valid).
 * There is at most one punctuation mark. If present, it must be at the end of
 * the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not
 * valid).
 *
 *
 * Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
 *
 * Given a string sentence, return the number of valid words in sentence.
 *
 *
 * Example 1:
 *
 *
 * Input: sentence = "cat and  dog"
 * Output: 3
 * Explanation: The valid words in the sentence are "cat", "and", and "dog".
 *
 *
 * Example 2:
 *
 *
 * Input: sentence = "!this  1-s b8d!"
 * Output: 0
 * Explanation: There are no valid words in the sentence.
 * "!this" is invalid because it starts with a punctuation mark.
 * "1-s" and "b8d" are invalid because they contain digits.
 *
 *
 * Example 3:
 *
 *
 * Input: sentence = "alice and  bob are playing stone-game10"
 * Output: 5
 * Explanation: The valid words in the sentence are "alice", "and", "bob",
 * "are", and "playing".
 * "stone-game10" is invalid because it contains digits.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= sentence.length <= 1000
 * sentence only contains lowercase English letters, digits, ' ', '-', '!',
 * '.', and ','.
 * There will be at least 1 token.
 *
 *
 */

// @lc code=start
class Solution {
    public int countValidWords(String sentence) {
        int n = sentence.length();
        int count = 0;
        boolean hyphen = false, is_valid = true;
        for (int i = 0; i <= n; i++) {
            char c = i < n ? sentence.charAt(i) : ' ';
            if (c == ' ') {
                if (is_valid && i > 0 && sentence.charAt(i - 1) != ' ') {
                    count++;
                }
                is_valid = true;
                hyphen = false;
            } else if (is_valid) {
                if (c >= '0' && c <= '9') {
                    is_valid = false;
                } else if (c == '!' || c == '.' || c == ',') {
                    is_valid = i + 1 == n || sentence.charAt(i + 1) == ' ';
                } else if (c == '-') {
                    is_valid = !hyphen && i > 0 && i + 1 < n && sentence.charAt(i - 1) >= 'a'
                            && sentence.charAt(i - 1) <= 'z'
                            && sentence.charAt(i + 1) >= 'a' && sentence.charAt(i + 1) <= 'z';
                    hyphen = true;
                }
            }
        }
        return count;
    }
}
// @lc code=end
