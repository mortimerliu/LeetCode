import bisect
from functools import lru_cache
import heapq
from itertools import accumulate
from math import gcd
from operator import itemgetter
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Tuple
from sortedcontainers import SortedList


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


"""329. Longest Increasing Path in a Matrix

Given an `m x n` integers `matrix`, return *the length of the longest 
increasing path in* `matrix`.

From each cell, you can either move in four directions: left, right, up, 
or down. You **may not** move **diagonally** or move **outside the 
boundary** (i.e., wrap-around is not allowed).


**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```


**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 231 - 1`
"""

def longestIncreasingPath(matrix: List[List[int]]) -> int:  # type: ignore
    # DP with sort
    m, n = len(matrix), len(matrix[0])
    nodes = sorted(
        [(i, j) for i in range(m) for j in range(n)], 
        key=lambda x: matrix[x[0]][x[1]]
    )
    rval = 1
    dist = [[1] * n for _ in range(m)]
    
    for i, j in nodes:
        rval = max(rval, dist[i][j])
        for ni, nj in zip((i, i, i-1, i+1), (j-1, j+1, j, j)):
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                dist[ni][nj] = max(dist[ni][nj], dist[i][j] + 1)
                
    return rval

def longestIncreasingPath(matrix: List[List[int]]) -> int:  # type: ignore
    # this is a DP problem with topological sort
    
    m, n = len(matrix), len(matrix[0])
    
    # treat the matrix as a graph, connect node a -> node b only if 
    # val(a) < val(b), then traverse the graph using topological sort
    # we can save the adj
    adj = defaultdict(list)
    indegree = defaultdict(int)
    for i in range(m):
        for j in range(n):
            for ni, nj in zip((i, i, i-1, i+1), (j-1, j+1, j, j)):
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    adj[(i, j)].append((ni, nj))
                    indegree[(ni, nj)] += 1
    
    rval = 1
    dist = [[1] * n for _ in range(m)]
    queue = [(i, j) for i in range(m) for j in range(n) if indegree[(i, j)] == 0]
    
    while queue:
        i, j = queue.pop()
        rval = max(rval, dist[i][j])
        for ni, nj in adj[(i, j)]:
            dist[ni][nj] = max(dist[ni][nj], dist[i][j] + 1)
            indegree[(ni, nj)] -= 1
            if indegree[(ni, nj)] == 0:
                queue.append((ni, nj))
    return rval

def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    # this is a DP problem
    
    m, n = len(matrix), len(matrix[0])
    
    # treat the matrix as a graph, connect node a -> node b only if 
    # val(a) < val(b), then traverse the graph using topological sort
    indegree = defaultdict(int)
    for i in range(m):
        for j in range(n):
            for ni, nj in zip((i, i, i-1, i+1), (j-1, j+1, j, j)):
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    indegree[(ni, nj)] += 1
    
    # we can further optimize the answer by observing that the longest
    # increasing path essentially equals to number of layers in the DAG
    # (first layer: zero indegree, second layer: new zero indegree after
    # remove first layer) - peeling the onion
    # this way, we don't need to keep track the answer for each cell
    rval = 0
    queue = [(i, j) for i in range(m) for j in range(n) if indegree[(i, j)] == 0]
    
    while queue:
        new_layer = []
        for i, j in queue:
            for ni, nj in zip((i, i, i-1, i+1), (j-1, j+1, j, j)):
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    indegree[(ni, nj)] -= 1
                    if indegree[(ni, nj)] == 0:
                        new_layer.append((ni, nj))
        queue = new_layer
        rval += 1
    return rval


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


"""562. Longest Line of Consecutive One in Matrix

Given an `m x n` binary matrix `mat`, return *the length of the longest 
line of consecutive one in the matrix*.

The line could be horizontal, vertical, diagonal, or anti-diagonal.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/04/24/long1-grid.jpg)

```
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/04/24/long2-grid.jpg)

```
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
```


**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 104`
- `1 <= m * n <= 104`
- `mat[i][j]` is either `0` or `1`.
"""

def longestLine(self, mat: List[List[int]]) -> int:
    """
    DFS -> DP 
    def f(i, j, dir) = longest path ending at (i, j) with
    direction dir
    
    we have 8 directions in total, due to symmetric, we only
    need to check 4
    
    # longest path ending at (i, j) in 4 directions
    g(i, j) = ( 
        f(i, j, diag), 
        f(i, j, right), 
        f(i, j, anti_diag), 
        f(i, j, down)
    )
    
    Space can be optimzied to O(m)
    """
    
    m, n = len(mat), len(mat[0])
    g = [[[0, 0, 0, 0] for _ in range(n+1)] for i in range(m+2)]
    
    rval = 0
    # go thru column by column
    for j in range(n):
        for i in range(m):
            if mat[i][j] == 0:
                continue
            g[i+1][j+1][0] = g[i][j][0] + 1
            g[i+1][j+1][1] = g[i+1][j][1] + 1
            g[i+1][j+1][2] = g[i+2][j][2] + 1
            g[i+1][j+1][3] = g[i][j+1][3] + 1
            rval = max(rval, max(g[i+1][j+1]))
    
    return rval
    

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


