# https://leetcode.com/discuss/interview-question/398037/
# string S of length N containing only characters 'a' and 'b'
# semi alternating substring is does not contain three identical consecutive characters
# return the length of the longest semi-alternating substring of S


def longest_semi(s):
    max_len = 0
    left = 0
    for right in range(len(s)):
        if right - left + 1 >= 3 and s[right] == s[right - 1] == s[right - 2]:
            left = right - 1
        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_semi('abaaaa')) # 4
print(longest_semi('babba')) # 5
print(longest_semi('baaabbabbb')) # 7