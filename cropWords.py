# https://leetcode.com/discuss/interview-question/507367/

# give  a message containing english alphabet letters and spaces
# longer than limit, you need to crop a number of words from the
# end of the message, some requirements:
# 1. may not exceed K character limiit but as long as possible
# 2. may not crop away part of a word
# 3. output may not end with a space

# examole "codility we test coders" output "codility we"

def cropWords(s: str, k: int):
    if len(s) <= k:
        return s.rstrip()   # rstrip remove the space at the end

    # check if k finished in the middle of the word
    truncate_word = True if k < len(s) and s[k] != ' ' else False

    s = s[0:k]
    if truncate_word:
        while len(s) > 0 and s[-1] != ' ':
            s = s[:-1]

    return s.rstrip()

    # RTC: O(N), SC: O(1)

# test cases:

assert cropWords("codility We test coders", 14) == "codility We"
assert cropWords(" co de my", 5) == " co"
assert cropWords(" co de my", 7) == " co de"
assert cropWords("   ", 2) == ""
assert cropWords("   re", 2) == "" #3 spaces before
assert cropWords(" c ", 3) == " c"
assert cropWords(" c d  ", 5) == " c d"
assert cropWords("co de my", 5) == "co de"
assert cropWords("Word", 4) == "Word"
assert cropWords("codility We test coders", 23) == "codility We test coders"
assert cropWords("withOutSpaces", 14) == "withOutSpaces"
assert cropWords("", 14) == ""
assert cropWords("Separatedby hyphens", 14) == "Separatedby"
assert cropWords("      Codility We test coders     ", 14) == "      Codility" #6 leading spaces
assert cropWords("      Codility We test coders     ", 10) == "" #6 leading spaces





