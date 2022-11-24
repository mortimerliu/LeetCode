package algorithms.java;

import java.util.HashMap;
import java.util.Map;

/**
 * [Medium] 3. Longest Substring Without Repeating Characters
 * 
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 * 
 * Example 1:
 * 
 * Input: s = "abcabcbb"
 * Output: 3
 * 
 * Example 2:
 * 
 * Input: s = "pwwkew"
 * Output: 3
 * 
 * Constraints:
 * 
 * * 0 <= s.length <= 5 * 104
 * * s consists of English letters, digits, symbols and spaces.
 * 
 * @author Hongru Liu
 */
class Solution {
    public int lengthOfLongestSubstring(String s) {
        /**
         * use a HashMap to record the last index of a letter
         * ans = max(ans, cur_idx - last_idx)
         * 
         * if the character set is small, we can use an array to replace
         * HashMap; though it's still O(1), the constant factor is smaller
         *
         * Time: O(n)
         * Space: O(1) or O(m) where m is the size of the character set
         */
        Map<Character, Integer> lastIndex = new HashMap<>();
        int ans = 0;
        int start = -1;

        for (int end = 0; end < s.length(); end++) {
            char cur = s.charAt(end);
            start = Math.max(start, lastIndex.getOrDefault(cur, -1));
            ans = Math.max(ans, end - start);
            lastIndex.put(cur, end);
        }
        return ans;
    }
}
