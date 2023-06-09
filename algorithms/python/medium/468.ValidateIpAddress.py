#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (26.55%)
# Likes:    859
# Dislikes: 2604
# Total Accepted:    143.5K
# Total Submissions: 539K
# Testcase Example:  '"172.16.254.1"'
#
# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6"
# if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any
# type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255
# and xi cannot contain leading zeros. For example, "192.168.1.1" and
# "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00",
# and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8"
# where:
#
#
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter
# ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
#
#
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
# "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while
# "2001:0db8:85a3::8A2E:037j:7334" and
# "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
#
#
# Example 1:
#
#
# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
#
#
# Example 2:
#
#
# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
#
#
# Example 3:
#
#
# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
#
#
#
# Constraints:
#
#
# queryIP consists only of English letters, digits and the characters '.' and
# ':'.
#
#
#


# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.check_ipv4(queryIP):
            return "IPv4"
        if self.check_ipv6(queryIP):
            return "IPv6"
        return "Neither"

    def check_ipv4(self, queryIP):
        segs = queryIP.split(".")
        if len(segs) != 4:
            return False
        for seg in segs:
            if (
                not seg.isnumeric()
                or int(seg) > 255
                or (int(seg) == 0 and len(seg) > 1)
                or (int(seg) > 0 and seg[0] == "0")
            ):
                return False
        return True

    def check_ipv6(self, queryIP):
        segs = queryIP.split(":")
        if len(segs) != 8:
            return False
        for seg in segs:
            if not (1 <= len(seg) <= 4):
                return False
            for c in seg:
                if c not in "0987654321ABCDEFabcdef":
                    return False
        return True


# @lc code=end
