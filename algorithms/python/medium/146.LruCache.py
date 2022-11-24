#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (40.49%)
# Likes:    15867
# Dislikes: 680
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
#
#
#

# @lc code=start
# from heapq import heappop, heappush
# from itertools import count


# class LRUCache:
#     def __init__(self, capacity: int):
#         """
#         HashMap + MinHeap
#         """
#         self.capacity = capacity
#         # kv_map hold the value for the key and also indicate whether
#         # a key exists or not
#         self.kv_map = {}
#         # merely for maintaining the usage order
#         self.order = []
#         self.counter = count()

#     def get(self, key: int) -> int:
#         if key not in self.kv_map:
#             return -1
#         self._push_record(key, self.kv_map[key][0], next(self.counter))
#         return self.kv_map[key][0]

#     def put(self, key: int, value: int) -> None:
#         self._push_record(key, value, next(self.counter))
#         if len(self.kv_map) > self.capacity:
#             self._remove_least_recent()

#     def _push_record(self, key: int, value: int, cnt: int) -> None:
#         self.kv_map[key] = (value, cnt)
#         heappush(self.order, (cnt, key))

#     def _remove_least_recent(self) -> None:
#         while True:
#             cnt, key = heappop(self.order)
#             if key in self.kv_map and self.kv_map[key][1] == cnt:
#                 del self.kv_map[key]
#                 break


from algorithms.python.common import ListNode


class LRUCache:
    def __init__(self, capacity: int):
        """
        HashMap + MinHeap
        """
        self.capacity = capacity
        # a dict holding the value for the key and also indicate whether
        # a key exists or not
        self.kv_map = {}
        # a double linked list merely for maintaining the usage order
        # head -> tail: most recent -> least recent
        self.head = ListNode()  # dummy
        self.tail = ListNode()  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.kv_map:
            return -1
        self._push_to_head(self.kv_map[key])
        return self.kv_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            node = self.kv_map[key]
            node.val = value
            self._push_to_head(node)
        else:
            node = ListNode(val=value, key=key)
            self.kv_map[key] = node
            self._add_to_head(node)

            if len(self.kv_map) > self.capacity:
                tail = self._pop_tail()
                del self.kv_map[tail.key]

    def _add_to_head(self, node: ListNode) -> None:
        """Add a new node to head"""
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def _remove_node(self, node: ListNode) -> None:
        """Remove a node"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pop_tail(self) -> ListNode:
        """Remove the node at the tail"""
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def _push_to_head(self, node: ListNode) -> None:
        """Push an exisiting node to head"""
        self._remove_node(node)
        self._add_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
