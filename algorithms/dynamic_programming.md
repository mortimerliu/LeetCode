
- [1. Dynamic Programming](#1-dynamic-programming)
  - [1.1. Knapsack Problems](#11-knapsack-problems)
    - [1.1.1. 0/1 Knapsack](#111-01-knapsack)
    - [1.1.2. Number Partitioning](#112-number-partitioning)
    - [1.1.3. The Bounded Knapsack Problem](#113-the-bounded-knapsack-problem)
    - [1.1.4. The Unbounded Knapsack Problem](#114-the-unbounded-knapsack-problem)
    - [1.1.5. The Subset-Sum Problem](#115-the-subset-sum-problem)
    - [1.1.6. The Change-Making Problem](#116-the-change-making-problem)
    - [1.1.7. 0/1 Multiple Knapsack Problem](#117-01-multiple-knapsack-problem)
    - [1.1.8. Bin-Packing Problem](#118-bin-packing-problem)
    - [1.1.9. LC Problems](#119-lc-problems)

# 1. Dynamic Programming

## 1.1. Knapsack Problems

- [Wiki](https://en.wikipedia.org/wiki/Knapsack_problem)
- [GMU](http://masc.cs.gmu.edu/wiki/KnapsackProblems)
- [UNIBO](http://www.or.deis.unibo.it/knapsack.html)

### 1.1.1. 0/1 Knapsack

- **Input**
  - `N` items, Each item `i` associated with weight `w[i]` and profit `p[i]`.
  - A maximum weight `W`.
- **Output**
  - The maximum profit sum `P` possible without exceeding the weight capacity `W`.
  - A subset of the items which maximizes the profit sum without exceeding the weight capacity `W`.
    - The subset is usually given by a bit vector `s` of size `N` where `s[i]=1` represents that item `i` is included in the knapsack. (Hence the name 0/1 Knapsack)

#### Solution 1<!-- omit from toc -->

```python
def knapsack(weights, profits, W):
    '''
    Classical 0/1 Knapsack Problem
    '''

    n = len(weights)
    # P[i][j]: max profit we can get with items 0 to i-1
    # and knapsack size j (item is 0-indexed, thus i-1)
    # P can be reduced to a 1-D array
    P = [[0] * (W+1) for _ in range(n+1)]
    # S[i][j]: whether select item i-1 or not when knapsack
    # size is j to achieve the max profit
    S = [[0] * (W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            # not select item i-1
            P[i][j] = P[i-1][j]
            # only select item i-1 if it fits in knapsack
            if weights[i-1] <= j:
                # max profits if we select item i-1
                candi = P[i-1][j-weights[i-1]] + profits[i-1]
                if candi > P[i][j]:
                    P[i][j] = candi
                    S[i][j] = 1 # mark item i-1 as selected

    # now P[n][W] is the max profit
    # we need also generate the set of items we select
    i, j = n, W
    selected = [0] * n
    while i > 0 and j > 0:
        if S[i][j] == 1:
            selected[i-1] = 1
            j -= weights[i-1]
        i -= 1

    return P[n][W], selected

assert knapsack([2,3,4],[2,3,4], 5) == (5, [1, 1, 0])
```

#### Solution 2<!-- omit from toc -->

```python
def knapsackV2(weights, profits, W):
    '''
    Classical 0/1 Knapsack Problem
    if only max profits required
    '''

    n = len(weights)
    # P[[j]: max profit we can get with items 0 to i-1
    # and knapsack size j (item is 0-indexed, thus i-1)
    P = [0] * (W+1)
    max_profit = 0
    for i in range(1, n+1):
        for j in range(W, weights[i-1]-1, -1):
            P[j] = max(P[j], P[j-weights[i-1]] + profits[i-1])
            max_profit = max(max_profit, P[j])
    return max_profit

assert knapsackV2([2,3,4],[2,3,4], 5) == 5
```

### 1.1.2. Number Partitioning

Partition a set S containing N integers, into two sets S1 and S2, so that |sum(L1) - sum(L2)| is minimized.

- **Input**
  - A set of integers, S.
- **Output**
  - minimum of |sum(L1) - sum(L2)|
  - For each integer i in S, a 0 or 1 indicating which side of the partition it is on.

This problem is perhaps even more general than the 0/1 knapsack problem and is considered by Garey and Johnson as one of the six basic NP-hard problems that lie at the heart of NP-completeness theory. It has applications in multiprocessor scheduling, VLSI layout, and perhaps most famously, public key cryptography. In programming contests, the problem sometimes shows up in the form of children picking sides in a ball game so that the game is fair.

#### Solution 1<!-- omit from toc -->

```python
def partitionNumber(S):
    '''
    Number Partitioning

    Translate to 0/1 Knapsack:
    weights[i] = profits[i] = S[i]
    W = sum(S) // 2
    '''
    t = sum(S)
    p, selected = knapsack(S, S, t // 2)
    return t - 2 * p, selected

assert partitionNumber([1,10, 5, 8, 9]) == (1, [1, 1, 1, 0, 0])
```

### 1.1.3. The Bounded Knapsack Problem

Instead of N items, you are given M types of items, each type having a bounded quantity.

- **Input**
  - `M` types of items, each item type `m` having bounded quantity `q[m]` and associated with weight `w[m]` and profit `p[m]`
  - A maximum weight `W`.
- **Output**
  - The amount of each type of item should be included in the knapsack to maximize profit sum without exceeding weight capacity `W` and subject to the bounded quantity for each item type.

Note that, 0/1 Knapsack is a special case of bounded knapsack
where all `q[m] = 1`

#### Related articles<!-- omit from toc -->

+ [Stack Overflow](https://stackoverflow.com/questions/9559674/dp-algorithm-for-bounded-knapsack)
+ [sqrt decomposition](https://codeforces.com/blog/entry/59606)
+ [Binary representation](https://codeforces.com/blog/entry/65202?#comment-492168)
+ [The Integer (0/1) Bounded Knapsack Problem](http://dhruvbird.blogspot.com/2011/09/integer-01-bounded-knapsack-problem.html)

#### Solution 1<!-- omit from toc -->

```python
def boundedKnapsack(q, w, p, W):
    '''
    Bounded Knapsack Problem

    given M types of items 0 to M-1, each with bounded quantity q[m]
    and associated with weight w[m] and profit p[m] and a knapsack
    with size W, calculate the maximum of profit sum and the amount
    of each type of item

    Adapt the solution for 0/1 Knapsack:
    Time O(M * W * sum(q) / M) = Time O(W * sum(q))
    '''

    M = len(q)
    P = [0] * (W+1)
    S = [[0] * (W+1) for _ in range(M+1)]

    for i in range(1, M+1):
        for j in range(W, w[i-1]-1, -1):
            # no selected -> selected all q[i-1]
            for k in range(q[i-1]+1):
                if w[i-1] * k <= j and P[j - w[i-1] * k] + p[i-1] * k > P[j]:
                    P[j] = P[j - w[i-1] * k] + p[i-1] * k
                    S[i][j] = k

    # now P[W] contains the maximum profit
    i, j = M, W
    selected = [0] * M
    while i > 0 and j > 0:
        if S[i][j]:
            selected[i-1] = S[i][j]
            j -= w[i-1] * S[i][j]
        i -= 1
    return P[W], selected

boundedKnapsack([1,1,1], [2,3,4],[2,3,4], 5)
# (5, [1, 1, 0])

# [1, 2, 3], [2, 3, 4], [3, 4, 5], 20
# (26, [1, 2, 3])
```

#### Solution 2<!-- omit from toc -->

```python
def boundedKnapsackV2(q, w, p, W):
    '''
    Bounded Knapsack Problem - Solution 2

    given M types of items 0 to M-1, each with bounded quantity q[m]
    and associated with weight w[m] and profit p[m] and a knapsack
    with size W, calculate the maximum of profit sum and the amount
    of each type of item

    convert to a pure 0/1 Knapsack by treating duplicated items as
    distinct items
    Time O(W * sum(q[m]))

    However, we can do better by splitting each type into only
    log(q[m]) items using binary representation. For exmaple,
    if q[m] = 13, we know 13 = 1 + 4 + 8, we first split 13 to
    3 items: 1, 4, 8. Note that this doesn't represent buying
    2 items. In order to fix this, for each item, if item // 2 is
    not in the split, split it into two. In our example, it means,
    for the set bit 4, since the lower bit 2 is a clear bit, split
    4 into 2 of 2. After that, we represent 13 with 4 items:
    1, 2, 2, and 8. the total number of items for each type is
    O(log(q[m])).
    Time O(W * sum(log(q[m])))
    '''

    def decompose(i, q, items):
        n = 0
        while 1 << (n+1) <= q:
            n += 1
        while n >= 0:
            if q >= 1 << n:
                q -= 1 << n
            else:
                items.pop()
                items.append((i, 1 << n))
            items.append((i, 1 << n))
            n -= 1

    M = len(q)
    items = []
    for i in range(M):
        decompose(i, q[i], items)

    N = len(items)
    P = [0] * (W+1)
    S = [[0] * (W+1) for _ in range(N)]

    for k, (i, cnt) in enumerate(items):
        for j in range(W, w[i]*cnt-1, -1):
            if P[j-w[i]*cnt] + p[i]*cnt > P[j]:
                P[j] = P[j-w[i]*cnt] + p[i]*cnt
                S[k][j] = 1

    # now P[W] contains the maximum profit
    i, j = N-1, W
    selected = [0] * M
    while i >= 0 and j > 0:
        if S[i][j]:
            selected[items[i][0]] += items[i][1]
            j -= w[items[i][0]] * items[i][1]
        i -= 1
    return P[W], selected

boundedKnapsackV2([1,1,1], [2,3,4],[2,3,4], 5)
# (5, [1, 1, 0])
```

#### Solution 3<!-- omit from toc -->

```python
import collections

def boundedKnapsackV3(q, w, p, W):
    '''
    Bounded Knapsack Problem - Solution 3

    Problem:

    given M types of items 0 to M-1, each with bounded quantity q[m]
    and associated with weight w[m] and profit p[m] and a knapsack
    with size W, calculate the maximum of profit sum and the amount
    of each type of item

    same DP definition as 0/1 Knapsack

    Time O(M * W)
    '''

    M = len(q)
    P = [0] * (W+1)
    S = [[0] * (W+1) for _ in range(M+1)]

    for i in range(1, M+1):
        # break the dp row into w[i-1] groups by remainder
        # and update each group in O(M / w[i-1])
        # and then overall time will be O(M) (a rolling
        # maximum question)
        # and make the overall time for the algorithm O(MW)
        for r in range(w[i-1]):
            j, n = r, W // w[i-1]
            queue = collections.deque([])
            while j <= W:
                cur = P[j] + n * p[i-1]
                # remove the out of window items
                # window is q[i-1] * w[i-1]
                while queue and j - queue[0][0] > q[i-1] * w[i-1]:
                    queue.popleft()
                # remove the items smaller than the current
                while queue and queue[-1][1] <= cur:
                    queue.pop()
                queue.append((j, cur))
                P[j] = queue[0][1] - n * p[i-1]
                S[i][j] = (j - queue[0][0]) // w[i-1]
                j += w[i-1]
                n -= 1

    # now P[W] contains the maximum profit
    i, j = M, W
    selected = [0] * M
    while i > 0 and j > 0:
        if S[i][j]:
            selected[i-1] = S[i][j]
            j -= w[i-1] * S[i][j]
        i -= 1
    return P[W], selected

boundedKnapsackV3([1,1,1], [2,3,4],[2,3,4], 5)
# (5, [1, 1, 0])
```

### 1.1.4. The Unbounded Knapsack Problem

You have an unbounded quantity of each item type, instead of a bounded quantity.

- **Input**
  - `M` types of items, each item type `m` having unbounded quantity and associated with weight `w[m]` and profit `p[m]`
  - A maximum weight W.
- **Output**
  - Maximum profit
  - The amount of each type of item should be included in the knapsack to maximize profit sum without exceeding weight capacity `W`.

#### Solution 1<!-- omit from toc -->

```python
def unboundedKnapsack(w, p, W):
    '''
    Unbounded Knapsack Problem

    Time O(MW)
    '''

    M = len(p)
    P = [0] * (W+1)
    S = [[0] * (W+1) for _ in range(M+1)]

    for i in range(1, M+1):
        # break the dp row into w[i-1] groups by remainder
        # and update each group in O(M / w[i-1])
        # and then overall time will be O(M)
        # and make the overall time for the algorithm O(MW)
        for r in range(w[i-1]):
            j, n = r, W // w[i-1]
            max_j, max_p = j, P[j]
            while j <= W:
                cur_p = P[j] + n * p[i-1]
                if cur_p >= max_p:
                    max_j, max_p = j, cur_p
                P[j] = max_p - n * p[i-1]
                S[i][j] = (j - max_j) // w[i-1]
                j += w[i-1]
                n -= 1

    # now P[W] contains the maximum profit
    i, j = M, W
    selected = [0] * M
    while i > 0 and j > 0:
        if S[i][j]:
            selected[i-1] = S[i][j]
            j -= w[i-1] * S[i][j]
        i -= 1
    return P[W], selected

unboundedKnapsack([2,3,4],[2,3,5],10)
# (12, [1, 0, 2])
```

#### Solution 2<!-- omit from toc -->

```python
def unboundedKnapsackV2(w, p, W):
    '''
    Unbounded Knapsack Problem
    only maximum profit is required

    Time O(MW)
    '''

    M = len(p)
    P = [0] * (W+1)

    for i in range(M):
        for j in range(w[i], W+1):
            P[j] = max(P[j], P[j-w[i]]+p[i])

    return P[W]

unboundedKnapsackV2([2,3,4],[2,3,5],10)
# 12
```

### 1.1.5. The Subset-Sum Problem

The same as 0/1 knapsack if profit p[i] equals the weight w[i].

- **Input**
  - Some set of N numbers.
  - A target value W
- **Output**
  - A subset of the N numbers so that the sum is as large as possible without exceeding W.

#### Solution 1<!-- omit from toc -->

```python
def subsetSum(S, W):
    return knapsack(S, S, W)

subsetSum([2,3,4], 5)
# (5, [1, 1, 0])
```

### 1.1.6. The Change-Making Problem

You are given a target value V and you need to make change for it using the smallest amount coins. The coins have some bounded number of denominations but an unbounded number of available coins in each denomination. This is the same as the unbounded knapsack problem except all the profits are 1 (however, notice that we want to reduce the number of coins, so we want to minimize this profit. some textbooks use a negative value, instead, in order to fit it under the exact same formulation as the knapsack problem.).

- **Input**
  - Some set of M denominations.
  - A target value V
- **Output**
  - The amount of each denomination that should be included in the knapsack to maximize profit sum without exceeding weight capacity W.

You can formulate this recursively this way:

- Let c[j] be the optimal number of coins to make value j.
- Let m[i] be the list of denominations
- Then you can write the following recursive relation:

![The Change-Making Problem](https://s2.loli.net/2022/01/28/CeNGH4ySXLFtgcm.png)

#### Solution 1<!-- omit from toc -->

```python
def CoinChange(w, V):
    '''
    Unbounded Knapsack with weight w[i]=S[i] and profit p[i]=1
    and minimize the profit instead of maximize
    but we need to make sure there is no unused space in Knapsack
    '''

    M = len(w)
    P = [float('inf')] * (V+1)
    P[0] = 0
    S = [[0] * (V+1) for _ in range(M)]

    for i in range(M):
        for r in range(w[i]):
            j, n = r, V // w[i]
            min_j, min_p = j, float('inf')
            while j <= V:
                cur_p = P[j] + n
                if cur_p <= min_p:
                    min_j, min_p = j, cur_p
                P[j] = min_p - n
                S[i][j] = (j - min_j) // w[i]
                j += w[i]
                n -= 1
    # now P[V] contains the maximum profit
    i, j = M-1, V
    selected = [0] * M
    while i >= 0 and j > 0:
        if S[i][j]:
            selected[i] = S[i][j]
            j -= w[i] * S[i][j]
        i -= 1
    return P[V], selected

CoinChange([2,3,4], 5)
# (inf, [0, 0])
```

### 1.1.7. 0/1 Multiple Knapsack Problem

The 0/1 knapsack problem but you are given multiple knapsacks of different sizes. The capacity constraint must be met for all of the knapsacks.

- **Input**
  - Some set of N items. Each item i is associated with weight w[i] and profit p[i].
  - Some set of knapsacks W with max size of knapsack k given by W[k]
- **Output**
  - A subset S of the items and which knapsack they are in.
    - For item i, S[i] will indicate the knapsack the item is in so that the profit is maximized without exceeding the capacity of any knapsack.

### 1.1.8. Bin-Packing Problem

You have some number of equally sized bins. You need to pack the items into bins so that the number of bins used is as small as possible.

- **Input**
  - The number of bins N.
  - The size of the bins K.
- **Output**
  - For each item i, S[i] represents the bin that the item is in so that the number of bins used is minimized.

### 1.1.9. LC Problems

- [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)
- [494. Target Sum](https://leetcode.com/problems/target-sum/)
- [1402. Reducing Dishes](https://leetcode.com/problems/reducing-dishes/) - bounded knapsack variation
- [2218. Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/)
