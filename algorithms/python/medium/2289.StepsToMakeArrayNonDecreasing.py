#
# @lc app=leetcode id=2289 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/
#
# algorithms
# Medium (21.39%)
# Likes:    1084
# Dislikes: 111
# Total Accepted:    14.9K
# Total Submissions: 71.1K
# Testcase Example:  '[5,3,4,4,7,3,6,11,8,5,11]'
#
# You are given a 0-indexed integer array nums. In one step, remove all
# elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
#
# Return the number of steps performed until nums becomes a non-decreasing
# array.
#
#
# Example 1:
#
#
# Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
# Output: 3
# Explanation: The following are the steps performed:
# - Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
# - Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
# - Step 3: [5,4,7,11,11] becomes [5,7,11,11]
# [5,7,11,11] is a non-decreasing array. Therefore, we return 3.
#
#
# Example 2:
#
#
# Input: nums = [4,5,7,7,13]
# Output: 0
# Explanation: nums is already a non-decreasing array. Therefore, we return
# 0.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/steps-to-make-array-non-decreasing/solutions/2085864/java-c-python-stack-dp-explanation-poem/

        长江后浪推前浪，
        前浪死在沙滩上。
        后浪继续往前推，
        还是死在沙滩上。

        Solution 1: brute force
        go step by step, worst case, we can only remove 1 element at
        a step (the array is sorted descendingly), then runtime is
        O(n^2)
        """

        """
        Solution 2: DP & Stack - Iterate forward
        For index i,
        * if it is max so far, no need to remove
        * else, it needs to be removed
          * to remove it, we need to first remove all numbers on its
            left and is smaller than it

        we can use a stack to maintain this - non increasing stack

        Example:
        * number indicates how many steps to remove
        * ! note it's 4 instead of 3 as there is a number smaller than it
          requring 3 steps to remove (*).
                       0
        0             /
         \           4!
          \   3*    /
           \ 2 1   /
            1   \ 2
                 1
        """
        # n = len(nums)
        # dp = [0] * n
        # stack = []
        # for i in range(n):
        #     cur = 0
        #     while stack and nums[stack[-1]] <= nums[i]:
        #         cur = max(cur, dp[stack.pop()])
        #     # if stack is empty, that means the nums[i] is the next
        #     # max so far, so no need to remove (dp[i] = 0)
        #     if stack:
        #         dp[i] = cur + 1
        #     stack.append(i)
        # return max(dp)

        """
        Solution 3: DP & Stack - Iterate backward
        When looking from backward, nums[i] can only be added to the
        list when there are no numbers on the right that is smaller than
        itself - this can be achieved using a monotonic stack

        the meaning of dp is different from solution 2: now the dp[i]
        means # of steps to remove all numbers to the right of nums[i]
        ( # items that are eaten by itme i) before we can add nums[i] to
        the resulting attary

        lets say we have a sequence [15, 2, 11, 13, 15]. And before we
        reach this, "11" ate 10 elements.


             15 2 11 13 15
        dp -> 0 0 10  0  0

        so how many steps "15" needs to eat until "13"?
          * from 15's perspective, it will need eat 3 steps to consume
            [2,11,13].
          * but 11 is taking its time to eat the 10 elements.
          * When 15 is eating, **concurrently** 11 is eating its share
            as well.
          * When 15 catches up with 11, it will be eating the remaining
            of 11's share in 11's place. so the time take for 15 to eat
            everything will be max(3, 10).
        """
        n = len(nums)
        stack = []
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                # cur number at i can eat the number at top of the stack
                # need one more step to eat
                # note that, the number to be eat could also potentially
                # eat other numbers, and if that takes more steps,
                # we need to take the maximum
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)
        return max(dp)


# @lc code=end
