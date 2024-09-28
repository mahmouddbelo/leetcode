# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of the nodes is None or the values are different, they are not the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage
# Creating two identical trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

solution = Solution()
print(solution.isSameTree(tree1, tree2))  # Output: True

# Creating two different trees
tree3 = TreeNode(1)
tree3.left = TreeNode(2)

tree4 = TreeNode(1)
tree4.right = TreeNode(2)

print(solution.isSameTree(tree3, tree4))  # Output: False
