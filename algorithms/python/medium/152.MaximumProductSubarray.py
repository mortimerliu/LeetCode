#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.92%)
# Likes:    15923
# Dislikes: 481
# Total Accepted:    999.7K
# Total Submissions: 2.9M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Solution 1: brute force

        O(n^2)
        """

        """
        Solution 2: DP
        observations:
        1. positive numbers are always good to include
        2. negative numbers should be included only if there are even appearance
        3. never across 0
        
        with there three obs, then we want to include as much as possible while
        not across 0, and when there is negative number, only consider extend
        the first neg number or not
        """
        # if len(nums) == 1:
        #     return nums[0]
        # ans = 0
        # cur_prod = first_neg_prod = 1
        # for num in nums:
        #     if num == 0:
        #         cur_prod = first_neg_prod = 1
        #     else:
        #         cur_prod *= num
        #         ans = max(ans, cur_prod, cur_prod // first_neg_prod)
        #         if num < 0 and first_neg_prod > 0:
        #             first_neg_prod = cur_prod
        # return ans

        """
        Solution 3: DP
        max_so_far = max(cur, max_so_far * cur, min_so_far * cur)
        min_so_far = min(cur, max_so_far * cur, min_so_far * cur)
        
        Example: 
        cur:            pos1 neg1      pos2           neg2                neg3
        max_so_far:  1  pos1 neg1      pos2           pos1*neg1*pos2*neg2 pos2*neg2*neg3
        min_so_far:  1  pos1 pos1*neg1 pos1*neg*1pos2 pos2*neg2           pos1*neg1*pos2*neg2*neg3
        """
        # max_so_far = nums[0]
        # min_so_far = nums[0]
        # result = max_so_far

        # for i in range(1, len(nums)):
        #     curr = nums[i]
        #     temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        #     min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        #     max_so_far = temp_max

        #     result = max(max_so_far, result)

        # return result

        """
        Solution 4: the max product subarray must reach either begin of end of nums
        
        For even number of neg, we just include all nums.
        For odd number of neg: we need to abandan 1 neg.
        
        <------candi1----->
        pos,neg,pos,neg,pos,neg,pos
                <------candi2----->
        
        For zeros, they just split the long nums into several small nums and 
        we can condier them independently.
        
        Algo:
        Calculate prefix product in nums.
        Calculate suffix product in nums.
        Return the max.
        """
        revs = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            revs[i] *= revs[i - 1] or 1
        return max(nums + revs)


# @lc code=end
