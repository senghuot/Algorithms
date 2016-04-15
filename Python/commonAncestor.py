# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == p or root == q: return root
        
        left_p = self.contains(root.left, p)
        left_q = self.contains(root.left, q)
        
        if (left_p and not left_q) or (not left_p and left_q):
            return root
            
        if left_p and left_q:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
        
    def contains(self, root, target):
        if root == None: return False
        
        if root == target: return True
        
        return self.contains(root.left, target) or self.contains(root.right, target)
        