"""715. Range Module

A Range Module is a module that tracks ranges of numbers. Design a data 
structure to track the ranges represented as **half-open intervals** and 
query about them.

A **half-open interval** `[left, right)` denotes all the real numbers 
`x` where `left <= x < right`.

Implement the `RangeModule` class:

- `RangeModule()` Initializes the object of the data structure.
- `void addRange(int left, int right)` Adds the **half-open interval** 
`[left, right)`, tracking every real number in that interval. Adding an 
interval that partially overlaps with currently tracked numbers should 
add any numbers in the interval `[left, right)` that are not already 
tracked.
- `boolean queryRange(int left, int right)` Returns `true` if every real 
number in the interval `[left, right)` is currently being tracked, and 
`false` otherwise.
- `void removeRange(int left, int right)` Stops tracking every real 
number currently being tracked in the **half-open interval** 
`[left, right)`.


**Example 1:**

```
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)
```


**Constraints:**

- `1 <= left < right <= 109`
- At most `104` calls will be made to `addRange`, `queryRange`, and `removeRange`.
"""


class RangeModule:  # type: ignore

    def __init__(self):
        self.ranges = SortedList()

    def addRange(self, left: int, right: int) -> None:
        idx = self._findLastSmallerThanOrEqualTo(left)
        while idx < len(self.ranges) and self.ranges[idx][0] <= right:
            if self.ranges[idx][1] >= left:
                left = min(self.ranges[idx][0], left)
                right = max(self.ranges[idx][1], right)
                self.ranges.pop(idx)
            else:
                idx += 1
        self.ranges.add([left, right])        

    def queryRange(self, left: int, right: int) -> bool:
        idx = self._findLastSmallerThanOrEqualTo(left)
        if idx < len(self.ranges) and self.ranges[idx][0] <= left and self.ranges[idx][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        self.addRange(left, right)
        idx = self._findLastSmallerThanOrEqualTo(left)
        start, end = self.ranges[idx]
        self.ranges.pop(idx)
        if start < left:
            self.addRange(start, left)
        if end > right:
            self.addRange(right, end)
        
    def _findLastSmallerThanOrEqualTo(self, start):
        left, right = 1, len(self.ranges)
        while left < right:
            mid = (left + right) // 2
            if self.ranges[mid][0] <= start:
                left = mid + 1
            else:
                right = mid
        return left - 1

class RangeModule:

    def __init__(self):
        self.line = [0, 10**9+1]
        self.track = [False, False]

    def addRange(self, left: int, right: int, track=True) -> None:
        def index(val):
            # insert val to line if not exist
            # maintain the track info
            i = bisect.bisect_left(self.line, val)
            if self.line[i] != val:
                self.line.insert(i, val)
                self.track.insert(i, self.track[i-1])
            return i
            
        i = index(left)
        j = index(right)
        self.line[i:j] = [left]
        self.track[i:j] = [track]
                
    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.line, left) - 1
        j = bisect.bisect_left(self.line, right)
        return all(self.track[i:j])

    def removeRange(self, left: int, right: int) -> None:
        self.addRange(left, right, False)


"""759. Employee Free Time

We are given a list `schedule` of employees, which represents the 
working time for each employee.

Each employee has a list of non-overlapping `Intervals`, and these 
intervals are in sorted order.

Return the list of finite intervals representing **common, 
positive-length free time** for *all* employees, also in sorted order.

(Even though we are representing `Intervals` in the form `[x, y]`, 
the objects inside are `Intervals`, not lists or arrays. For example, 
`schedule[0][0].start = 1`, `schedule[0][0].end = 2`, and 
`schedule[0][0][0]` is not defined). Also, we wouldn't include intervals 
like [5, 5] in our answer, as they have zero length.


**Example 1:**

```
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
```

**Example 2:**

```
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
```
"""

class Interval:
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end


