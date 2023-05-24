/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (36.42%)
 * Likes:    9282
 * Dislikes: 1100
 * Total Accepted:    740.6K
 * Total Submissions: 2.1M
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers, return an array of all the unique
 * quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
 *
 *
 * 0 <= a, b, c, d < n
 * a, b, c, and d are distinct.
 * nums[a] + nums[b] + nums[c] + nums[d] == target
 *
 *
 * You may return the answer in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,0,-1,0,-2,2], target = 0
 * Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,2,2,2,2], target = 8
 * Output: [[2,2,2,2]]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 200
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 *
 *
 */

// @lc code=start
import java.util.*;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, target, 4, 0);
    }

    // notice the data type for target
    // target - nums[j] could overflow if it's int
    List<List<Integer>> kSum(int[] nums, long target, int k, int i) {
        if (k == 2) {
            return twoSum(nums, target, i);
        }
        List<List<Integer>> res = new ArrayList<>();

        long avg = target / k;
        if (i >= nums.length || nums[i] > avg || nums[nums.length - 1] < avg) {
            return res;
        }

        for (int j = i; j < nums.length; j++) {
            if (j == i || nums[j] != nums[j - 1]) {
                for (List<Integer> subset : kSum(nums, target - nums[j], k - 1, j + 1)) {
                    res.add(new ArrayList<>(Arrays.asList(nums[j])));
                    res.get(res.size() - 1).addAll(subset);
                }
            }
        }
        return res;
    }

    List<List<Integer>> twoSum(int[] nums, long target, int i) {
        List<List<Integer>> res = new ArrayList<>();
        Set<Long> seen = new HashSet<>();
        for (int j = i; j < nums.length; j++) {
            if (res.isEmpty() || res.get(res.size() - 1).get(1) != nums[j]) {
                if (seen.contains(target - nums[j])) {
                    res.add(Arrays.asList((int) target - nums[j], nums[j]));
                }
                seen.add((long) nums[j]);
            }
        }
        return res;
    }
}
// @lc code=end
