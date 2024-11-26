# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def ldepth(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def rdepth(node):
            h = 0
            while node:
                h += 1
                node = node.right
              
            return h

        leftHeight = ldepth(root.left)
        rightHeight = rdepth(root.right)

        if leftHeight == rightHeight:
  
           
            return 2**(leftHeight + 1) - 1
        else:

            return 1+ self.countNodes(root.left) + self.countNodes(root.right)





        
        