def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
    queue = []
    for j, s in enumerate(schedule):
        heapq.heappush(queue, [s[0].start, 0, j])
    
    free_time = []
    cur_end = -1
    while queue:
        _, i, j = heapq.heappop(queue)
        s = schedule[j]
        if cur_end >= 0 and s[i].start > cur_end:
            free_time.append(Interval(cur_end, s[i].start))
        cur_end = max(cur_end, s[i].end)
        i += 1
        if i < len(s):
            heapq.heappush(queue, [s[i].start, i, j])
    
    return free_time


"""778. Swim in Rising Water

You are given an `n x n` integer matrix `grid` where each value 
`grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere 
is `t`. You can swim from a square to another 4-directionally adjacent 
square if and only if the elevation of both squares individually are at 
most `t`. You can swim infinite distances in zero time. Of course, you 
must stay within the boundaries of the grid during your swim.

Return *the least time until you can reach the bottom right square* 
`(n - 1, n - 1)` *if you start at the top left square* `(0, 0)`.

 
**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg)

```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)

```
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```


**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n2`
- Each value `grid[i][j]` is **unique**.
"""

def swimInWater(grid: List[List[int]]) -> int:  # type: ignore
    '''
    Dijkstra node (i,j) -> min time to reach (i, j) from (0, 0)
    '''
    n = len(grid)
    dist = {(0, 0): grid[0][0]}
    for i in range(n):
        for j in range(n):
            if i != 0 or j != 0:
                dist[(i, j)] = float('inf')
    
    queue = [(grid[0][0], (0, 0))]
    S = set((0, 0))
    
    while queue:
        _, (i, j) = heapq.heappop(queue)
        if (i, j) in S:
            continue
        S.add((i, j))
        for ni, nj in zip((i-1, i+1, i, i), (j, j, j-1, j+1)):
            if 0 <= ni < n and 0 <= nj < n:
                alt = max(grid[ni][nj], dist[(i, j)])
                if dist[(ni, nj)] > alt:
                    dist[(ni, nj)] = alt
                    heapq.heappush(queue, (alt, (ni, nj)))
                    
    return dist[(n-1, n-1)]

def swimInWater(grid: List[List[int]]) -> int:  # type: ignore
    """
    binary search
    """
    n = len(grid)
    
    def canSwimUntilTime(t):
        visited = set()
        def dfs(i, j, t):
            if i == n-1 and j == n-1:
                return True
            visited.add((i, j))
            for ni, nj in zip((i-1, i+1, i, i), (j, j, j-1, j+1)):
                if (
                    0 <= ni < n # in grid
                    and 0 <= nj < n # in grid
                    and grid[ni][nj] <= t # can Swim
                    and (ni, nj) not in visited # prevent loop
                    and dfs(ni, nj, t)
                ):
                    return True
            return False
        # we can remove the below line as the left in binary search
        # below starts from grid[0][0]
        # if grid[0][0] > t: return False
        return dfs(0, 0, t)
        
    left, right = grid[0][0], n * n
    
    while left < right:
        mid = (left + right) // 2
        if canSwimUntilTime(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def swimInWater(grid: List[List[int]]) -> int:
    # (greedy) minimal spanning tree
    
    groups = {}
    rank = defaultdict(int)
    def parent(node):
        grp = groups.setdefault(node, node)
        if grp != node:
            groups[node] = parent(grp)
        return groups[node]
    
    def union(a, b):
        grp_a, grp_b = parent(a), parent(b)
        if grp_a == grp_b:
            return
        if rank[grp_a] < rank[grp_b]:
            grp_a, grp_b = grp_b, grp_a
        groups[grp_b] = grp_a
        if rank[grp_a] == rank[grp_b]:
            rank[grp_a] += 1
    
    n = len(grid)
    nodes = sorted(
        [(i, j) for i in range(n) for j in range(n)], 
        key=lambda x: grid[x[0]][x[1]]
    )
    visited = [[False] * n for _ in range(n)]
    for i, j in nodes:
        visited[i][j] = True
        for ni, nj in zip((i-1, i+1, i, i), (j, j, j-1, j+1)):
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj]:
                union((i, j), (ni, nj))
                
        if parent((0, 0)) == parent((n-1, n-1)):
            return grid[i][j]


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


"""939. Minimum Area Rectangle

You are given an array of points in the **X-Y** plane `points` where 
`points[i] = [xi, yi]`.

Return *the minimum area of a rectangle formed from these points, with 
sides parallel to the X and Y axes*. If there is not any such rectangle, 
return `0`.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

```
Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```


**Constraints:**

- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= xi, yi <= 4 * 104`
- All the given points are **unique**.
"""

