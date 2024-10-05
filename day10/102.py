from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is none then return 0.
        if root == None:
            return 0
        # recursive call to check all the nodes on the left of the root
        leftDepth = self.maxDepth(root.left)
        # recursive call to check all the nodes on the right of the root
        rightDepth = self.maxDepth(root.right)

        # accounting for depth = 1 at root, we do 1 + max(left, right), where left and right are two different depths of the tree. We need the max depth
        return 1 + max(leftDepth, rightDepth)