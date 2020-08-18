# Microsoft | OA 2020 | Largest M-aligned subset
# https://leetcode.com/discuss/interview-question/525894/Microsoft-or-OA-2020-or-m-aligned-subset

# Solution priciple: i % m == j % m, then (i - j) % m == 0, all numbers in a group have the same remainder after dividing by m
# example:
# A = [-3, -2, 1, 0, 8, 7, 1]
# R = [0, 1, 1, 0, 2, 1, 1], where R[i] = A[i] % m

# TC O(n). SC O(1)

from typing import List

def largest_m_aligned(nums: List[int], m: int) -> int:
    if m == 0: return 0

    remainders = [0] * m

    for num in nums:
        remainders[num % m] += 1

    return max(remainders)


if __name__ == "__main__":
    print(largest_m_aligned([-3, -2, 1, 0, 8, 7, 1], 3) == 4)  # [-2, 1, 7, 1]
    print(largest_m_aligned([7, 2, 4, 8, 6], 2) == 4)  # [2, 4, 6, 8]
    print(largest_m_aligned([3, 1, 4, 1, 5], 1) == 5)  # [3, 1, 4, 1, 5]
    print(largest_m_aligned([5, 5, 5, 5, 5], 0) == 0)  # []
    print(largest_m_aligned([4, 7, 10, 6, 9], 3) == 3)  # [4, 7, 10]