def minAreaRect(points: List[List[int]]) -> int:
    points_by_x = defaultdict(set)
    for x, y in points:
        points_by_x[x].add(y)
    points_by_x = {k: v for k, v in points_by_x.items() if len(v) >= 2}
    
    xs = list(points_by_x.keys())
    #print('x', xs)
    n = len(xs)
    res = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            x1, x2 = xs[i], xs[j]
            ys = points_by_x[x1] & points_by_x[x2]
            if len(ys) >= 2:
                #print('y', ys)
                ys = sorted(ys)
                for y1, y2 in zip(ys, ys[1:]):
                    res = min(res, (y2 - y1) * abs(x1 - x2))
    
    return res if res < float('inf') else 0  # type: ignore

def minAreaRect(self, points: List[List[int]]) -> int:
    """A rectangle will be fixed by two points in diagonal
    
    check all pairs of points as diagonal of rectangle, cache
    points seen in a set (same technique as twosum)"""
    
    seen = set()
    rval = float('inf')
    for x1, y1 in points:
        for x2, y2 in seen:
            if (x1, y2) in seen and (x2, y1) in seen:
                rval = min(rval, abs((x1 - x2) * (y1 - y2)))
        seen.add((x1, y1))
    
    return rval if rval < float('inf') else 0  # type: ignore
    

"""1101. The Earliest Moment When Everyone Become Friends

There are n people in a social group labeled from `0` to `n - 1`. You 
are given an array `logs` where `logs[i] = [timestampi, xi, yi]` 
indicates that `xi` and `yi` will be friends at the time `timestampi`.

Friendship is **symmetric**. That means if `a` is friends with `b`, 
then `b` is friends with `a`. Also, person `a` is acquainted with a 
person `b` if `a` is friends with `b`, or `a` is a friend of someone 
acquainted with `b`.

Return *the earliest time for which every person became acquainted with 
every other person*. If there is no such earliest time, return `-1`.


**Example 1:**

```
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
```

**Example 2:**

```
Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
```


**Constraints:**

- `2 <= n <= 100`
- `1 <= logs.length <= 104`
- `logs[i].length == 3`
- `0 <= timestampi <= 109`
- `0 <= xi, yi <= n - 1`
- `xi != yi`
- All the values `timestampi` are **unique**.
- All the pairs `(xi, yi)` occur at most one time in the input.
"""

def earliestAcq(logs: List[List[int]], n: int) -> int:
    '''Minimum Spanning Tree with Union Find'''
    
    group = {}
    size = defaultdict(lambda: 1)
    
    def root(node):
        grp = group.setdefault(node, node)
        if grp != node:
            group[node] = root(grp)
        return group[node]
    
    def union(a, b):
        # Union a and b if not yet; return
        # if there is group with size n
        grp_a, grp_b = root(a), root(b)
        if grp_a == grp_b:
            # we can return False safely 
            # as if grp_a has size n, we
            # will stop the algo
            return False
        if size[grp_a] < size[grp_b]:
            grp_a, grp_b = grp_b, grp_a
        group[grp_b] = grp_a
        size[grp_a] += size[grp_b]
        if size[grp_a] == n:
            return True
        return False
    
    logs.sort()
    
    for time, a, b in logs:
        if union(a, b):
            return time
    return -1
    

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


"""1423. Maximum Points You Can Obtain from Cards

There are several cards **arranged in a row**, and each card has an 
associated number of points. The points are given in the integer array 
`cardPoints`.

In one step, you can take one card from the beginning or from the end 
of the row. You have to take exactly `k` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `cardPoints` and the integer `k`, return the 
*maximum score* you can obtain.


**Example 1:**

```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, 
choosing the rightmost card first will maximize your total score. 
The optimal strategy is to take the three cards on the right, giving 
a final score of 1 + 6 + 5 = 12.
```

**Example 2:**

```
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

**Example 3:**

```
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```


**Constraints:**

- `1 <= cardPoints.length <= 105`
- `1 <= cardPoints[i] <= 104`
- `1 <= k <= cardPoints.length`
"""

def maxScore(self, cardPoints: List[int], k: int) -> int:
    cur_sum = global_max = sum(cardPoints[:k])
    for i in range(k):
        cur_sum = cur_sum - cardPoints[k-i-1] + cardPoints[-i-1]
        global_max = max(global_max, cur_sum)
    
    return global_max


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


