import bisect
from functools import lru_cache
import heapq
from itertools import accumulate
from math import gcd
from operator import itemgetter
from collections import Counter, defaultdict, deque
from typing import List, Optional


"""65. Valid Number

A **valid number** can be split up into these components (in order):

1. A **decimal number** or an **integer**.
2. (Optional) An `'e'` or `'E'`, followed by an **integer**.

A **decimal number** can be split up into these components (in order):

1. (Optional) A sign character (either `'+'` or `'-'`).
2. One of the following formats:
   1. One or more digits, followed by a dot `'.'`.
   2. One or more digits, followed by a dot `'.'`, followed by one or more digits.
   3. A dot `'.'`, followed by one or more digits.

An **integer** can be split up into these components (in order):

1. (Optional) A sign character (either `'+'` or `'-'`).
2. One or more digits.

For example, all the following are valid numbers: `["2", "0089", "-0.1", 
"+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", 
"-123.456e789"]`, while the following are not valid numbers: `["abc", 
"1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`.

Given a string `s`, return `true` *if* `s` *is a **valid number***.


**Example 1:**

```
Input: s = "0"
Output: true
```

**Example 2:**

```
Input: s = "e"
Output: false
```

**Example 3:**

```
Input: s = "."
Output: false
```
 

**Constraints:**

- `1 <= s.length <= 20`
- `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`.
"""

def isNumber(s: str) -> bool:
    # Deterministic Finite Automation (DFA)
    # 8 states, depends on whether see digits, dot, exponent so far
    # state 1, 4, 7 are valid
    # 1: 124
    # 4: 123.34
    # 7: 123.34E12
    # 0: digit; 1: sign; 2: dot; 3: exponent
    dfa = [
        {0: 1, 1: 3, 2: 2},
        {0: 1, 3: 5, 2: 4},
        {0: 4},
        {2: 2, 0: 1},
        {0: 4, 3: 5},
        {0: 7, 1: 6},
        {0: 7},
        {0: 7},
    ]
    
    cur_state = 0
    for c in s:
        if c.isdigit():
            grp = 0
        elif c in ('+', '-'):
            grp = 1
        elif c == '.':
            grp = 2
        elif c in ('E', 'e'):
            grp = 3
        else:
            return False
        if grp not in dfa[cur_state]:
            return False
        cur_state = dfa[cur_state][grp]
        
    return cur_state in (1, 4, 7)


"""125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

* 1 <= s.length <= 2 * 105
* s consists only of printable ASCII characters.
"""

def isPalindrome(self, s: str) -> bool:
    # two pointers
    i, j = 0, len(s)-1
    while i <= j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


"""246. Strobogrammatic Number

Given a string `num` which represents an integer, return `true` *if* 
`num` *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when 
rotated `180` degrees (looked at upside down).


**Example 1:**

```
Input: num = "69"
Output: true
```

**Example 2:**

```
Input: num = "88"
Output: true
```

**Example 3:**

```
Input: num = "962"
Output: false
```


**Constraints:**

- `1 <= num.length <= 50`
- `num` consists of only digits.
- `num` does not contain any leading zeros except for zero itself.
"""

def isStrobogrammatic(num: str) -> bool:
    n = len(num)
    for i in range((n+1)//2):
        if not num[i] + num[n-1-i] in ('00', '11', '88', '69', '96'):
            return False
    return True


"""346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving 
average of all integers in the sliding window.

Implement the MovingAverage class:

* MovingAverage(int size) Initializes the object with the size of the window size.
* double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:

* 1 <= size <= 1000
* -105 <= val <= 105
* At most 104 calls will be made to next.
"""

class MovingAverage:

    def __init__(self, size: int):
        self.deque = deque([])
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.deque) == self.size:
            self.total -= self.deque.popleft()
        self.total += val
        self.deque.append(val)
        return self.total / len(self.deque)


"""498. Diagonal Traverse

Given an `m x n` matrix `mat`, return *an array of all the elements of 
the array in a diagonal order*.

 
**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

 
**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 104`
- `1 <= m * n <= 104`
- `-105 <= mat[i][j] <= 105`
"""

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    # m+n-1 diagonals, for k-th (0-indexed) diagonal, i + j = k
    # if k % 2 == 0: i from m-1 to 0
    # if k % 2 == 1: i from 0 to m-1
    # make sure 0 <= j < n
    
    m, n = len(mat), len(mat[0])
    array = []
    
    # for k in range(m+n):
    #     it = range(m) if k % 2 else range(m-1, -1, -1)
    #     for i in it:
    #         if 0 <= k-i < n:
    #             array.append(mat[i][k-i])
    # return array
    
    # cannot simply loop as above as it will waste a lot of time
    # do the checking, especailly for matrix with shape like
    # (40000, 1) for example. True time compexity for above is
    # O((m+n)*n)
    # need to only traverse O(m*n)
    
    for k in range(m+n):
        if k % 2:
            i = max(0, k-n+1)
            j = k - i
            while i < m and j > -1:
                array.append(mat[i][j])
                i += 1
                j -= 1
        else:
            j = max(0, k-m+1)
            i = k - j
            while i > -1 and j < n:
                array.append(mat[i][j])
                i -= 1
                j += 1
    
    return array


"""539. Minimum Time Difference

Given a list of 24-hour clock time points in **"HH:MM"** format, return 
*the minimum **minutes** difference between any two time-points in the 
list*.


**Example 1:**

```
Input: timePoints = ["23:59","00:00"]
Output: 1
```

**Example 2:**

```
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
```


**Constraints:**

- `2 <= timePoints.length <= 2 * 104`
- `timePoints[i]` is in the format **"HH:MM"**.
"""

def findMinDifference(timePoints: List[str]) -> int:
    def toMinutes(timePoint):
        return int(timePoint[:2]) * 60 + int(timePoint[3:])
    
    minutes = sorted([toMinutes(tp) for tp in timePoints])
    min_diff = 60 * 24
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i-1])
        if min_diff == 0:
            break
            
    min_diff = min(min_diff, minutes[0] + 24 * 60 - minutes[-1])

    return min_diff
    

