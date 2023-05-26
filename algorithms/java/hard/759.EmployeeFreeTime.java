/*
 * @lc app=leetcode id=759 lang=java
 *
 * [759] Employee Free Time
 *
 * https://leetcode.com/problems/employee-free-time/description/
 *
 * algorithms
 * Hard (71.73%)
 * Likes:    1749
 * Dislikes: 120
 * Total Accepted:    132.7K
 * Total Submissions: 184.7K
 * Testcase Example:  '[[[1,2],[5,6]],[[1,3]],[[4,10]]]'
 *
 * We are given a list schedule of employees, which represents the working time
 * for each employee.
 *
 * Each employee has a list of non-overlapping Intervals, and these intervals
 * are in sorted order.
 *
 * Return the list of finite intervals representing common, positive-length
 * free time for all employees, also in sorted order.
 *
 * (Even though we are representing Intervals in the form [x, y], the objects
 * inside are Intervals, not lists or arrays. For example, schedule[0][0].start
 * = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also,
 * we wouldn't include intervals like [5, 5] in our answer, as they have zero
 * length.
 *
 *
 * Example 1:
 *
 *
 * Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
 * Output: [[3,4]]
 * Explanation: There are a total of three employees, and all common
 * free time intervals would be [-inf, 1], [3, 4], [10, inf].
 * We discard any intervals that contain inf as they aren't finite.
 *
 *
 * Example 2:
 *
 *
 * Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
 * Output: [[5,6],[7,9]]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= schedule.length , schedule[i].length <= 50
 * 0 <= schedule[i].start < schedule[i].end <= 10^8
 *
 *
 */

// @lc code=start

// Definition for an Interval.
import java.util.*;

/*
class Interval {
    public int start;
    public int end;

    public Interval() {
    }

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Pair implements Comparable<Pair> {
    Interval interval;
    int i;
    int j;

    Pair(Interval interval, int i, int j) {
        this.interval = interval;
        this.i = i;
        this.j = j;
    }

    @Override
    public int compareTo(Pair other) {
        // compareTo should return < 0 if this is supposed to be
        // less than other, > 0 if this is supposed to be greater than
        // other and 0 if they are supposed to be equal
        return this.interval.start - other.interval.start;
    }
}

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        // // line sweep
        // // Time O(nlogn)
        // List<Interval> intervals = new ArrayList<>();
        // for (List<Interval> emp : schedule) {
        // for (Interval interval : emp) {
        // intervals.add(interval);
        // }
        // }
        // Collections.sort(intervals, (a, b) -> a.start - b.start);

        // List<Interval> free = new ArrayList<>();
        // int end = intervals.get(0).end;
        // for (Interval interval : intervals) {
        // if (end < interval.start) {
        // free.add(new Interval(end, interval.start));
        // }
        // end = Math.max(end, interval.end);
        // }
        // return free;

        // better implementation - Priority Queue
        // use the fact that interval for same employee are not overlapping
        // Time O(nlogk), Space O(k)
        PriorityQueue<Pair> intervals = new PriorityQueue<>();
        for (int i = 0; i < schedule.size(); i++) {
            intervals.offer(new Pair(schedule.get(i).get(0), i, 0));
        }

        List<Interval> free = new ArrayList<>();
        int end = intervals.peek().interval.end;
        while (!intervals.isEmpty()) {
            Pair cur = intervals.poll();
            if (end < cur.interval.start) {
                free.add(new Interval(end, cur.interval.start));
            }
            end = Math.max(end, cur.interval.end);
            if (cur.j + 1 < schedule.get(cur.i).size()) {
                intervals.offer(new Pair(schedule.get(cur.i).get(cur.j + 1), cur.i, cur.j + 1));
            }
        }
        return free;

    }
}
// @lc code=end
