/*
 * @lc app=leetcode id=2444 lang=java
 *
 * [2444] Count Subarrays With Fixed Bounds
 *
 * https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
 *
 * algorithms
 * Hard (43.15%)
 * Likes:    2155
 * Dislikes: 46
 * Total Accepted:    56.9K
 * Total Submissions: 92K
 * Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
 *
 * You are given an integer array nums and two integers minK and maxK.
 *
 * A fixed-bound subarray of nums is a subarray that satisfies the following
 * conditions:
 *
 *
 * The minimum value in the subarray is equal to minK.
 * The maximum value in the subarray is equal to maxK.
 *
 *
 * Return the number of fixed-bound subarrays.
 *
 * A subarray is a contiguous part of an array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
 * Output: 2
 * Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,1,1,1], minK = 1, maxK = 1
 * Output: 10
 * Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
 * possible subarrays.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^5
 * 1 <= nums[i], minK, maxK <= 10^6
 *
 *
 */

// @lc code=start
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        // two pointers
        int left_bound = -1, minIdx = -1, maxIdx = -1;
        long count = 0;
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (num < minK || num > maxK) {
                left_bound = i;
            }
            if (num == minK) {
                minIdx = i;
            }
            if (num == maxK) {
                maxIdx = i;
            }
            count += Math.max(0, Math.min(minIdx, maxIdx) - left_bound);
        }
        return count;
    }
}
// @lc code=end
