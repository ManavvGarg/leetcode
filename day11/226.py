from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root return
        if not root:
            return
        
        # swap left and right child nodes of a node
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # use recursion to get to the leaf node
        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)
        
        return root

        