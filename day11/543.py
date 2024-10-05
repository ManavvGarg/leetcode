from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        # res[0] = diameter
        # passing array as reference to reflect changes outside functions

        # recursive function definition
        def getDiameter(res, node):
            # if node turns out be to null then we return 0
            if not node:
                return 0
            
            # recursive to find the left node
            leftPaths = getDiameter(res, node.left)
            # recursive to find the right node
            rightPaths = getDiameter(res, node.right)

            # calculating the diameter as the max of (leftMost Node + rightMost Node) and already existing res[0]
            res[0] = max(res[0], leftPaths + rightPaths)

            # returning max of left or right + 1 for furthere recursive calls
            return max(leftPaths, rightPaths) + 1


        getDiameter(res, root) 
        
        return res[0]