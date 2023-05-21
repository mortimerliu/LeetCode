/*
 * @lc app=leetcode id=152 lang=java
 *
 * [152] Maximum Product Subarray
 *
 * https://leetcode.com/problems/maximum-product-subarray/description/
 *
 * algorithms
 * Medium (34.92%)
 * Likes:    15923
 * Dislikes: 481
 * Total Accepted:    999.7K
 * Total Submissions: 2.9M
 * Testcase Example:  '[2,3,-2,4]'
 *
 * Given an integer array nums, find a subarray that has the largest product,
 * and return the product.
 * 
 * The test cases are generated so that the answer will fit in a 32-bit
 * integer.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 2 * 10^4
 * -10 <= nums[i] <= 10
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int maxProduct(int[] nums) {
        // if nums[i:j] is the subarray with max product,
        // then (i==0 || j==nums.length) == true
        int prefix = 1, suffix = 1, ans = nums[0], n = nums.length;
        for (int i = 0; i < nums.length; ++i) {
            prefix = (prefix == 0 ? 1 : prefix) * nums[i];
            suffix = (suffix == 0 ? 1 : suffix) * nums[n - 1 - i];
            ans = Math.max(ans, Math.max(prefix, suffix));
        }
        return ans;
    }
}
// @lc code=end
