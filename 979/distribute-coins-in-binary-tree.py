# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        take = 0
        (_, take) = self.helper(root, take)

        return take

    def helper(self, node: Optional[TreeNode], take) -> int:
        if node == None:
            return (0, take)

        (left, take_l) = self.helper(node.left, take)
        (right, take_r) = self.helper(node.right, take)

        take += abs(left) + abs(right) + take_l + take_r

        return (left + right + node.val - 1, take)