"""2115. Find All Possible Recipes from Given Supplies

You have information about `n` different recipes. You are given a string 
array `recipes` and a 2D string array `ingredients`. The `ith` recipe 
has the name `recipes[i]`, and you can **create** it if you have **all** 
the needed ingredients from `ingredients[i]`. Ingredients to a recipe 
may need to be created from **other** recipes, i.e., `ingredients[i]` 
may contain a string that is in `recipes`.

You are also given a string array `supplies` containing all the 
ingredients that you initially have, and you have an infinite supply of 
all of them.

Return *a list of all the recipes that you can create.* You may return 
the answer in **any order**.

Note that two recipes may contain each other in their ingredients.


**Example 1:**

```
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
```

**Example 2:**

```
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
```

**Example 3:**

```
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
```

 
**Constraints:**

- `n == recipes.length == ingredients.length`
- `1 <= n <= 100`
- `1 <= ingredients[i].length, supplies.length <= 100`
- `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
- `recipes[i], ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
- All the values of `recipes` and `supplies` combined are unique.
- Each `ingredients[i]` does not contain any duplicate values.
"""

def findAllRecipes(  # type: ignore
    recipes: List[str], 
    ingredients: List[List[str]], 
    supplies: List[str]
) -> List[str]:
    
    recipe2idx = {recipe: i for i, recipe in enumerate(recipes)}
    memo = {}
    supplies = set(supplies)  # type: ignore
    
    def canMake(recipe):
        if recipe not in memo:
            memo[recipe] = False
            if recipe in recipe2idx:
                ingre = ingredients[recipe2idx[recipe]]
                memo[recipe] = all(item in supplies or canMake(item) for item in ingre)
        return memo[recipe]
    
    return [recipe for recipe in recipes if canMake(recipe)]

def findAllRecipes(
    recipes: List[str], 
    ingredients: List[List[str]], 
    supplies: List[str]
) -> List[str]:
    
    supplies = set(supplies)  # type: ignore
    adj, indegree = defaultdict(list), defaultdict(int)
    for recipe, ingredient in zip(recipes, ingredients):
        for item in ingredient:
            if item not in supplies:
                adj[item].append(recipe)
                indegree[recipe] += 1
                
    available = [recipe for recipe in recipes if indegree[recipe] == 0]
    ans = list(available)
    
    while available:
        for neigh in adj[available.pop()]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                ans.append(neigh)
                available.append(neigh)
    
    return ans


"""2128. Remove All Ones With Row and Column Flips

You are given an `m x n` binary matrix `grid`.

In one operation, you can choose **any** row or column and flip each
value in that row or column (i.e., changing all `0`'s to `1`'s, and 
all `1`'s to `0`'s).

Return `true` *if it is possible to remove all* `1`*'s from* `grid` 
using **any** number of operations or `false` otherwise.


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/01/03/image-20220103191300-1.png)

```
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181204-7.png)

```
Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1's from grid.
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2022/01/03/image-20220103181224-8.png)

```
Input: grid = [[0]]
Output: true
Explanation: There are no 1's in grid.
```


**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is either `0` or `1`.
"""


def removeOnes(grid: List[List[int]]) -> bool:
    """no matter how we flip, since we can only flip an *entire*
    row or column, for any two of rows, all corresponding 
    digits in two rows must be either all same or all opposite"""
    
    m, n = len(grid), len(grid[0])
    for i in range(1, m):
        xor_count = 0
        for j in range(n):
            xor_count += grid[0][j] ^ grid[i][j]
        if xor_count not in (0, n):
            return False
    
    return True


"""2135. Count Words Obtained After Adding a Letter

You are given two **0-indexed** arrays of strings `startWords` and 
`targetWords`. Each string consists of **lowercase English letters** only.

For each string in `targetWords`, check if it is possible to choose a 
string from `startWords` and perform a **conversion operation** on it 
to be equal to that from `targetWords`.

The **conversion operation** is described in the following two steps:

1. Append any lowercase letter that is not present in the string to its end.
   - For example, if the string is `"abc"`, the letters `'d'`, `'e'`, 
   or `'y'` can be added to it, but not `'a'`. If `'d'` is added, the 
   resulting string will be `"abcd"`.
2. Rearrange the letters of the new string in any arbitrary order.
   - For example, `"abcd"` can be rearranged to `"acbd"`, `"bacd"`, 
   `"cbda"`, and so on. Note that it can also be rearranged to `"abcd"` itself.

Return *the **number of strings** in* `targetWords` *that can be obtained 
by performing the operations on **any** string of* `startWords`.

**Note** that you will only be verifying if the string in `targetWords` 
can be obtained from a string in `startWords` by performing the operations. 
The strings in `startWords` **do not** actually change during this process.


**Example 1:**

```
Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
Explanation:
- In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
  Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
- In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
```

**Example 2:**

```
Input: startWords = ["ab","a"], targetWords = ["abc","abcd"]
Output: 1
Explanation:
- In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
- There is no string in startWords that can be used to obtain targetWords[1] = "abcd".
```


**Constraints:**

- `1 <= startWords.length, targetWords.length <= 5 * 104`
- `1 <= startWords[i].length, targetWords[j].length <= 26`
- Each string of `startWords` and `targetWords` consists of lowercase English letters only.
- No letter occurs more than once in any string of `startWords` or `targetWords`.
"""

