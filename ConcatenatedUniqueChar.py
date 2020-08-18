# https://leetcode.com/discuss/interview-question/401826/
# Concatenated string length with unique Characters

# Related: leetcode 1239
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# It's a NP-hard problem, any O(ploy(N)) is wrong.
# Enumerating all posisble subsets O(2^N) either via DFS or BFS with early pruning is the best you can do

def maxLength(array):
    comb = [set(word) for word in array if len(set(word)) == len(word)]

    queue = [set()]

    for charSet in comb:
        for wordSet in comb:
            if not (charSet & wordSet):
                queue.append(charSet | wordSet)

    if len(queue) == 1:
        return 0

    for charSet in comb:
        for wordSet in queue:
            queue.append(charSet | wordSet)

    return max(len(charSet) for charSet in queue)

print(maxLength(["co","dil","ity"]))
print(maxLength(["abc","kkk","def","csv"]))
print(maxLength(["abc","ade","akl"]))




