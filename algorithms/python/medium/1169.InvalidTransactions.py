#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#
# https://leetcode.com/problems/invalid-transactions/description/
#
# algorithms
# Medium (31.19%)
# Likes:    450
# Dislikes: 2084
# Total Accepted:    62K
# Total Submissions: 199K
# Testcase Example:  '["alice,20,800,mtv","alice,50,100,beijing"]'
#
# A transaction is possibly invalid if:
#
#
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with
# the same name in a different city.
#
#
# You are given an array of strings transaction where transactions[i] consists
# of comma-separated values representing the name, time (in minutes), amount,
# and city of the transaction.
#
# Return a list of transactions that are possibly invalid. You may return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction
# occurs within a difference of 60 minutes, have the same name and is in a
# different city. Similarly the second one is invalid too.
#
# Example 2:
#
#
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
#
#
# Example 3:
#
#
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]
#
#
#
# Constraints:
#
#
# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths
# between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and
# 1000.
# Each {amount} consist of digits, and represent an integer between 0 and
# 2000.
#
#
#


# @lc code=start
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # O(NlogN)
        def parse(txn):
            name, time, amt, city = txn.split(",")
            return name, int(time), int(amt), city

        # by_name = {}
        # for i, txn in enumerate(transactions):
        #     name, time, amt, city = parse(txn)
        #     if name not in by_name:
        #         by_name[name] = []
        #     by_name[name].append((time, amt, city, i))

        # invalid = []
        # for name, txns in by_name.items():
        #     txns.sort()
        #     by_city = []
        #     prev_city = None
        #     for time, amt, city, i in txns:
        #         if prev_city != city:
        #             by_city.append([])
        #         by_city[-1].append([time, amt, i])
        #         prev_city = city
        #     for j in range(len(by_city)):
        #         for k, (time, amt, i) in enumerate(by_city[j]):
        #             if (
        #                 amt > 1000
        #                 or (j > 0 and time - 60 <= by_city[j - 1][-1][0])
        #                 or (j + 1 < len(by_city) and time + 60 >= by_city[j + 1][0][0])
        #             ):
        #                 print(time, amt, i)
        #                 invalid.append(transactions[i])
        # return invalid

        # O(N)
        mapped_transactions = collections.defaultdict(
            lambda: collections.defaultdict(set)
        )

        for transaction in transactions:
            name, time, amount, city = parse(transaction)
            mapped_transactions[name][time].add(city)

        result = []
        for transaction in transactions:
            name, time, amount, city = parse(transaction)
            if amount > 1000:
                result.append(transaction)
                continue
            for t in range(time - 60, time + 61):
                if t in mapped_transactions[name] and (
                    len(mapped_transactions[name][t]) > 1
                    or city not in mapped_transactions[name][t]
                ):
                    result.append(transaction)
                    break

        return result


# @lc code=end
