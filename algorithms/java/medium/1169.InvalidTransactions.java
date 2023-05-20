/*
 * @lc app=leetcode id=1169 lang=java
 *
 * [1169] Invalid Transactions
 *
 * https://leetcode.com/problems/invalid-transactions/description/
 *
 * algorithms
 * Medium (31.19%)
 * Likes:    450
 * Dislikes: 2084
 * Total Accepted:    62K
 * Total Submissions: 199K
 * Testcase Example:  '["alice,20,800,mtv","alice,50,100,beijing"]'
 *
 * A transaction is possibly invalid if:
 * 
 * 
 * the amount exceeds $1000, or;
 * if it occurs within (and including) 60 minutes of another transaction with
 * the same name in a different city.
 * 
 * 
 * You are given an array of strings transaction where transactions[i] consists
 * of comma-separated values representing the name, time (in minutes), amount,
 * and city of the transaction.
 * 
 * Return a list of transactions that are possibly invalid. You may return the
 * answer in any order.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
 * Output: ["alice,20,800,mtv","alice,50,100,beijing"]
 * Explanation: The first transaction is invalid because the second transaction
 * occurs within a difference of 60 minutes, have the same name and is in a
 * different city. Similarly the second one is invalid too.
 * 
 * Example 2:
 * 
 * 
 * Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
 * Output: ["alice,50,1200,mtv"]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
 * Output: ["bob,50,1200,mtv"]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * transactions.length <= 1000
 * Each transactions[i] takes the form "{name},{time},{amount},{city}"
 * Each {name} and {city} consist of lowercase English letters, and have
 * lengths between 1 and 10.
 * Each {time} consist of digits, and represent an integer between 0 and
 * 1000.
 * Each {amount} consist of digits, and represent an integer between 0 and
 * 2000.
 * 
 * 
 */

// @lc code=start
import java.util.*;

class Transaction {
    String name;
    int time;
    int amount;
    String city;

    public Transaction(String txn) {
        // split the string and parse it
        String[] split = txn.split(",");
        name = split[0];
        time = Integer.parseInt(split[1]);
        amount = Integer.parseInt(split[2]);
        city = split[3];
    }
}

class Solution {
    Map<String, HashMap<Integer, Set<String>>> mapTrans;

    public List<String> invalidTransactions(String[] transactions) {
        // O(N)
        mapTrans = new HashMap<>();
        for (String txn : transactions) {
            Transaction split = new Transaction(txn);
            if (!mapTrans.containsKey(split.name)) {
                mapTrans.put(split.name, new HashMap<>());
            }
            if (!mapTrans.get(split.name).containsKey(split.time)) {
                mapTrans.get(split.name).put(split.time, new HashSet<>());
            }
            mapTrans.get(split.name).get(split.time).add(split.city);
        }

        List<String> invalid = new ArrayList<>();
        for (String txn : transactions) {
            Transaction split = new Transaction(txn);
            if (!isValid(split)) {
                invalid.add(txn);
            }
        }
        return invalid;
    }

    private boolean isValid(Transaction split) {
        if (split.amount > 1000) {
            return false;
        }
        for (int t = split.time - 60; t <= split.time + 60; t++) {
            if (mapTrans.get(split.name).containsKey(t)) {
                Set<String> cities = mapTrans.get(split.name).get(t);
                if (cities.size() > 1 || !cities.contains(split.city)) {
                    return false;
                }
            }
        }
        return true;
    }
}
// @lc code=end
