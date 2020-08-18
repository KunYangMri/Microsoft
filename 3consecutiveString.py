from itertools import groupby
def solution(S):

    return sum(len(list(group)) // 3 for key, group in groupby(S))




def solution3(s):
    left, right = 0, 0
    res = 0
    while left < len(s):
        tmp = 1
        right = left + 1
        while right < len(s) and s[left] == s[right]:
            tmp += 1
            right += 1
        res += tmp // 3
        left = right

    return res



test1 = "aaaabaaabbbb"
test2 = 'baaabbaabbba'
test3 = 'baabab'
print(solution3(test1))


