/*
 * @lc app=leetcode id=290 lang=java
 *
 * [290] Word Pattern
 *
 * https://leetcode.com/problems/word-pattern/description/
 *
 * algorithms
 * Easy (40.43%)
 * Likes:    6288
 * Dislikes: 756
 * Total Accepted:    528.9K
 * Total Submissions: 1.3M
 * Testcase Example:  '"abba"\n"dog cat cat dog"'
 *
 * Given a pattern and a string s, find if s follows the same pattern.
 *
 * Here follow means a full match, such that there is a bijection between a
 * letter in pattern and a non-empty word in s.
 *
 *
 * Example 1:
 *
 *
 * Input: pattern = "abba", s = "dog cat cat dog"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: pattern = "abba", s = "dog cat cat fish"
 * Output: false
 *
 *
 * Example 3:
 *
 *
 * Input: pattern = "aaaa", s = "dog cat cat dog"
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= pattern.length <= 300
 * pattern contains only lower-case English letters.
 * 1 <= s.length <= 3000
 * s contains only lowercase English letters and spaces ' '.
 * s does not contain any leading or trailing spaces.
 * All the words in s are separated by a single space.
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        // one hash map
        HashMap map = new HashMap();
        String[] words = s.split(" ");
        if (pattern.length() != words.length) {
            return false;
        }
        for (Integer i = 0; i < words.length; i++) {
            String w = words[i];
            char p = pattern.charAt(i);
            if (!map.containsKey(w)) {
                map.put(w, i);
            }
            if (!map.containsKey(p)) {
                map.put(p, i);
            }
            if (map.get(w) != map.get(p)) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
