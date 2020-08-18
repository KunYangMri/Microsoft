# https://leetcode.com/discuss/interview-question/684355/
# Number of fractions that sum up to 1

# Fractions are represented as two arrays, X and Y of length N.
# return number of pairs that sum to 1

from typing import List
from math import gcd
import collections

def fraction_sum(X: List[int], Y: List[int]) -> int:
    if not X or not Y or len(X) != len(Y):
        return 0
    res = 0
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            p = (X[i], Y[i])
            q = (X[j], Y[j])
            if isValid(p, q):
                res += 1

    return res

def isValid(p, q):
    denominator = p[1] * q[1]
    numerator = p[0] * q[1] + q[0] * p[1]
    return denominator == numerator

def fraction_sum2(X: List[int], Y: List[int]) -> int:
    """
    Idea: similar to 2sum
    TC: O(n), but zip takes O(m * n) for two large vectors
    """
    seen = collections.defaultdict(int)
    pair = 0
    for top, base in zip(X, Y):
        if top <= base:
            divisor = gcd(top, base)
            top, base = top // divisor, base // divisor

            if (base - top) / base in seen:
                pair += seen[(base - top) / base]

            seen[top/base] += 1

    return pair



print(fraction_sum([1, 1, 2], [3, 2, 3]) == 1)
print(fraction_sum([1, 1, 1], [2, 2, 2]) == 3)
print(fraction_sum([1, 2, 3, 1, 2, 12, 8, 4], [5, 10, 15, 2, 4, 15, 10, 5]) == 10)
print(fraction_sum2([1, 1, 2], [3, 2, 3]) == 1)
print(fraction_sum2([1, 1, 1], [2, 2, 2]) == 3)
print(fraction_sum2([1, 2, 3, 1, 2, 12, 8, 4], [5, 10, 15, 2, 4, 15, 10, 5]) == 10)
