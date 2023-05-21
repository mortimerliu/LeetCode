/*
 * @lc app=leetcode id=204 lang=java
 *
 * [204] Count Primes
 *
 * https://leetcode.com/problems/count-primes/description/
 *
 * algorithms
 * Medium (33.07%)
 * Likes:    6808
 * Dislikes: 1285
 * Total Accepted:    733.5K
 * Total Submissions: 2.2M
 * Testcase Example:  '10'
 *
 * Given an integer n, return the number of prime numbers that are strictly
 * less than n.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 10
 * Output: 4
 * Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 0
 * Output: 0
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 1
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= n <= 5 * 10^6
 * 
 * 
 */

// @lc code=start
class Solution {
    public int countPrimes(int n) {
        // Sieve of Eratosthenes
        // Time
        // https://leetcode.com/problems/count-primes/solutions/473021/Time-Complexity-O(log(log(n))-Explained/
        if (n <= 2) {
            return 0;
        }

        boolean[] numbers = new boolean[n];
        for (int p = 2; p <= (int) Math.sqrt(n); ++p) {
            if (!numbers[p]) {
                for (int j = p * p; j < n; j += p) {
                    numbers[j] = true;
                }
            }
        }

        int numberOfPrimes = 0;
        for (int i = 2; i < n; i++) {
            if (!numbers[i]) {
                ++numberOfPrimes;
            }
        }

        return numberOfPrimes;
    }
}
// @lc code=end
