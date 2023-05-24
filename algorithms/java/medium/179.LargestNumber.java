/*
 * @lc app=leetcode id=179 lang=java
 *
 * [179] Largest Number
 *
 * https://leetcode.com/problems/largest-number/description/
 *
 * algorithms
 * Medium (34.07%)
 * Likes:    6927
 * Dislikes: 566
 * Total Accepted:    395.1K
 * Total Submissions: 1.1M
 * Testcase Example:  '[10,2]'
 *
 * Given a list of non-negative integers nums, arrange them such that they form
 * the largest number and return it.
 *
 * Since the result may be very large, so you need to return a string instead
 * of an integer.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [10,2]
 * Output: "210"
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [3,30,34,5,9]
 * Output: "9534330"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 10^9
 *
 *
 */

// @lc code=start

import java.util.Arrays;
import java.util.Comparator;

class LargerNumberComparator implements Comparator<String> {

    @Override
    public int compare(String a, String b) {
        String order1 = a + b;
        String order2 = b + a;
        return order2.compareTo(order1);
    }
}

class Solution {
    public String largestNumber(int[] nums) {
        String[] strings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strings[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(strings, new LargerNumberComparator());

        if (strings[0].equals("0")) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : strings) {
            sb.append(s);
        }
        return sb.toString();

        // slower implementation
        // String[] s = new String[nums.length];
        // for (int i = 0; i < nums.length; i++)
        // s[i] = String.valueOf(nums[i]);
        // Arrays.sort(s, (a, b) -> (b + a).compareTo(a + b));
        // return s[0].equals("0") ? "0" : String.join("", s);
    }
}
// @lc code=end
