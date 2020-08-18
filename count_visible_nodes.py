# https://leetcode.com/discuss/interview-question/546703/
# similar question:

# Count Visible Nodes in Binary Tree
# In a binary tree, if in the path from root to the node A,
# there is no node with greater value than A’s,
# this node A is visible. We need to count the number of visible nodes in a binary tree

# """
# Example 1:
#
# Input:
#         5
#      /     \
#    3        10
#   /  \     /
# 20   21   1
#
# Output: 4
# Explanation: There are 4 visible nodes: 5, 20, 21, and 10.
# """
import collections
import sys
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # use recursion
    def countNodes(self, root):
        if not root: return 0

        def traverse(root, max_value):
            if not root: return 0
            visible = 1 if root.val >= max_value else 0
            max_value = max(root.val, max_value)
            return traverse(root.left, max_value) + visible + traverse(root.right, max_value)

        return traverse(root, float('-inf'))

    # use iteration, not tested for many cases
    def countNodes2(self, root):
        if not root: return 0
        max_value = -sys.maxsize
        start = root
        res = 0
        stack = []
        while root or stack:
            if root:
                if root.val > max_value:
                    res += 1
                    max_value = root.val
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node == start:  # here reset the max_value, cause it going to the right subtree
                    max_value = start.val
                root = node.right
        return res

    # use BFS: relatively commonly used template

    def countNodes3(self, root) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append((root, -sys.maxsize))
        res = 0

        while queue:
            node, max_value = queue.popleft()
            if node.val >= max_value:
                max_value = node.val
                res += 1

            if node.left:
                queue.append((node.left, max_value))
            if node.right:
                queue.append((node.right, max_value))

        return res


if __name__ == '__main__':
    s = Solution()
    # Build a test tree
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.left.left = TreeNode(20)
    tree.left.right = TreeNode(21)
    tree.right = TreeNode(10)
    tree.right.left = TreeNode(1)

    assert s.countNodes(tree) == 4
    print(s.countNodes3(tree))
    assert s.countNodes2(tree) == 4
    assert s.countNodes3(tree) == 4


