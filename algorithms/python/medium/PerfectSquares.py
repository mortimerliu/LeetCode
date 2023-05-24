"""
[Medium] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with
itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Constraints:

1 <= n <= 104
"""

import sys


class Solution1:
    def numSquares(self, n: int) -> int:
        """
        DP - Bottom up

        f(n) = min(1 + f(n - i * i) for all i s.t. i * i <= n)

        Time: O(N^3/2)
        Space: O(N)
        """

        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                if dp[i] == 1:
                    break
                j += 1

        return dp[n]


class Solution2:
    def numSquares(self, n: int) -> int:
        """
        Greedy

        consider the question from the following perspective: starting from the set of one perfect squared number to
        multiple numbers, *once* we find a set that sum up to `n`, we find the smallest set and that is our solution

        define a function `is_divided_by(n, count) -> bool` that return a boolean value to indicate whether `n` can be
        divided by a set of perfect squared numbers with size `count`, then:

        `numSquares(n) == min(i for i in range(1, n+1) if is_divided_by(n, i))`

        note that, `is_divided_by(n, count) == any(is_divided_by(n - k, count - 1) for k in psn)`

        where `psn` is the set of perfect squared numbers that are smaller than or equal to `n`

        when do the search, we need to try `count` from smallest (`1`) first to guarantee an optimal answer

        Question: why we don't need to care about repetitive calls to `is_divided_by`?

        Example:
            ```
            is_divided_by(12, 3) -1-> is_divided_by(11, 2) -4-> is_divided_by(7, 1)
            is_divided_by(12, 3) -4-> is_divided_by( 8, 2) -1-> is_divided_by(7, 1)
            ```

        Thoughts: maybe since we search `count` from `1` to `n`, we are implicitly performing BFS and thus won't have
        too much duplicated calls. <- this is probably correct.
        """

        def is_divided_by(n: int, count: int) -> bool:
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if k < n and is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = {i * i for i in range(1, int(n ** 0.5) + 1)}

        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count

        return -1 # to suppress type hint warning


class Solution3:
    def numSquares(self, n: int) -> int:
        """
        Solution 2 actually forms a N-ary tree. To better demonstrate this idea, take the example of `n=13`

            count=1 ->         13 (F)
                           /     |      \
            count=2 -> 12 (F)   4 (T)   9 (T)  <- Found the answer!

        Since it's a tree, to find the smallest, we can use breadth first search.
        """

        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set() # remove duplicates
            for remainder in queue:
                for num in square_nums:
                    if remainder == num:
                        return level
                    elif num < remainder:
                        next_queue.add(remainder - num)
                    else:
                        break
            queue = next_queue

        return level
