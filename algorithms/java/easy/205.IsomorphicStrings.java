/*
 * @lc app=leetcode id=205 lang=java
 *
 * [205] Isomorphic Strings
 *
 * https://leetcode.com/problems/isomorphic-strings/description/
 *
 * algorithms
 * Easy (42.61%)
 * Likes:    6799
 * Dislikes: 1485
 * Total Accepted:    901.7K
 * Total Submissions: 2.1M
 * Testcase Example:  '"egg"\n"add"'
 *
 * Given two strings s and t, determine if they are isomorphic.
 *
 * Two strings s and t are isomorphic if the characters in s can be replaced to
 * get t.
 *
 * All occurrences of a character must be replaced with another character while
 * preserving the order of characters. No two characters may map to the same
 * character, but a character may map to itself.
 *
 *
 * Example 1:
 * Input: s = "egg", t = "add"
 * Output: true
 * Example 2:
 * Input: s = "foo", t = "bar"
 * Output: false
 * Example 3:
 * Input: s = "paper", t = "title"
 * Output: true
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * t.length == s.length
 * s and t consist of any valid ascii character.
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        // same as 290
        if (s.length() != t.length())
            return false;
        // Map<Character, Integer> smap = new HashMap<>();
        // Map<Character, Integer> tmap = new HashMap<>();
        // for (int i = 0; i < s.length(); i++) {
        // char sc = s.charAt(i);
        // char tc = t.charAt(i);
        // if (!smap.containsKey(sc))
        // smap.put(sc, i);
        // if (!tmap.containsKey(tc))
        // tmap.put(tc, i);
        // if (!smap.get(sc).equals(tmap.get(tc)))
        // return false;
        // }
        // return true;
        // using int[]
        int[] map1 = new int[200];
        int[] map2 = new int[200];
        for (int i = 0; i < s.length(); i++) {
            if (map1[s.charAt(i)] != map2[t.charAt(i)])
                return false;
            map1[s.charAt(i)] = i + 1;
            map2[t.charAt(i)] = i + 1;
        }
        return true;
    }
}
// @lc code=end