def wordCount(startWords: List[str], targetWords: List[str]) -> int:
    def char2int(char):
        return ord(char) - ord('a')
    def word_hash(word):
        hash_value = 0
        for char in word:
            hash_value |= 1 << char2int(char)
        return hash_value
    
    hashes = {word_hash(word) for word in startWords}
    
    rval = 0    
    for word in targetWords:
        hash_value = word_hash(word)
        for char in word:
            i = char2int(char)
            if hash_value & 1 << i and hash_value & (~ (1 << i)) in hashes:
                rval += 1
                break
                
    return rval
    
    
"""2158. Amount of New Area Painted Each Day

There is a long and thin painting that can be represented by a number 
line. You are given a **0-indexed** 2D integer array `paint` of length 
`n`, where `paint[i] = [starti, endi]`. This means that on the `ith` day 
you need to paint the area **between** `starti` and `endi`.

Painting the same area multiple times will create an uneven painting so 
you only want to paint each area of the painting at most **once**.

Return *an integer array* `worklog` *of length* `n`*, where* `worklog[i]` 
*is the amount of **new** area that you painted on the* `ith` *day.*


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-16-16-diagram-drawio-diagrams-net.png)

```
Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1. 
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-17-45-diagram-drawio-diagrams-net.png)

```
Input: paint = [[1,4],[5,8],[4,7]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 5 and 8.
The amount of new area painted on day 1 is 8 - 5 = 3.
On day 2, paint everything between 4 and 5.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 5 - 4 = 1. 
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2022/02/01/screenshot-2022-02-01-at-17-19-49-diagram-drawio-diagrams-net.png)

```
Input: paint = [[1,5],[2,4]]
Output: [4,0]
Explanation:
On day 0, paint everything between 1 and 5.
The amount of new area painted on day 0 is 5 - 1 = 4.
On day 1, paint nothing because everything between 2 and 4 was already painted on day 0.
The amount of new area painted on day 1 is 0.
```


**Constraints:**

- `1 <= paint.length <= 105`
- `paint[i].length == 2`
- `0 <= starti < endi <= 5 * 104`
"""

class SegmentTree:  # type: ignore
    
    def __init__(self, n):
        self.n = n
        self.tree = {}
        self._build(0, 0, self.n-1)
        
    def _build(self, treeIdx, left, right):
        if left == right:
            self.tree[treeIdx] = 1
        else:
            mid = (left + right) // 2
            self._build(treeIdx * 2 + 1, left, mid)
            self._build(treeIdx * 2 + 2, mid + 1, right)
            self.tree[treeIdx] = self.tree[treeIdx * 2 + 1] + self.tree[treeIdx * 2 + 2]
    
    def range_sum(self, treeIdx, treeLeft, treeRight, left, right):
        if left <= treeLeft and right >= treeRight:
            return self.tree[treeIdx]
        if left > treeRight or right < treeLeft:
            return 0
        treeMid = (treeLeft + treeRight) // 2
        leftSum = self.range_sum(treeIdx * 2 + 1, treeLeft, treeMid, left, right)
        rightSum = self.range_sum(treeIdx * 2 + 2, treeMid + 1, treeRight, left, right)
        return leftSum + rightSum
    
    def range_update(self, treeIdx, treeLeft, treeRight, left, right):
        if treeRight < left or treeLeft > right:
            return
        if treeLeft == treeRight:
            self.tree[treeIdx] = 0
        else:
            treeMid = (treeLeft + treeRight) // 2
            self.range_update(treeIdx * 2 + 1, treeLeft, treeMid, left, right)
            self.range_update(treeIdx * 2 + 2, treeMid + 1, treeRight, left, right)
            self.tree[treeIdx] = self.tree[treeIdx * 2 + 1] + self.tree[treeIdx * 2 + 2]


def amountPainted(paint: List[List[int]]) -> List[int]:  # type: ignore
    """Segment Tree - TLE in Python"""
    min_val, max_val = min([x[0] for x in paint]), max([x[1] for x in paint])
    n = max_val - min_val
    seg_tree = SegmentTree(n)  # type: ignore
    
    rval = []
    for start, end in paint:
        rval.append(seg_tree.range_sum(0, 0, n-1, start-min_val, end-min_val-1))  # type: ignore
        seg_tree.range_update(0, 0, n-1, start-min_val, end-min_val-1)  # type: ignore
    
    return rval