"""708. Insert into a Sorted Circular Linked List

Given a Circular Linked List node, which is sorted in ascending order, 
write a function to insert a value `insertVal` into the list such that 
it remains a sorted circular list. The given node can be a reference to 
any single node in the list and may not necessarily be the smallest 
value in the circular list.

If there are multiple suitable places for insertion, you may choose any 
place to insert the new value. After the insertion, the circular list 
should remain sorted.

If the list is empty (i.e., the given node is `null`), you should create 
a new single circular list and return the reference to that single node. 
Otherwise, you should return the originally given node.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/01/19/example_1_before_65p.jpg)

```
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
```

**Example 2:**

```
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
```

**Example 3:**

```
Input: head = [1], insertVal = 0
Output: [1,0]
```
 

**Constraints:**

- The number of nodes in the list is in the range `[0, 5 * 104]`.
- `-106 <= Node.val, insertVal <= 106`
"""

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
    if not head:
        node = Node(insertVal)
        node.next = node  # type: ignore
        return node
    
    def _insert(cur, insertVal):
        node = Node(insertVal)
        node.next = cur.next
        cur.next = node
    
    cur = head
    while True:
        if cur.val <= cur.next.val:
            if cur.val <= insertVal <= cur.next.val:
                _insert(cur, insertVal)
                return head
        # find the edge of max -> min or we alredy visited all nodes
        # which indicates all numbers in list are the same but doesn't
        # equal to `insertVal`
        if cur.val > cur.next.val or cur.next == head:
            if insertVal <= cur.next.val or insertVal >= cur.val:
                _insert(cur, insertVal)
                return head
        cur = cur.next


"""791. Custom Sort String

You are given two strings order and s. All the words of `order` are 
**unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` 
was sorted. More specifically, if a character `x` occurs before a 
character `y` in `order`, then `x` should occur before `y` in the 
permuted string.

Return *any permutation of* `s` *that satisfies this property*.


**Example 1:**

```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

**Example 2:**

```
Input: order = "cbafg", s = "abcd"
Output: "cbad"
```


**Constraints:**

- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All the characters of `order` are **unique**.
"""

def customSortString(self, order: str, s: str) -> str:
    ordered = []
    freqs = defaultdict(int)
    order_set = set(order)
    for c in s:
        if c not in order_set:
            ordered.append(c)
        else:
            freqs[c] += 1
    
    for c in order:
        ordered.append(c*freqs[c])
        
    return ''.join(ordered)


"""1411. Number of Ways to Paint N × 3 Grid

You have a `grid` of size `n x 3` and you want to paint each cell of the 
grid with exactly one of the three colors: **Red**, **Yellow,** or 
**Green** while making sure that no two adjacent cells have the same 
color (i.e., no two cells that share vertical or horizontal sides have 
the same color).

Given `n` the number of rows of the grid, return *the number of ways* 
you can paint this `grid`. As the answer may grow large, the answer 
**must be** computed modulo `10^9 + 7`.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/03/26/e1.png)

```
Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
```

**Example 2:**

```
Input: n = 5000
Output: 30228214
```


**Constraints:**

- `n == grid.length`
- `1 <= n <= 5000`
"""

def numOfWays(n: int) -> int:
    '''
    DP - Bottom up w/ space optimized
    
    Observation: for a given row, the pattern of the colors could only
    be either `aba` or `abc`, and the number of ways for each pattern
    depends on the pattern of previous row
    
    define dp[i]: with a grid of `ix3`, in the (i-1)-th row, there will 
    be x ways of aba, y ways of abc
    dp[1]: 6 aba, 6 abc
    dp[i]: x aba, y abc
    dp[i+1]: 3x+2y aba, 2x+2y abc
    '''
    x = y = 6
    for i in range(1, n):
        x, y = 3*x + 2*y, 2*x + 2*y
    return (x + y) % 1000000007
    

"""1891. Cutting Ribbons

You are given an integer array `ribbons`, where `ribbons[i]` represents 
the length of the `ith` ribbon, and an integer `k`. You may cut any of 
the ribbons into any number of segments of **positive integer** lengths, 
or perform no cuts at all.

- For example, if you have a ribbon of length `4`, you can:
  - Keep the ribbon of length `4`,
  - Cut it into one ribbon of length `3` and one ribbon of length `1`,
  - Cut it into two ribbons of length `2`,
  - Cut it into one ribbon of length `2` and two ribbons of length `1`, or
  - Cut it into four ribbons of length `1`.

Your goal is to obtain `k` ribbons of all the **same positive integer 
length**. You are allowed to throw away any excess ribbon as a result of 
cutting.

Return *the **maximum** possible positive integer length that you can 
obtain* `k` *ribbons of**, or* `0` *if you cannot obtain* `k` *ribbons 
of the same length*.


**Example 1:**

```
Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
```

**Example 2:**

```
Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
```

**Example 3:**

```
Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
```


**Constraints:**

- `1 <= ribbons.length <= 105`
- `1 <= ribbons[i] <= 105`
- `1 <= k <= 109`
"""

