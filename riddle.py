# no letter appears next to another letter of the same kind
# input = 'ab?ac?', one potential ouput = "abcaca"
# input = "????????", one potential output is "codility"

def riddle(s: str):
    """
    Time: O(N)
    Space: O(1)
    """
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for j in range(26):
                char = chr(ord('a') + j)

                left = i == 0 or s[i - 1] != char
                right = i == len(s) - 1 or s[i+1] != char
                if left and right:
                    s[i] = char
                    break
    return ''.join(s)

if __name__ == "__main__":
    s = ["ab?ac?", "rd?e?wg??", "????????"]
    print(riddle(s[1]))