def amountPainted(paint: List[List[int]]) -> List[int]:  # type: ignore
    # jump line
    line, rval = [0] * 500001, [0] * len(paint)
    
    for i, (start, end) in enumerate(paint):
        while start < end:
            jump = max(start + 1, line[start])
            rval[i] += 1 if line[start] == 0 else 0
            line[start] = max(line[start], end)
            start = jump
    
    return rval

def amountPainted(paint: List[List[int]]) -> List[int]:
    # sorted list
    records = []
    for i, (start, end) in enumerate(paint):
        records.append((start, i, 0))
        records.append((end, i, 1))
    records.sort()
    
    rval = [0] * len(paint)
    indexes = SortedList()
    last_idx = 0
    for idx, i, status in records:
        if indexes:
            rval[indexes[0]] += idx - last_idx
        if status == 0:
            indexes.add(i)
        else:
            # since end < start, i must have been
            # added to indexes before remove
            indexes.remove(i)
        last_idx = idx
            
    return rval


"""2178. Maximum Split of Positive Even Integers

You are given an integer `finalSum`. Split it into a sum of a **maximum** 
number of **unique** positive even integers.

- For example, given `finalSum = 12`, the following splits are **valid** 
(unique positive even integers summing up to `finalSum`): `(12)`, `(2 + 10)`, 
`(2 + 4 + 6)`, and `(4 + 8)`. Among them, `(2 + 4 + 6)` contains the
maximum number of integers. Note that `finalSum` cannot be split into 
`(2 + 2 + 4 + 4)` as all the numbers should be unique.

Return *a list of integers that represent a valid split containing a 
**maximum** number of integers*. If no valid split exists for `finalSum`, 
return *an **empty** list*. You may return the integers in **any** order.


**Example 1:**

```
Input: finalSum = 12
Output: [2,4,6]
Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.
```

**Example 2:**

```
Input: finalSum = 7
Output: []
Explanation: There are no valid splits for the given finalSum.
Thus, we return an empty array.
```

**Example 3:**

```
Input: finalSum = 28
Output: [6,8,2,12]
Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). 
(6 + 8 + 2 + 12) has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.
```


**Constraints:**

- `1 <= finalSum <= 1010`
"""


def maximumEvenSplit(finalSum: int) -> List[int]:
    ''' Greedy: start from min even number
    
    finalSum = 2 + 4 + ... + 2n + m where m > 2n
    => n * (n + 3) < finalSum
    
    binary search if just need to return length
    '''
    if finalSum % 2: return []
    
    rval = [] 
    val = 2
    
    while val * 2 < finalSum:
        rval.append(val)
        finalSum -= val
        val += 2
    rval.append(finalSum)
    
    return rval


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


"""2351. First Letter to Appear Twice

Given a string `s` consisting of lowercase English letters, return *the 
first letter to appear **twice***.

**Note**:

- A letter `a` appears twice before another letter `b` if the **second** 
occurrence of `a` is before the **second** occurrence of `b`.
- `s` will contain at least one letter that appears twice.


**Example 1:**

```
Input: s = "abccbaacz"
Output: "c"
Explanation:
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.
```

**Example 2:**

```
Input: s = "abcdd"
Output: "d"
Explanation:
The only letter that appears twice is 'd' so we return 'd'.
```


**Constraints:**

- `2 <= s.length <= 100`
- `s` consists of lowercase English letters.
- `s` has at least one repeated letter.
"""

def repeatedCharacter(s: str) -> str:
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return ''
        
        
"""2352. Equal Row and Column Pairs

Given a **0-indexed** `n x n` integer matrix `grid`, *return the number 
of pairs* `(Ri, Cj)` *such that row* `Ri` *and column* `Cj` *are equal*.

A row and column pair is considered equal if they contain the same 
elements in the same order (i.e. an equal array).


**Example 1:**

![img](https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg)

```
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg)

```
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
```


**Constraints:**

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 105`
"""

def equalPairs(self, grid: List[List[int]]) -> int:  # type: ignore
    hashes = defaultdict(int)
    for row in grid:
        hash_ = ','.join([str(ele) for ele in row])
        hashes[hash_] += 1
    
    rval = 0
    m, n = len(grid), len(grid[0])
    for j in range(n):
        hash_ = []
        for i in range(m):
            hash_.append(str(grid[i][j]))
        hash_ = ','.join(hash_)
        rval += hashes[hash_]
    
    return rval

def equalPairs(self, grid: List[List[int]]) -> int:
    "Same idea with simplified codes"
    pairs = 0
    cnt = Counter(tuple(row) for row in grid)
    for tpl in zip(*grid): # generate columns
        pairs += cnt[tpl]
    return pairs


