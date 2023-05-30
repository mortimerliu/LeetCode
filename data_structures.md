- [Summary](#summary)
- [Abstract Data-Type (ADT)](#abstract-data-type-adt)
  - [Priority Queue](#priority-queue)
- [Data Structure](#data-structure)
  - [Heap](#heap)
  - [Bianry Heap](#bianry-heap)
  - [Self-Balancing Binary Search Tree](#self-balancing-binary-search-tree)
  - [AVL Tree](#avl-tree)
  - [Red–Black Tree](#redblack-tree)
  - [Disjoint-Set](#disjoint-set)


# Summary
<!-- no toc -->
* [Priority Queue](#priority-queue)
  * [Heap](#heap)
    * [Binary Heap](#bianry-heap)
  * [Self-Balancing Binary Search Tree](#self-balancing-binary-search-tree)
    * [AVL Tree](#avl-tree)
    * [Red–Black Tree](#red–black-tree)
* [Disjoint-Set](#disjoint-set)

# Abstract Data-Type (ADT)

## [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue)

A priority queue is an **abstract data-type** similar to a regular queue or stack data structure.

* Each element in a priority queue has an associated **priority**.
* **Elements with high priority are served before elements with low priority**.

Stacks and queues can be implemented as particular kinds of priority queues, with the priority determined by the order in which the elements are inserted.

### Operations<!-- omit from toc -->

A priority queue must at least support the following operations:

* `is_empty`: check if the queue has no elements
* `insert(element, priority)`: insert an element with an associated priority
* `pop()`: remove the element with highest priority and return it
* `peek()`: return the element with priority

More advanced implementations may support more complicated operations, such as:

* pull lowest priority element
* inspecting the first few highest- or lowest-priority elements
* clearing the queue
* clearing subsets of the queue
* performing a batch insert
* merging two or more queues into one
* incrementing priority of any element

### Implementation<!-- omit from toc -->

* [heap](#heap)
  * insert: $O(\text{log} n)$
  * delete: $O(\text{log} n)$
  * build: $O(n)$
  * search: $O(n)$
* [self-balancing binary search tree](#self-balancing-binary-search-tree)
  * insert: $O(\text{log} n)$
  * delete: $O(\text{log} n)$
  * build: $O(n\text{log} n)$
  * search: $O(\log n)$

Links

* [Compare between heap and balacned BST](https://stackoverflow.com/questions/65882138/implementing-priority-queue-using-max-heap-vs-balanced-bst)

# Data Structure

## [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))

A **heap** is a specialized tree-based data structure which is essentially an almost complete binary tree that satisfies the **heap property**:

* In a max/min heap, for any given node $C$, if $P$ is a parent node of $C$, then the key (the value) of $P$ is greater/smaller than or equal to the key of $C$

The heap is one *maximally efficient* implementation of a [priority queue](#priority-queue).

### Operations<!-- omit from toc -->

For max heap:

* `find-max`/`peek`
* `insert`/`push`
* `extract-max`/`pop`
* `delete-max`
* `replace`: pop root and push a new key
* `create-heap`: create an empty heap
* `heapify`: create a heap out of given array of elements
* `merge`: joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps
* `meld`: joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps
* `size`
* `is-empty`
* `increase-key`, `decrease-key`: updating a key
* `delete`: delete an arbitrary node
* `sift-up`, `sift-down`: move a node up/down in the tree, as long as needed; used to restore heap condition after insertion

### Implementation<!-- omit from toc -->

Heaps are usually implemented with an array, as follows:

* Each element in the array represents a node of the heap.
* The parent/child relationship is defined implicitly by the elements' indices in the array.

#### Common variants<!-- omit from toc -->

* [Binary heap](#bianry-heap)

## [Bianry Heap](https://en.wikipedia.org/wiki/Binary_heap)

A **binary heap** is a heap data structure that takes the form of a binary tree with two additional constraints:

* **Shape property**: a binary heap is a complete binary tree:
  * all levels of the tree, except possibly the last one (deepest) are fully filled
  * if the last level of the tree is not complete, the nodes of that level are filled from left to right.
* **Heap property**: the key stored in each node is either greater than or equal to ($≥$) or less than or equal to ($≤$) the keys in the node's children, according to some total order.

Binary heaps are a common way of implementing priority queues.

### Implementation<!-- omit from toc -->

Heaps are commonly implemented with an array.

Let `n` be the number of elements in the heap and `i` be an arbitrary valid index of the array storing the heap.

For `0`-indexed array:

* children at indices `2i + 1` and `2i + 2`
* its parent at index `floor((i − 1) / 2)`

Alternatively, for `1`-indexed array

* children at indices `2i` and `2i +1`
* its parent at index `floor(i / 2)`

Python: [`heapq`](https://docs.python.org/3/library/heapq.html)

**Complexity**

| Operation  | Average     | Worst case  |
| ---------- | ----------- | ----------- |
| Search     | $O(n)$      | $O(n)$      |
| Insert     | $O(1)$      | $O(\log n)$ |
| Find-min   | $O(1)$      | $O(1)$      |
| Delete-min | $O(\log n)$ | $O(\log n)$ |
| Delete-min | -           | $O(\log n)$ |

## [Self-Balancing Binary Search Tree](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

A **self-balancing** binary search tree (BST) is any node-based binary search tree that automatically keeps its height (maximal number of levels below the root) small in the face of arbitrary item insertions and deletions.

For **height-balanced** binary trees, the height is defined to be logarithmic $O(\log n)$ in the number $n$ of items. This is the case for many binary search trees, such as AVL trees and red–black trees.

In the asymptotic ("Big-O") sense, a self-balancing BST structure containing n items allows the lookup, insertion, and removal of an item in $O(\log n)$ worst-case time, and ordered enumeration of all items in $O(n)$ time.

### Implementation<!-- omit from toc -->

* [AVL tree](#avl-tree)
  | Operation | Amortized   | Worst case  |
  | --------- | ----------- | ----------- |
  | Search    | $O(\log n)$ | $O(\log n)$ |
  | Insert    | $O(\log n)$ | $O(\log n)$ |
  | Delete    | $O(\log n)$ | $O(\log n)$ |
* [Red–black tree](#red-black-tree)
  | Operation | Amortized   | Worst case  |
  | --------- | ----------- | ----------- |
  | Search    | $O(\log n)$ | $O(\log n)$ |
  | Insert    | $O(1)$      | $O(\log n)$ |
  | Delete    | $O(1)$      | $O(\log n)$ |

## [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree)

An **AVL tree** (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree.

* The heights of the two child subtrees of any node differ by at most one.
* If at any time they differ by more than one, rebalancing is done to restore this property.\
* Lookup, insertion, and deletion all take $O(\log n)$ time in both the average and worst cases.

### Implementation<!-- omit from toc -->

**Complexity**

| Operation | Amortized   | Worst case  |
| --------- | ----------- | ----------- |
| Search    | $O(\log n)$ | $O(\log n)$ |
| Insert    | $O(\log n)$ | $O(\log n)$ |
| Delete    | $O(\log n)$ | $O(\log n)$ |

## [Red–Black Tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)

A **red–black tree** is a specialised binary search tree data structure noted for fast storage and retrieval of ordered information, and a guarantee that operations will complete within a known time.

* The nodes in a red-black tree hold an extra bit called "color" representing "red" and "black" which is used when re-organising the tree to ensure that it is always approximately balanced.

### Implementation<!-- omit from toc -->

**Complexity**

| Operation | Amortized   | Worst case  |
| --------- | ----------- | ----------- |
| Search    | $O(\log n)$ | $O(\log n)$ |
| Insert    | $O(1)$      | $O(\log n)$ |
| Delete    | $O(1)$      | $O(\log n)$ |

## [Disjoint-Set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

A **disjoint-set** data structure, also called a union-find data structure or merge-find set, is a data structure that stores a collection of disjoint (non-overlapping) sets.

### Implementation<!-- omit from toc -->

* [Java](https://github.com/mortimerliu/LeetCode/blob/main/algorithms/java/common/DisjointSet.java)
* [Python](https://github.com/mortimerliu/LeetCode/blob/main/algorithms/python/common/disjoint_set.py)

**Complexity**

* A disjoint-set forest implementation in which `Find` does not update parent pointers, and in which `Union` does not attempt to control tree heights, can have trees with height $O(n)$. In such a situation, the `Find` and `Union` operations require $O(n)$ time.
* The combination of path compression with union by size or by rank, reduces the running time for m operations of any type, up to n of which are MakeSet operations, to $\Theta(m\alpha(n))$. This makes the amortized running time of each operation $\Theta(\alpha(n))$. This is asymptotically optimal, meaning that every disjoint set data structure must use $\Omega(\alpha (n))$ amortized time per operation. Here, the function $\alpha (n)$ is the [inverse Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function#Inverse). The inverse Ackermann function grows extraordinarily slowly, so this factor is 4 or less for any n that can actually be written in the physical universe. This makes disjoint-set operations **practically amortized constant time**.
