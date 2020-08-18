# https://leetcode.com/discuss/interview-question/760379/Microsoft-or-OA-2020-or-Word-Machine

"""
A word machine is a system that performs operations
on a stack of integers. Initially stack is empty.

The sequence of operations is given as a string.
Operations are seperated by single spaces.

The following operations may be specified

- An integer X ( from 0 to 2^20-1) the machine pushes X onto stack
- "POP" the machine removes the top most number from stack
- "DUP" the machine pushes a duplicate of the topmost number onto the stack
- "+" the machine pops the two top most elemnets of stack, add them and pushes the sum
to the stack
- "-" the machine pops the two top most elements of stack,
substracts the second one from the first and pushes the result
to the stack

After processing all operations, the machine returns the topmost
value from the stack.

The machine processes 20 bit unsigned integers(numbers from 0 to 2^20-1).
An overflow in addition or underflow in substraction causes an error.
The machine also reports error when it tries to extract elements from the
stack more than it contains.
Also if after performing all errors the stack is empty return error.

input: "13 DUP 4 POP 5 DUP + DUP + -"
output: 7

input: "5 6 + -"
output: -1

input: "3 DUP 5 - -"
output: -1

1) 0<=len(s)<2000
2) S is a valid sequence of word machine operations

"""

class Solution:
    def wordMachine(self, s: str) -> int:
        operations = s.split()
        stack = []
        for op in operations:
            if op.isdigit():
                stack.append(int(op))
            elif op == 'POP':
                if not stack: return -1
                stack.pop()
            elif op == '+':
                if len(stack) < 2: return -1
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp1 + tmp2)
            elif op == 'DUP':
                if not stack: return -1
                tmp1 = stack[-1]
                stack.append(tmp1)
            elif op == '-':
                if len(stack) < 2: return -1
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                if tmp1 < tmp2: return -1
                stack.append(tmp1 - tmp2)
            else:
                return -1

        return stack[-1]


s = Solution()
test1 = "13 DUP 4 POP 5 DUP + DUP + -"
print(s.wordMachine(test1))

assert s.wordMachine("13 DUP 4 POP 5 DUP + DUP + -") == 7
assert s.wordMachine("5 6 + -") == -1
assert s.wordMachine("3 DUP 5 - -") == -1