"""2353. Design a Food Rating System

Design a food rating system that can do the following:

- **Modify** the rating of a food item listed in the system.
- Return the highest-rated food item for a type of cuisine in the system.

Implement the `FoodRatings` class:

- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.
  - `foods[i]` is the name of the `ith` food,
  - `cuisines[i]` is the type of cuisine of the `ith` food, and
  - `ratings[i]` is the initial rating of the `ith` food.
- `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.
- `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.


**Example 1:**

```
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".
```


**Constraints:**

- `1 <= n <= 2 * 104`
- `n == foods.length == cuisines.length == ratings.length`
- `1 <= foods[i].length, cuisines[i].length <= 10`
- `foods[i]`, `cuisines[i]` consist of lowercase English letters.
- `1 <= ratings[i] <= 108`
- All the strings in `foods` are **distinct**.
- `food` will be the name of a food item in the system across all calls to `changeRating`.
- `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.
- At most `2 * 104` calls **in total** will be made to `changeRating` and `highestRated`.
"""

class FoodRatings:  # type: ignore

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = defaultdict(dict)
        self.queue = defaultdict(list)
        self.f2c = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[cuisine][food] = -rating
            heapq.heappush(self.queue[cuisine], (-rating, food))
            self.f2c[food] = cuisine
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.f2c[food]
        self.foods[cuisine][food] = -newRating
        heapq.heappush(self.queue[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        foods = self.foods[cuisine]
        queue = self.queue[cuisine]
        while queue:
            rating, food = queue[0]
            if rating == foods[food]:
                return food
            else:
                heapq.heappop(queue)
                continue
        return ''       
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2cr = {}
        self.lists = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings):
            # use negative rating as we want the max
            self.f2cr[f] = (c, -r)
            self.lists[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.f2cr[food]
        self.f2cr[food] = (cuisine, -newRating)
        self.lists[cuisine].remove((rating, food))  # type: ignore
        self.lists[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.lists[cuisine][0][1]
    

"""2354. Number of Excellent Pairs

You are given a **0-indexed** positive integer array `nums` and a positive integer `k`.

A pair of numbers `(num1, num2)` is called **excellent** if the following conditions are satisfied:

- **Both** the numbers `num1` and `num2` exist in the array `nums`.
- The sum of the number of set bits in `num1 OR num2` and `num1 AND num2` is greater than or equal to `k`, where `OR` is the bitwise **OR** operation and `AND` is the bitwise **AND** operation.

Return *the number of **distinct** excellent pairs*.

Two pairs `(a, b)` and `(c, d)` are considered distinct if either `a != c` or `b != d`. For example, `(1, 2)` and `(2, 1)` are distinct.

**Note** that a pair `(num1, num2)` such that `num1 == num2` can also be excellent if you have at least **one** occurrence of `num1` in the array.


**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: 5
Explanation: The excellent pairs are the following:
- (3, 3). (3 AND 3) and (3 OR 3) are both equal to (11) in binary. The total number of set bits is 2 + 2 = 4, which is greater than or equal to k = 3.
- (2, 3) and (3, 2). (2 AND 3) is equal to (10) in binary, and (2 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
- (1, 3) and (3, 1). (1 AND 3) is equal to (01) in binary, and (1 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
So the number of excellent pairs is 5.
```

**Example 2:**

```
Input: nums = [5,1,1], k = 10
Output: 0
Explanation: There are no excellent pairs for this array.
```


**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 109`
- `1 <= k <= 60`
"""

def countExcellentPairs(nums: List[int], k: int) -> int:  # type: ignore
    '''
    setbit(num1 & num2) + setbit(num1 | num2) = setbit(num1) + setbit(num2)
    '''
    
    setbits = []
    for num in set(nums):
        setbit = 0
        while num > 0:
            num, setbit = num // 2, setbit + num % 2
        setbits.append(setbit)
    setbits.sort()
    
    rval = 0
    n = j = len(setbits)
    for i in range(n):
        while j > 0 and setbits[j-1] + setbits[i] >= k:
            j -= 1
        rval += n - j
    
    return rval

def countExcellentPairs(self, nums: List[int], k: int) -> int:
    '''
    setbit(num1 & num2) + setbit(num1 | num2) = setbit(num1) + setbit(num2)
    '''
    
    # require python 3.10
    setbits = sorted(map(int.bit_count, set(nums)))  # type: ignore
    
    rval = 0
    n = j = len(setbits)
    for i in range(n):
        while j > 0 and setbits[j-1] + setbits[i] >= k:
            j -= 1
        rval += n - j
    
    return rval