def maxLength(ribbons: List[int], k: int) -> int:
    # binary search O(NlogN)
    
    total = sum(ribbons)
    if k > total:
        return 0
    
    # optimize the upper bound
    lo, hi = 1, min(total // k, max(ribbons))
    
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if sum(x // mid for x in ribbons) >= k:
            lo = mid
        else:
            hi = mid - 1
    
    return lo


"""2060. Check if an Original String Exists Given Two Encoded Strings

An original string, consisting of lowercase English letters, can be 
encoded by the following steps:

- Arbitrarily **split** it into a **sequence** of some number of 
  **non-empty** substrings.
- Arbitrarily choose some elements (possibly none) of the sequence, 
  and **replace** each with **its length** (as a numeric string).
- **Concatenate** the sequence as the encoded string.

For example, **one way** to encode an original string 
`"abcdefghijklmnop"` might be:

- Split it as a sequence: `["ab", "cdefghijklmn", "o", "p"]`.
- Choose the second and third elements to be replaced by their lengths, 
  respectively. The sequence becomes `["ab", "12", "1", "p"]`.
- Concatenate the elements of the sequence to get the encoded string: 
  `"ab121p"`.

Given two encoded strings `s1` and `s2`, consisting of lowercase English 
letters and digits `1-9` (inclusive), return `true` *if there exists an 
original string that could be encoded as **both*** `s1` *and* `s2`*. 
Otherwise, return* `false`.

**Note**: The test cases are generated such that the number of 
consecutive digits in `s1` and `s2` does not exceed `3`.


**Example 1:**

```
Input: s1 = "internationalization", s2 = "i18n"
Output: true
Explanation: It is possible that "internationalization" was the original string.
- "internationalization" 
  -> Split:       ["internationalization"]
  -> Do not replace any element
  -> Concatenate:  "internationalization", which is s1.
- "internationalization"
  -> Split:       ["i", "nternationalizatio", "n"]
  -> Replace:     ["i", "18",                 "n"]
  -> Concatenate:  "i18n", which is s2
```

**Example 2:**

```
Input: s1 = "l123e", s2 = "44"
Output: true
Explanation: It is possible that "leetcode" was the original string.
- "leetcode" 
  -> Split:      ["l", "e", "et", "cod", "e"]
  -> Replace:    ["l", "1", "2",  "3",   "e"]
  -> Concatenate: "l123e", which is s1.
- "leetcode" 
  -> Split:      ["leet", "code"]
  -> Replace:    ["4",    "4"]
  -> Concatenate: "44", which is s2.
```

**Example 3:**

```
Input: s1 = "a5b", s2 = "c5b"
Output: false
Explanation: It is impossible.
- The original string encoded as s1 must start with the letter 'a'.
- The original string encoded as s2 must start with the letter 'c'.
```


**Constraints:**

- `1 <= s1.length, s2.length <= 40`
- `s1` and `s2` consist of digits `1-9` (inclusive), and lowercase English letters only.
- The number of consecutive digits in `s1` and `s2` does not exceed `3`.
"""

def possiblyEquals(self, s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    
    def gg(s): 
        ans = {int(s)}
        for i in range(1, len(s)): 
            ans |= {x+y for x in gg(s[:i]) for y in gg(s[i:])}
        return ans
    
    @lru_cache(maxsize=None)
    def dfs(i, j, diff):
        if i == m and j == n:
            return diff == 0
        # if either i or j points to digit, move the pointer
        # and update the diff
        elif i < m and s1[i].isdigit():
            ni = i
            while ni < m and s1[ni].isdigit():
                ni += 1
            for offset in gg(s1[i:ni]):
                if dfs(ni, j, diff-offset):
                    return True
        elif j < n and s2[j].isdigit():
            nj = j
            while nj < n and s2[nj].isdigit():
                nj += 1
            for offset in gg(s2[j:nj]):
                if dfs(i, nj, diff+offset):
                    return True
        # at this point, i and j must be both letter
        # or at the end (but not both)
        
        # diff is 0, and both i, j points to letter
        # so they must match
        elif diff == 0:
            if i < m and j < n and s1[i] == s2[j]:
                return dfs(i+1, j+1, diff)
        # diff != 0, then we can take one diff to match a letter
        elif diff > 0:
            if i < m:
                return dfs(i+1, j, diff-1)
        else:
            if j < n:
                return dfs(i, j+1, diff+1)
        
        return False
    
    return dfs(0, 0, 0)


"""2096. Step-By-Step Directions From a Binary Tree Node to Another

You are given the `root` of a **binary tree** with `n` nodes. Each node 
is uniquely assigned a value from `1` to `n`. You are also given an 
integer `startValue` representing the value of the start node `s`, and 
a different integer `destValue` representing the value of the 
destination node `t`.

Find the **shortest path** starting from node `s` and ending at node `t`. 
Generate step-by-step directions of such path as a string consisting of 
only the **uppercase** letters `'L'`, `'R'`, and `'U'`. Each letter 
indicates a specific direction:

- `'L'` means to go from a node to its **left child** node.
- `'R'` means to go from a node to its **right child** node.
- `'U'` means to go from a node to its **parent** node.

Return *the step-by-step directions of the **shortest path** from node* 
`s` *to node* `t`.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/11/15/eg1.png)

```
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/11/15/eg2.png)

```
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
```


**Constraints:**

- The number of nodes in the tree is `n`.
- `2 <= n <= 105`
- `1 <= Node.val <= n`
- All the values in the tree are **unique**.
- `1 <= startValue, destValue <= n`
- `startValue != destValue`
"""

class TreeNode:  # type: ignore
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(
        self, 
        root: Optional[TreeNode], 
        startValue: int, 
        destValue: int
    ) -> str:
        
        part1 = []
        part2 = []
        def dfs(node):
            if not node:
                return False, False
            midStart = node.val == startValue
            midEnd = node.val == destValue
            
            leftStart, leftEnd = dfs(node.left)
            if leftStart and not leftEnd:
                part1.append('U')
            elif not leftStart and leftEnd:
                part2.append('L')
            rightStart, rightEnd = dfs(node.right)
            if rightStart and not rightEnd:
                part1.append('U')
            elif not rightStart and rightEnd:
                part2.append('R')
            
            start = leftStart | rightStart | midStart
            end = leftEnd | rightEnd | midEnd
            
            return start, end
        
        dfs(root)
        
        return ''.join(part1 + list(reversed(part2)))


"""2259. Remove Digit From Number to Maximize Result

You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of 
digit from number such that the value of the resulting string in decimal 
form is maximized. The test cases are generated such that digit occurs 
at least once in number.

 
Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
Example 3:

Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".
 

Constraints:

* 2 <= number.length <= 100
* number consists of digits from '1' to '9'.
* digit is a digit from '1' to '9'.
* digit occurs at least once in number.
"""

def removeDigit(self, number: str, digit: str) -> str:
    removed = []
    flag = False
    last = max(i for i, num in enumerate(number) if num == digit)
    for i, num in enumerate(number):
        if num != digit:
            removed.append(num)
        else:
            if not flag and (i == last or num < number[i+1]):
                flag = True
            else:
                removed.append(num)            
        
    return ''.join(removed)


"""2260. Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents the value
of the ith card. A pair of cards are matching if the cards have the same 
value.

Return the minimum number of consecutive cards you have to pick up to 
have a pair of matching cards among the picked cards. If it is impossible 
to have matching cards, return -1.
 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

* 1 <= cards.length <= 105
* 0 <= cards[i] <= 106
"""

def minimumCardPickup(self, cards: List[int]) -> int:
    val2idx = {}
    min_size = len(cards) + 1
    for i, card in enumerate(cards):
        if card in val2idx:
            min_size = min(min_size, i - val2idx[card] + 1)
        val2idx[card] = i
    return min_size if min_size != len(cards) + 1 else -1


"""2261. K Divisible Elements Subarrays

Given an integer array nums and two integers k and p, return the number 
of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.
 

Example 1:

Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11
Explanation:
The elements at indices 0, 3, and 4 are divisible by p = 2.
The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation:
All element of nums are divisible by p = 1.
Also, every subarray of nums will have at most 4 elements that are divisible by 1.
Since all subarrays are distinct, the total number of subarrays satisfying all the constraints is 10.
 

Constraints:

* 1 <= nums.length <= 200
* 1 <= nums[i], p <= 200
* 1 <= k <= nums.length
"""

def countDistinct(self, nums: List[int], k: int, p: int) -> int:
    # hash
    # O(N^2)
    visited = set()
    count = 0
    
    for i in range(len(nums)):
        hash_value = 0
        cur_k = 0
        for j in range(i, len(nums)):
            if nums[j] % p == 0:
                cur_k += 1
            if cur_k > k:
                break
            # need to pick 201 as the max of nums could be 200
            hash_value = hash_value * 201 + nums[j]
            if hash_value not in visited:
                count += 1
                visited.add(hash_value)
    return count


"""2262. Total Appeal of A String

The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct 
characters: 'a', 'b', and 'c'.

Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.
 

Example 1:

Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
The total sum is 5 + 7 + 7 + 6 + 3 = 28.
Example 2:

Input: s = "code"
Output: 20
Explanation: The following are the substrings of "code":
- Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
- Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
- Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 4: "code" has an appeal of 4. The sum is 4.
The total sum is 4 + 6 + 6 + 4 = 20.
 

Constraints:

* 1 <= s.length <= 105
* s consists of lowercase English letters.
"""

def appealSum(self, s: str) -> int:
    # dp
    # f(i): appeal for all substr end at i
    # f(i) = f(i-1) + (i - last_index[s[i]])
    
    last_index = defaultdict(lambda: -1)
    last_appeal = total_appeal = 0
    for i, char in enumerate(s):
        last_appeal += i - last_index[char]
        total_appeal += last_appeal
        last_index[char] = i
    
    return total_appeal


"""2264. Largest 3-Same-Digit Number in String

You are given a string `num` representing a large integer. An integer is 
**good** if it meets the following conditions:

- It is a **substring** of `num` with length `3`.
- It consists of only one unique digit.

Return *the **maximum good** integer as a **string** or an empty string* 
`""` *if no such integer exists*.

Note:

- A **substring** is a contiguous sequence of characters within a string.
- There may be **leading zeroes** in `num` or a good integer.


**Example 1:**

```
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
```

**Example 2:**

```
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
```

**Example 3:**

```
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
```


**Constraints:**

- `3 <= num.length <= 1000`
- `num` only consists of digits.
"""

def largestGoodInteger(num: str) -> str:
    res = ""
    for i in range(len(num)-2):
        if num[i] == num[i+1] == num[i+2]:
            res = max(res, num[i:i+3])
    return res


"""2265. Count Nodes Equal to Average of Subtree

Given the `root` of a binary tree, return *the number of nodes where the 
value of the node is equal to the **average** of the values in its 
**subtree***.

**Note:**

- The **average** of `n` elements is the **sum** of the `n` elements divided by `n` and **rounded down** to the nearest integer.
- A **subtree** of `root` is a tree consisting of `root` and all of its descendants.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png)

```
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png)

```
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
```


**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 1000`
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfSubtree(root: Optional[TreeNode]) -> int:
    
    count = 0
    def dfs(node):
        nonlocal count
        if node is None: return (0, 0)
        left_sum, left_cnt = dfs(node.left)
        right_sum, right_cnt = dfs(node.right)
        total_sum = left_sum + node.val + right_sum
        total_cnt = left_cnt + 1 + right_cnt
        if total_sum // total_cnt == node.val:
            count += 1
        return (total_sum, total_cnt)
    
    dfs(root)
    return count


"""2266. Count Number of Texts

Alice is texting Bob using her phone. The **mapping** of digits to 
letters is shown in the figure below.

![img](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

In order to **add** a letter, Alice has to **press** the key of the 
corresponding digit `i` times, where `i` is the position of the letter 
in the key.

- For example, to add the letter `'s'`, Alice has to press `'7'` four times. Similarly, to add the letter `'k'`, Alice has to press `'5'` twice.
- Note that the digits `'0'` and `'1'` do not map to any letters, so Alice **does not** use them.

However, due to an error in transmission, Bob did not receive Alice's 
text message but received a **string of pressed keys** instead.

- For example, when Alice sent the message `"bob"`, Bob received the string `"2266622"`.

Given a string `pressedKeys` representing the string received by Bob, 
return *the **total number of possible text messages** Alice could have 
sent*.

Since the answer may be very large, return it **modulo** `109 + 7`.


**Example 1:**

```
Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
```

**Example 2:**

```
Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.
```


**Constraints:**

- `1 <= pressedKeys.length <= 105`
- `pressedKeys` only consists of digits from `'2'` - `'9'`.
"""

def countTexts(self, pressedKeys: str) -> int:
    # space can be optimized to O(4) / O(1) as
    # the dependency is at most 4 (a key can be
    # at most repeatly pressed 4 times for a char)
    
    n = len(pressedKeys)
    dp = [0] * n
    
    for i in range(n):
        if i == 0:
            dp[i] = 1
        else:
            cur_key = pressedKeys[i]
            max_press = 4 if cur_key in '79' else 3 
            for j in range(max_press):
                start = i - j
                if start < 0 or pressedKeys[start] != cur_key:
                    break
                if start == 0: 
                    dp[i] += 1
                else:
                    dp[i] += dp[start-1]
    
    return dp[-1] % 1000000007


"""2267. Check if There Is a Valid Parentheses String Path

A parentheses string is a **non-empty** string consisting only of `'('` 
and `')'`. It is **valid** if **any** of the following conditions is 
**true**:

- It is `()`.
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
- It can be written as `(A)`, where `A` is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A **valid 
parentheses string path** in the grid is a path satisfying **all** of 
the following conditions:

- The path starts from the upper left cell `(0, 0)`.
- The path ends at the bottom-right cell `(m - 1, n - 1)`.
- The path only ever moves **down** or **right**.
- The resulting parentheses string formed by the path is **valid**.

Return `true` *if there exists a **valid parentheses string path** in 
the grid.* Otherwise, return `false`.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png)

```
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png)

```
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
```


**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either `'('` or `')'`.
"""

def hasValidPath(self, grid: List[List[str]]) -> bool:
    # space can be further optimized to O(M) - only the prev row needed
    if grid[-1][-1] == '(' or grid[0][0] == ')':
        return False
    
    m, n = len(grid), len(grid[0])
    dp = [[set() for _ in range(n)] for _ in range(m)]
    dp[0][0].add(1)
    
    for i in range(m):
        for j in range(n):
            cur = 1 if grid[i][j] == '(' else -1
            top = dp[i-1][j] if i > 0 else []
            for pre_cnt in top:
                # pruning here: if the cnt > m+n-i-j-2,
                # then there won't be enough cells left
                # to offset the cnt so that the cnt 
                # could be 0 at the end
                if 0 <= pre_cnt+cur <= m+n-i-j-2:
                    dp[i][j].add(pre_cnt+cur)
            left = dp[i][j-1] if j > 0 else []
            for pre_cnt in left:
                if 0 <= pre_cnt+cur <= m+n-i-j-2:
                    dp[i][j].add(pre_cnt+cur)

    return 0 in dp[-1][-1]


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
    
    
"""2278. Percentage of Letter in String

Given a string `s` and a character `letter`, return *the **percentage** 
of characters in* `s` *that equal* `letter` ***rounded down** to the 
nearest whole percent.*


**Example 1:**

```
Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
```

**Example 2:**

```
Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
```


**Constraints:**

- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter.
"""

def percentageLetter(s: str, letter: str) -> int:
    return int(len([c for c in s if c == letter]) / len(s) * 100)


"""2279. Maximum Bags With Full Capacity of Rocks

You have `n` bags numbered from `0` to `n - 1`. You are given two 
**0-indexed** integer arrays `capacity` and `rocks`. The `ith` bag can 
hold a maximum of `capacity[i]` rocks and currently contains `rocks[i]` 
rocks. You are also given an integer `additionalRocks`, the number of 
additional rocks you can place in **any** of the bags.

Return *the **maximum** number of bags that could have full capacity 
after placing the additional rocks in some bags.*


**Example 1:**

```
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
```

**Example 2:**

```
Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
Output: 3
Explanation:
Place 8 rocks in bag 0 and 2 rocks in bag 2.
The number of rocks in each bag are now [10,2,2].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that we did not use all of the additional rocks.
```


**Constraints:**

- `n == capacity.length == rocks.length`
- `1 <= n <= 5 * 104`
- `1 <= capacity[i] <= 109`
- `0 <= rocks[i] <= capacity[i]`
- `1 <= additionalRocks <= 109`
"""

def maximumBags(
    capacity: List[int], 
    rocks: List[int], 
    additionalRocks: int
) -> int:
    remains = [c-r for c, r in zip(capacity, rocks)]
    remains.sort()
    
    num_full = 0
    for i in range(len(capacity)):
        if remains[i] == 0:
            num_full += 1
        elif remains[i] <= additionalRocks:
            additionalRocks -= remains[i]
            num_full += 1
        else:
            break
    
    return num_full


"""2280. Minimum Lines to Represent a Line Chart

You are given a 2D integer array `stockPrices` where `stockPrices[i] = 
[dayi, pricei]` indicates the price of the stock on day `dayi` is 
`pricei`. A **line chart** is created from the array by plotting the 
points on an XY plane with the X-axis representing the day and the 
Y-axis representing the price and connecting adjacent points. One such 
example is shown below:

![img](https://assets.leetcode.com/uploads/2022/03/30/1920px-pushkin_population_historysvg.png)

Return *the **minimum number of lines** needed to represent the line chart*.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/03/30/ex0.png)

```
Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
Output: 3
Explanation:
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/03/30/ex1.png)

```
Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
Output: 1
Explanation:
As shown in the diagram above, the line chart can be represented with a single line.
```


**Constraints:**

- `1 <= stockPrices.length <= 105`
- `stockPrices[i].length == 2`
- `1 <= dayi, pricei <= 109`
- All `dayi` are **distinct**.
"""

def minimumLines(stockPrices: List[List[int]]) -> int:  # type: ignore
    """Greatest Common Divisor"""
    stockPrices.sort()
    n = len(stockPrices)
    if n==0 or n==1: return 0
    
    ans = n - 1
    for i in range(2, n):
        # check if the slope is same as prev
        # if yes, num of lines can be reduced by 1
        # to deal with the floating precision issue,
        # use greatest common divider
        x1, y1 = stockPrices[i-2]
        x2, y2 = stockPrices[i-1]
        x3, y3 = stockPrices[i]
        dx1, dy1 = x2-x1, y2-y1
        dx2, dy2 = x3-x2, y3-y2
        gcd1 = gcd(dx1, dy1)
        dx1, dy1 = dx1 / gcd1, dy1 / gcd1
        gcd2 = gcd(dx2, dy2)
        dx2, dy2 = dx2 / gcd2, dy2 / gcd2
        if dx1 == dx2 and dy1 == dy2: ans -= 1
        
    return ans

def minimumLines(stockPrices: List[List[int]]) -> int:
    """Cross multiplication"""
    stockPrices.sort()
    n = len(stockPrices)
    if n==0 or n==1: return 0
    
    ans = n - 1
    for i in range(2, n):
        # y1 / x1 == y2 / x2
        # <==> y1 *x2 = x1 * y2
        y1 = stockPrices[i][1] - stockPrices[i-1][1]
        x1 = stockPrices[i][0] - stockPrices[i-1][0]
        y2 = stockPrices[i-1][1] - stockPrices[i-2][1]
        x2 = stockPrices[i-1][0] - stockPrices[i-2][0]
        
        if y1 * x2 == y2 * x1:
            ans -= 1
        
    return ans


"""2281. Sum of Total Strength of Wizards

As the ruler of a kingdom, you have an army of wizards at your command.

You are given a **0-indexed** integer array `strength`, where 
`strength[i]` denotes the strength of the `ith` wizard. For a 
**contiguous** group of wizards (i.e. the wizards' strengths form a 
**subarray** of `strength`), the **total strength** is defined as the 
**product** of the following two values:

- The strength of the **weakest** wizard in the group.
- The **total** of all the individual strengths of the wizards in the group.

Return *the **sum** of the total strengths of **all** contiguous groups 
of wizards*. Since the answer may be very large, return it **modulo** 
`109 + 7`.

A **subarray** is a contiguous **non-empty** sequence of elements 
within an array.


**Example 1:**

```
Input: strength = [1,3,1,2]
Output: 44
Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.
```

**Example 2:**

```
Input: strength = [5,4,6]
Output: 213
Explanation: The following are all the contiguous groups of wizards: 
- [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
- [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
- [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
- [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.
```


**Constraints:**

- `1 <= strength.length <= 105`
- `1 <= strength[i] <= 109`
"""

def totalStrength(self, s: List[int]) -> int:
    """
    Idea is similar to LC84. Largest Rectangle in Histogram. 
    For each bar (value), find the sum of subarrays where the bar is
    the minimum value. define l, r as the leftmost, and rightmost index
    which all values between l and r >= bar (we can use a mono stack
    to do this)
    
    the key part is how to calculate the sum of subarrays given i (index
    of bar), l, r. the solution is presum of presum
    
    define pp(i) = presum of presum
    
    example: [1,2,5,3,4,5]
    for i == 2, the range of subarray is [5,3,4,5]
    sum of subarrays are:
        3
        3 4      = pp(5) - pp(2) - 3 * (1,2,5)
        3 4 5
        
        5 3
        5 3 4    = pp(5) - pp(2) - 3 * (1,2)
        5 3 4 5
        
        3 * (1,2) + 3 * (1,2,5) = 3 * (pp(2) - pp(stack[-1]-1 or -1)
    
    summary:
    
    sum of subarrays give i, l, r =
    (i-l+1) * (pp(r) - pp(i-1)) - (r-i+1) * (pp(l) - pp(stack[-1]-1 or -1))
    pp(-1) = 0
                
    """
    n = len(s)
    
    # presum of presum
    pp = list(accumulate(accumulate(s), initial=0))  # type: ignore
    print(pp)
    stack = []
    total = 0
    for cur in range(n+1):
        cur_num = s[cur] if cur < n else float('-inf')
        while stack and cur_num <= s[stack[-1]]:
            i = stack.pop()
            l = stack[-1]+1 if stack else 0
            r = cur-1
            total += (
                (i-l+1) * (pp[r+1] - pp[i]) - (r-i+1) * (pp[i] - pp[max(l-1,0)])
            ) * s[i]
        stack.append(cur)
    return total % (1000000007)


"""2283. Check if Number Has Equal Digit Count and Digit Value

You are given a **0-indexed** string `num` of length `n` consisting of 
digits.

Return `true` *if for **every** index* `i` *in the range* `0 <= i < n`*, 
the digit* `i` *occurs* `num[i]` *times in* `num`*, otherwise return* `false`.


**Example 1:**

```
Input: num = "1210"
Output: true
Explanation:
num[0] = '1'. The digit 0 occurs once in num.
num[1] = '2'. The digit 1 occurs twice in num.
num[2] = '1'. The digit 2 occurs once in num.
num[3] = '0'. The digit 3 occurs zero times in num.
The condition holds true for every index in "1210", so return true.
```

**Example 2:**

```
Input: num = "030"
Output: false
Explanation:
num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
num[2] = '0'. The digit 2 occurs zero times in num.
The indices 0 and 1 both violate the condition, so return false.
```


**Constraints:**

- `n == num.length`
- `1 <= n <= 10`
- `num` consists of digits.
"""

def digitCount(num: str) -> bool:
    counter = Counter(num)
    for i, c in enumerate(num):
        if counter[str(i)] != int(c):
            return False
    return True


"""2284. Sender With Largest Word Count

You have a chat log of `n` messages. You are given two string arrays 
`messages` and `senders` where `messages[i]` is a **message** sent by 
`senders[i]`.

A **message** is list of **words** that are separated by a single space 
with no leading or trailing spaces. The **word count** of a sender is 
the total number of **words** sent by the sender. Note that a sender may 
send more than one message.

Return *the sender with the **largest** word count*. If there is more 
than one sender with the largest word count, return *the one with the 
**lexicographically largest** name*.

**Note:**

- Uppercase letters come before lowercase letters in lexicographical order.
- `"Alice"` and `"alice"` are distinct.


**Example 1:**

```
Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day 
Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
Output: "Alice"
Explanation: Alice sends a total of 2 + 3 = 5 words.
userTwo sends a total of 2 words.
userThree sends a total of 3 words.
Since Alice has the largest word count, we return "Alice".
```

**Example 2:**

```
Input: messages = ["How is leetcode for everyone","Leetcode is useful 
for practice"], senders = ["Bob","Charlie"]
Output: "Charlie"
Explanation: Bob sends a total of 5 words.
Charlie sends a total of 5 words.
Since there is a tie for the largest word count, we return the sender 
with the lexicographically larger name, Charlie.
```


**Constraints:**

- `n == messages.length == senders.length`
- `1 <= n <= 104`
- `1 <= messages[i].length <= 100`
- `1 <= senders[i].length <= 10`
- `messages[i]` consists of uppercase and lowercase English letters and `' '`.
- All the words in `messages[i]` are separated by **a single space**.
- `messages[i]` does not have leading or trailing spaces.
- `senders[i]` consists of uppercase and lowercase English letters only.
"""

def largestWordCount(messages: List[str], senders: List[str]) -> str:
    counts = defaultdict(int)
    for msg, sndr in zip(messages, senders):
        counts[sndr] += len(msg.split(' '))
    
    counts = list(counts.items())
    counts.sort(key = lambda x: (x[1], x[0]))
    
    return counts[-1][0]


"""2285. Maximum Total Importance of Roads

You are given an integer `n` denoting the number of cities in a country. 
The cities are numbered from `0` to `n - 1`.

You are also given a 2D integer array `roads` where `roads[i] = [ai, bi]` 
denotes that there exists a **bidirectional** road connecting cities `ai` 
and `bi`.

You need to assign each city with an integer value from `1` to `n`, 
where each value can only be used **once**. The **importance** of a road 
is then defined as the **sum** of the values of the two cities it connects.

Return *the **maximum total importance** of all roads possible after 
assigning the values optimally.*


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/04/07/ex1drawio.png)

```
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/04/07/ex2drawio.png)

```
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.
```


**Constraints:**

- `2 <= n <= 5 * 104`
- `1 <= roads.length <= 5 * 104`
- `roads[i].length == 2`
- `0 <= ai, bi <= n - 1`
- `ai != bi`
- There are no duplicate roads.
"""

def maximumImportance(n: int, roads: List[List[int]]) -> int:
    indegree = defaultdict(int)
    for a, b in roads:
        indegree[a] += 1
        indegree[b] += 1
    res = 0
    for i, (city, cnt) in enumerate(
        sorted(indegree.items(), key=lambda x: -x[1])
    ):
        res += cnt * (n-i)
    
    return res


"""2286. Booking Concert Tickets in Groups

A concert hall has `n` rows numbered from `0` to `n - 1`, each with `m` 
seats, numbered from `0` to `m - 1`. You need to design a ticketing 
system that can allocate seats in the following cases:

- If a group of `k` spectators can sit **together** in a row.
- If **every** member of a group of `k` spectators can get a seat. They 
may or **may not** sit together.

Note that the spectators are very picky. Hence:

- They will book seats only if each member of their group can get a seat 
with row number **less than or equal** to `maxRow`. `maxRow` can 
**vary** from group to group.
- In case there are multiple rows to choose from, the row with the 
**smallest** number is chosen. If there are multiple seats to choose in 
the same row, the seat with the **smallest** number is chosen.

Implement the `BookMyShow` class:

- `BookMyShow(int n, int m)` Initializes the object with `n` as number 
of rows and `m` as number of seats per row.
- `int[] gather(int k, int maxRow)` Returns an array of length `2` 
denoting the row and seat number (respectively) of the **first seat** 
being allocated to the `k` members of the group, who must sit 
**together**. In other words, it returns the smallest possible `r` and 
`c` such that all `[c, c + k - 1]` seats are valid and empty in row `r`, 
and `r <= maxRow`. Returns `[]` in case it is **not possible** to 
allocate seats to the group.
- `boolean scatter(int k, int maxRow)` Returns `true` if all `k` members 
of the group can be allocated seats in rows `0` to `maxRow`, who may or 
**may not** sit together. If the seats can be allocated, it allocates `k` 
seats to the group with the **smallest** row numbers, and the smallest 
possible seat numbers in each row. Otherwise, returns `false`.


**Example 1:**

```
Input
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
Output
[null, [0, 0], [], true, false]

Explanation
BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
                  // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
                  // There is only 1 seat left in row 0,
                  // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
                   // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
                   // There are only 2 seats left in the hall.
```


**Constraints:**

- `1 <= n <= 5 * 104`
- `1 <= m, k <= 109`
- `0 <= maxRow <= n - 1`
- At most `5 * 104` calls **in total** will be made to `gather` and `scatter`.
"""

class SegmentTree:
    '''array based implementation'''
    def __init__(self, n, m):
        # init is question custimized
        size = 2 ** (n*2).bit_length()
        self.tree = [None] * size
        # Segment Tree 1-index
        self.build(1, 0, n-1, m)
        
    def build(self, pos, rLeft, rRight, m):
        if rLeft == rRight:
            self.tree[pos] = [m, m]
        else:
            rMid = (rLeft + rRight) // 2
            self.build(2*pos, rLeft, rMid, m)
            self.build(2*pos+1, rMid+1, rRight, m)
            self.tree[pos] = [
                self.tree[2*pos][0] + self.tree[2*pos+1][0], 
                max(self.tree[2*pos][1], self.tree[2*pos+1][1])
            ]
    
    def update(self, pos, rLeft, rRight, idx, increVal):
        if rLeft > idx or rRight < idx:
            return 
        elif rLeft == rRight:
            self.tree[pos][0] += increVal
            self.tree[pos][1] += increVal
        else:
            rMid = (rLeft + rRight) // 2
            self.update(pos*2, rLeft, rMid, idx, increVal)
            self.update(pos*2+1, rMid+1, rRight, idx, increVal)
            self.tree[pos][0] = self.tree[2*pos][0] + self.tree[2*pos+1][0]
            self.tree[pos][1] = max(self.tree[2*pos][1], self.tree[2*pos+1][1])
        
    def query(self, pos, rLeft, rRight, qLeft, qRight):
        if rLeft > qRight or rRight < qLeft:
            return [0, 0]
        elif rLeft >= qLeft and rRight <= qRight:
            return self.tree[pos]
        else:
            rMid = (rLeft + rRight) // 2
            leftSum, leftMax = self.query(pos*2, rLeft, rMid, qLeft, qRight)
            rightSum, rightMax = self.query(pos*2+1, rMid+1, rRight, qLeft, qRight)
            return [leftSum+rightSum, max(leftMax, rightMax)]
        
    def querySum(self, pos, rLeft, rRight, qLeft, qRight):
        return self.query(pos, rLeft, rRight, qLeft, qRight)[0]
    
    def queryMax(self, pos, rLeft, rRight, qLeft, qRight):
        return self.query(pos, rLeft, rRight, qLeft, qRight)[1]
        
    def getLowestGreater(self, pos, rLeft, rRight, val):
        '''return the lowest index in the range [rLeft, rRight]
        where max of the range [rLeft, index] >= val
        '''
        if self.tree[pos][1] < val:
            return -1
        while rLeft < rRight:
            rMid = (rLeft + rRight) // 2
            if self.tree[pos*2][1] >= val:
                pos = pos*2
                rRight = rMid
            else:
                pos = pos*2+1
                rLeft = rMid+1
        return rLeft

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.st = SegmentTree(n, m)
        self.remain = [m] * n
        self.n = n
        self.m = m
        self.first_non_empty_row = 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self.st.getLowestGreater(1, 0, self.n-1, k)
        if row == -1 or row > maxRow: return []
        self.remain[row] -= k
        self.st.update(1, 0, self.n-1, row, -k)
        return [row, self.m-self.remain[row]-k]
        
    def scatter(self, k: int, maxRow: int) -> bool:
        if self.first_non_empty_row > maxRow: return False
        if self.st.querySum(1, 0, self.n-1, self.first_non_empty_row, maxRow) < k:
            return False
        i = self.first_non_empty_row
        while k > 0:
            booked = min(self.remain[i], k)
            self.remain[i] -= booked
            k -= booked
            self.st.update(1, 0, self.n-1, i, -booked)
            if self.remain[i] == 0: i += 1
        self.first_non_empty_row = i
        return True
    

"""2287. Rearrange Characters to Make Target String

You are given two **0-indexed** strings `s` and `target`. You can take 
some letters from `s` and rearrange them to form new strings.

Return *the **maximum** number of copies of* `target` *that can be 
formed by taking letters from* `s` *and rearranging them.*


**Example 1:**

```
Input: s = "ilovecodingonleetcode", target = "code"
Output: 2
Explanation:
For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
We can make at most two copies of "code", so we return 2.
```

**Example 2:**

```
Input: s = "abcba", target = "abc"
Output: 1
Explanation:
We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
We can make at most one copy of "abc", so we return 1.
Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".
```

**Example 3:**

```
Input: s = "abbaccaddaeea", target = "aaaaa"
Output: 1
Explanation:
We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
We can make at most one copy of "aaaaa", so we return 1.
```


**Constraints:**

- `1 <= s.length <= 100`
- `1 <= target.length <= 10`
- `s` and `target` consist of lowercase English letters.
"""

def rearrangeCharacters(s: str, target: str) -> int:
    s_cnt = Counter(s)
    t_cnt = Counter(target)
    res = len(s)
    for tc in t_cnt:
        res = min(res, s_cnt[tc] // t_cnt[tc])
    return res
    

"""2288. Apply Discount to Prices

A **sentence** is a string of single-space separated words where each 
word can contain digits, lowercase letters, and the dollar sign `'$'`. 
A word represents a **price** if it is a non-negative real number 
preceded by a dollar sign.

- For example, `"$100"`, `"$23"`, and `"$6.75"` represent prices while 
`"100"`, `"$"`, and `"2$3"` do not.

You are given a string `sentence` representing a sentence and an integer 
`discount`. For each word representing a price, apply a discount of 
`discount%` on the price and **update** the word in the sentence. All 
updated prices should be represented with **exactly two** decimal places.

Return *a string representing the modified sentence*.


**Example 1:**

```
Input: sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50
Output: "there are $0.50 $1.00 and 5$ candies in the shop"
Explanation: 
The words which represent prices are "$1" and "$2". 
- A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50".
- A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a price, we replace "$2" with "$1.00".
```

**Example 2:**

```
Input: sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100
Output: "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
Explanation: 
Applying a 100% discount on any price will result in 0.
The words representing prices are "$3", "$5", "$6", and "$9".
Each of them is replaced by "$0.00".
```


**Constraints:**

- `1 <= sentence.length <= 105`
- `sentence` consists of lowercase English letters, digits, `' '`, and `'$'`.
- `sentence` does not have leading or trailing spaces.
- All words in `sentence` are separated by a single space.
- All prices will be **positive** integers without leading zeros.
- All prices will have **at most** `10` digits.
- `0 <= discount <= 100`
"""

def discountPrices(sentence: str, discount: int) -> str:
    words = sentence.split(' ')
    updated = []
    discount = (100 - discount) / 100  # type: ignore
    
    for word in words:
        if word[0]=='$' and word[1:].isnumeric():
            new_word = '${:.2f}'.format(round(float(word[1:]) * discount, 2))
        else: 
            new_word = word
        updated.append(new_word)
        
    return ' '.join(updated)


"""2289. Steps to Make Array Non-decreasing

You are given a **0-indexed** integer array `nums`. In one step, 
**remove** all elements `nums[i]` where `nums[i - 1] > nums[i]` for all 
`0 < i < nums.length`.

Return *the number of steps performed until* `nums` *becomes a 
**non-decreasing** array*.


**Example 1:**

```
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
```

**Example 2:**

```
Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
```


**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
"""

def totalSteps(nums: List[int]) -> int:
    '''
    key observations
    + need to look at the array from right to left
    + a number at index `i` need to be remvoed if there is a 
        number at index `j` on its left (j < i) that > it
    + use a monotomic stack to track the count of numbers that
        a number can eat which is the number of steps needed
    '''
    res = 0
    nums.reverse()
    stack = [(nums[0], 0)]
    for i in range(1, len(nums)):
        cnt = 0
        while stack and stack[-1][0] < nums[i]:
            # cur number at i can eat the number at top of the stack
            # need one more step to eat
            # note that, the number to be eat could also potentially
            # eat other numbers, and if that takes more steps,
            # we need to take the maximum
            cnt = max(cnt+1, stack.pop()[1])
        stack.append((nums[i], cnt))  # type: ignore
        res = max(res, cnt)
    return res


"""2290. Minimum Obstacle Removal to Reach Corner

You are given a **0-indexed** 2D integer array `grid` of size `m x n`. 
Each cell has one of two values:

- `0` represents an **empty** cell,
- `1` represents an **obstacle** that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return *the **minimum** number of **obstacles** to **remove** so you 
can move from the upper left corner* `(0, 0)` *to the lower right 
corner* `(m - 1, n - 1)`.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/04/06/example1drawio-1.png)

```
Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/04/06/example1drawio.png)

```
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
```


**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 105`
- `2 <= m * n <= 105`
- `grid[i][j]` is either `0` **or** `1`.
- `grid[0][0] == grid[m - 1][n - 1] == 0`
"""

def minimumObstacles(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    queue = [(0, 0, 0)]
    #S = set()
    dist = defaultdict(lambda: m*n)
    dist[(0,0)] = 0
    
    while queue:
        _, i, j = heapq.heappop(queue)
        #if (i, j) in S:
        #    continue
        #S.add((i, j))
        for ni, nj in zip((i, i, i-1, i+1), (j-1, j+1, j, j)):
            if 0<=ni<m and 0<=nj<n and dist[(ni, nj)] > dist[(i, j)] + grid[ni][nj]:
                dist[(ni, nj)] = dist[(i, j)] + grid[ni][nj]
                if (ni, nj) == (m-1, n-1):
                    return dist[(ni, nj)]
                heapq.heappush(queue, (dist[(ni, nj)], ni, nj))
    return -1