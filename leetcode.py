import bisect
from operator import itemgetter
from collections import Counter, defaultdict
from typing import List


"""2273. Find Resultant Array After Removing Anagrams

You are given a 0-indexed string array words, where words[i] consists of 
lowercase English letters. 

In one operation, select any index i such that 0 < i < words.length and 
words[i - 1] and words[i] are anagrams, and delete words[i] from words. 
Keep performing this operation as long as you can select an index that 
satisfies the conditions.

Return words after performing all operations. It can be shown that 
selecting the indices for each operation in any arbitrary order will 
lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase using all the original letters exactly once. 
For example, "dacb" is an anagram of "abdc".

Example 1:

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.
Example 2:

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.
 

Constraints:

* 1 <= words.length <= 100
* 1 <= words[i].length <= 10
* words[i] consists of lowercase English letters.
"""

def removeAnagrams(self, words: List[str]) -> List[str]:
    return [
        w for i, w in enumerate(words) 
        if i == 0 or Counter(words[i-1]) != Counter(words[i])
    ]


"""2274. Maximum Consecutive Floors Without Special Floors

Alice manages a company and has rented some floors of a building as 
office space. Alice has decided some of these floors should be special 
floors, used for relaxation only.

You are given two integers bottom and top, which denote that Alice has 
rented all the floors from bottom to top (inclusive). You are also given 
the integer array special, where special[i] denotes a special floor that 
Alice has designated for relaxation.

Return the maximum number of consecutive floors without a special floor.

Example 1:

Input: bottom = 2, top = 9, special = [4,6]
Output: 3
Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.
Example 2:

Input: bottom = 6, top = 8, special = [7,6,8]
Output: 0
Explanation: Every floor rented is a special floor, so we return 0.
 

Constraints:

* 1 <= special.length <= 105
* 1 <= bottom <= special[i] <= top <= 109
* All the values of special are unique.
"""

def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
    special.sort()
    ans = special[0] - bottom
    for i in range(1, len(special)):
        ans = max(ans, special[i] - special[i-1] - 1)
    ans = max(ans, top - special[-1])
    return ans


"""2275. Largest Combination With Bitwise AND Greater Than Zero

The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.

You are given an array of positive integers candidates. Evaluate the 
bitwise AND of every combination of numbers of candidates. Each number 
in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise 
AND greater than 0.


Example 1:

Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
Example 2:

Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
 
 
Constraints:

* 1 <= candidates.length <= 105
* 1 <= candidates[i] <= 107
"""

def largestCombination(self, candidates: List[int]) -> int:  # type: ignore
    freq = defaultdict(int)
    
    for num in candidates:
        i = 0
        while 1 << i <= num:
            if num & (1 << i) > 0:
                freq[i] += 1
            i += 1
    
    return max(freq.values())

def largestCombination(self, candidates: List[int]) -> int:
    return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))


"""2276. Count Integers in Intervals

Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.

Example 1:

Input
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output
[null, null, null, 6, null, 8]

Explanation
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].
 

Constraints:

* 1 <= left <= right <= 109
* At most 105 calls in total will be made to add and count.
* At least one call will be made to count.
"""

class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        intervals = self.intervals
        
        l = bisect.bisect_left(intervals, left-1, key=itemgetter(1))  # type: ignore
        if l < len(intervals):
            left = min(left, intervals[l][0])
        
        r = bisect.bisect(intervals, right+1, key=itemgetter(0))  # type: ignore
        if r > 0:
            right = max(right, intervals[r-1][1])
        
        for start, end in intervals[l:r]:
            self.cnt -= end - start + 1
        intervals[l:r] = [[left, right]]
        self.cnt += right - left + 1
         
    def count(self) -> int:
        return self.cnt