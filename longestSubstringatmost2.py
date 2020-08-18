#Longest Substring Without 3 Contiguous Occurrences of Letter

def longestWithout3(s: str):
    if len(s) < 3: return s
    start, left, right = 0, 0, 1
    maxLength = 0
    count = 1
    char = s[0]

    while right < len(s):
        if s[right] == char:
            count += 1
            if count == 2:
                if right - left + 1 > maxLength:
                    maxLength = right -left + 1
                    start = left
            else:
                left = right - 1
        else:
            char = s[right]
            count = 1
            if right - left + 1 > maxLength:
                maxLength = right - left + 1
                start = left

        right += 1

    return s[start: start + maxLength]

S = "aabbaaaaabb"
print(longestWithout3(S))

S = "aabbaabbaabbaa"
print(longestWithout3(S))
