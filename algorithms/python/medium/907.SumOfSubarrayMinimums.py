#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (34.31%)
# Likes:    6117
# Dislikes: 415
# Total Accepted:    145.9K
# Total Submissions: 409K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers arr, find the sum of min(b), where b ranges over
# every (contiguous) subarray of arr. Since the answer may be large, return the
# answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4],
# [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
#
#
# Example 2:
#
#
# Input: arr = [11,81,94,43,3]
# Output: 444
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4
#
#
#


# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Solution 1: brute force: min so far

        O(n^2)
        """

        """
        Solution 2: monotonic stack (non decreasing)
        
        for equals, left < right
        
        for each `i`, 
        * find min index `left` such that all(nums[j] > nums[i] for left <= j < i)
        * find max index `right` such that all(nums[j] >= nums[i] for i < j <= right)
        * ans += nums[i] * (i - left + 1) * (right - i + 1)
        """
        M = 1000000007
        ans = 0
        n = len(arr)
        stack = []
        for i in range(n + 1):
            num = arr[i] if i < n else 0
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                ans += arr[j] * (i - j) * (j - (stack[-1] if stack else -1))
            stack.append(i)
        return ans % M

        """
        Solution 3: mono stack + dp
        
        dp[i]: sum of min for all subarrays ending at index i
        dp[i] = dp[j] + (i - j) * nums[i]
        where j is the min index where nums[j] < nums[i]
        which can be found usng a mono stack
        """
        # M = 1000000007
        # ans = 0
        # n = len(arr)
        # stack = []
        # dp = [0] * n
        # for i in range(n):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         stack.pop()
        #     if stack:
        #         dp[i] = dp[stack[-1]] + (i - stack[-1]) * arr[i]
        #     else:
        #         dp[i] = (i + 1) * arr[i]
        #     stack.append(i)
        #     ans += dp[i]
        # return ans % M


# @lc code=end
