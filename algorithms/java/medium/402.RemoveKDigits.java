/*
 * @lc app=leetcode id=402 lang=java
 *
 * [402] Remove K Digits
 *
 * https://leetcode.com/problems/remove-k-digits/description/
 *
 * algorithms
 * Medium (30.49%)
 * Likes:    7614
 * Dislikes: 323
 * Total Accepted:    312.6K
 * Total Submissions: 1M
 * Testcase Example:  '"1432219"\n3'
 *
 * Given string num representing a non-negative integer num, and an integer k,
 * return the smallest possible integer after removing k digits from num.
 *
 *
 * Example 1:
 *
 *
 * Input: num = "1432219", k = 3
 * Output: "1219"
 * Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
 * which is the smallest.
 *
 *
 * Example 2:
 *
 *
 * Input: num = "10200", k = 1
 * Output: "200"
 * Explanation: Remove the leading 1 and the number is 200. Note that the
 * output must not contain leading zeroes.
 *
 *
 * Example 3:
 *
 *
 * Input: num = "10", k = 2
 * Output: "0"
 * Explanation: Remove all the digits from the number and it is left with
 * nothing which is 0.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= num.length <= 10^5
 * num consists of only digits.
 * num does not have any leading zeros except for the zero itself.
 *
 *
 */

// @lc code=start

import java.util.*;
import java.util.stream.Collector;

class Solution {
    public String removeKdigits(String num, int k) {
        // // mono stack
        // if (num.length() <= k)
        // return "0";
        // Deque<Character> stack = new ArrayDeque<>();
        // for (int i = 0; i < num.length(); i++) {
        // char c = num.charAt(i);
        // while (k > 0 && !stack.isEmpty() && stack.peekLast() > c) {
        // stack.pollLast();
        // k--;
        // }
        // stack.addLast(c);
        // }
        // while (k-- > 0) {
        // stack.pollLast();
        // }
        // while (!stack.isEmpty() && stack.peekFirst() == '0') {
        // stack.pollFirst();
        // }
        // if (stack.isEmpty())
        // return "0";
        // return stack.stream().map(Object::toString).collect(Collectors.joining(""));
        if (num.length() == k)
            return "0";
        StringBuilder resStack = new StringBuilder(num.length() - k);
        for (int i = 0; i < num.length();) {
            char next = num.charAt(i);
            if (k > 0) {
                if (resStack.length() > 0) {
                    char last = resStack.charAt(resStack.length() - 1);
                    if (last > next) {
                        k--;
                        resStack.deleteCharAt(resStack.length() - 1);
                        continue;
                    }
                }
            }
            if (resStack.capacity() > resStack.length()) {
                resStack.append(next);
            } else
                k--;
            i++;
        }
        int start = 0;
        while (resStack.charAt(start) == '0' && start < resStack.length() - 1)
            start++;
        return resStack.substring(start);
    }
}
// @lc code=end
