#
# @lc app=leetcode id=1274 lang=python3
#
# [1274] Number of Ships in a Rectangle
#
# https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/
#
# algorithms
# Hard (69.40%)
# Likes:    486
# Dislikes: 53
# Total Accepted:    25K
# Total Submissions: 36.2K
# Testcase Example:  '[[1,1],[2,2],[3,3],[5,5]]\n[4,4]\n[0,0]'
#
# (This problem is an interactive problem.)
#
# Each ship is located at an integer point on the sea represented by a
# cartesian plane, and each integer point may contain at most 1 ship.
#
# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points
# as arguments and returns true If there is at least one ship in the rectangle
# represented by the two points, including on the boundary.
#
# Given two points: the top right and bottom left corners of a rectangle,
# return the number of ships present in that rectangle. It is guaranteed that
# there are at most 10 ships in that rectangle.
#
# Submissions making more than 400 calls to hasShips will be judged Wrong
# Answer. Also, any solutions that attempt to circumvent the judge will result
# in disqualification.
#
#
# Example :
#
#
# Input:
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
#
#
# Example 2:
#
#
# Input: ans = [[1,1],[2,2],[3,3]], topRight = [1000,1000], bottomLeft = [0,0]
# Output: 3
#
#
#
# Constraints:
#
#
# On the input ships is only given to initialize the map internally. You must
# solve this problem "blindfolded". In other words, you must find the answer
# using the given hasShips API, without knowing the ships position.
# 0 <= bottomLeft[0] <= topRight[0] <= 1000
# 0 <= bottomLeft[1] <= topRight[1] <= 1000
# topRight != bottomLeft
#
#
#


# @lc code=start
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#     def hasShips(self, topRight: "Point", bottomLeft: "Point") -> bool:
#         return False


# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y


class Solution:
    def countShips(self, sea: "Sea", topRight: "Point", bottomLeft: "Point") -> int:
        # binary search / divide and conquer
        def binarySplit(topRight, bottomLeft):
            if topRight.y - bottomLeft.y >= topRight.x - bottomLeft.x:
                m = (topRight.y + bottomLeft.y) // 2
                return [
                    [bottomLeft, Point(topRight.x, m)],
                    [Point(bottomLeft.x, m + 1), topRight],
                ]
            else:
                m = (topRight.x + bottomLeft.x) // 2
                return [
                    [bottomLeft, Point(m, topRight.y)],
                    [Point(m + 1, bottomLeft.y), topRight],
                ]

        count = 0
        questions = binarySplit(topRight, bottomLeft)
        while questions:
            bl, tr = questions.pop()
            if sea.hasShips(tr, bl):
                if bl.x == tr.x and bl.y == tr.y:
                    count += 1
                else:
                    questions.extend(binarySplit(tr, bl))
        return count


# @lc code=end
