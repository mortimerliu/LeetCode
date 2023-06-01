# String<!-- omit from toc -->

- [1. String Matching](#1-string-matching)
  - [1.1. Sliding Window](#11-sliding-window)
  - [1.2. Rabin-Karp Algorithm (Single Hash)](#12-rabin-karp-algorithm-single-hash)
    - [1.2.1. Complexity](#121-complexity)
    - [1.2.2. Implementation](#122-implementation)
  - [1.3 Rabin-Karp Algorithm (Double Hash)](#13-rabin-karp-algorithm-double-hash)

## 1. String Matching

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

- length of `needle` is $m$, and length of `haystack` is $n$.
- [LeetCode question](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

### 1.1. Sliding Window

- Time: $O((n-m)m)$

### 1.2. Rabin-Karp Algorithm (Single Hash)

This algorithm is based on the concept of **hashing**. We can hash two strings and just compare the hash values instead of every charactor.

There are two issues we need to address.

1. **Spurious hits**: if two strings are equal, then their hash values will be equal. However, the reverse will no necessarily be true: `hash(string1) == hash(string2)` but `string1 != string2`.
   1. Example: define our hash function as sum of mapped values of all the characters in the string. The mapped value of a is 1, the mapped value of b is 2, and so on. Using this hash function, both `abb` and `aca` will be mapped to $1 + 2 + 2 = 5$.
2. **Time complexity**: if we calculate the hash value of every `m`-substring of haystack, then it is equivalent to iterating each character of the `m`-substring, producing the same time complexity as the sliding window approach.

We can overcome both the limitations by using the concept of **rolling hash**.

1. To overcome spurious hits, we can assign a **position weight** to each index of the string: $B^i$.
   1. Let $H(i)$ be the hash value of the `m`-substring starting at index `i`, $h(i)$ as hash value of the char at index `i`, then $H(i)=h(i)\cdot B^{(m-1)} + h(i+1)\cdot B^{(m-2) }+ \ldots + h(i+m-1)\cdot B^0$
      1. If we choose $B=10$, `aca` will be mapped to $1\cdot 10^2 + 3\cdot 10^1 + 1\cdot 10^0 = 100+30+1 = 131$ where `abb` will be mapped to $122$. However, `aal` will also be mapped to $122$.
   2. *Mathematically*, it turns out that to have a unique hash value for every `m`-substring, **$B$ should be greater than or equal to the number of characters in the set, preferably, a prime number**.
   3. The hash value may easily **overflow**. To prevent overflow, we can use modular arithmetic. This will cause spurious hits and can be minimized by using a sufficiently large prime number $\red{MOD}$.
2. It turns out that we only need to compute the hash value of the first `m`-substring of `haystack` $H(0)$ using the equation above. For $0<i<=n-m$, $H(i)=H(i-1)\cdot B−h(i-1)\cdot B^m+h(i+m-1)$. Thus, from the previous hash value, we can compute the next hash value in $O(1)$ time.
   1. With modular arithmetic, $H(i)=(H(i-1)\cdot B \mod \red{MOD} − h(i-1) \cdot B^m \mod \red{MOD} + h(i+m-1) ) \mod \red{MOD}$.

To summarize the Rabin Karp:

1. Compute the hash of each `m`-substring with rolling hash (to get constant time)
   1. We can produce a unique hash but that can result in an overflow.
   2. To prevent overflow, we will take $\red{MOD}$, but that will result in spurious hits.
   3. To minimize spurious hits, we will use a very large prime number for taking $\red{MOD}$.
2. Since we have spurious hits, if the hash matches the hash of needle, check the substring character by character.

#### 1.2.1. Complexity

- Time: $O(nm)$ in worst case, $O(n+m)$ in best case
- Space: $O(1)$

#### 1.2.2. Implementation

- [java](https://github.com/mortimerliu/LeetCode/blob/main/algorithms/java/medium/28.FindTheIndexOfTheFirstOccurrenceInAString.java)

Implementation notes:

- In Python3, we can use `ord` to convert a character to its ASCII value.
- Since Python3 can handle large integers, we need not use MOD. But operations (addition, multiplication, and subtraction) on large integers are slow.
- We should calcualate $B^m$ it iteratively, instead of using the `pow()` function, for a few reasons:
  - pow() function can overflow, and we don't want that. In Iteration, we $\red{MOD}$ the value at each step, so we are safe.
  - In java, the Math.pow() function returns a double, and it has a precision error.
- In java, we have added $\red{MOD}$ in the $O(1)$ formula to avoid downflowing to a negative value.

### 1.3 Rabin-Karp Algorithm (Double Hash)

To further reduce the chances of spurious hits, instead of a single hash value, we can compute two (or more) hash values. We need to compare these hash value pair of `needle` with hash value pair of windows of `haystack`.

We can produce different hash values by changing

- $\red{MOD}$
- $B$
- $h(\cdot)$
- WEIGHTAGE associated with characters of the string. There can be two or more versions
  - Rightmost character has weightage 1
  - Leftmost character will have weightage 1
