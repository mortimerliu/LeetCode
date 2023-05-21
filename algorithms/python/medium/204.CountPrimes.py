#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Medium (33.07%)
# Likes:    6808
# Dislikes: 1285
# Total Accepted:    733.5K
# Total Submissions: 2.2M
# Testcase Example:  '10'
#
# Given an integer n, return the number of prime numbers that are strictly less
# than n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Solution 1: check every number
        """

        # def is_prime(m):
        #     # O(m^0.5)
        #     for i in range(2, max(int(m**0.5) + 1, m)):
        #         if m % i == 0:
        #             return False
        #     return True

        # if n < 2:
        #     return 0
        # return sum(1 for i in range(2, n) if is_prime(i))

        """
        Solution 2: Sieve of Eratosthenes
        
        once we know 2 is a prime number, we can eliminate all multiples of 2
        once we know 3 is a prime number, we can eliminate all muliples of 3
        ...
        """
        if n < 2:
            return 0
        # 1 means is_prime
        nums = [1] * n
        # start from 2, mark all numbers that are not possible to be prime
        nums[0] = nums[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if nums[i]:
                for j in range(i * i, n, i):
                    nums[j] = 0
        return sum(nums)


# @lc code=end
