/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> inorder = new ArrayList<>();
        inorderHelper(root, inorder);
        return inorder;
    }

    private void inorderHelper(TreeNode root, ArrayList<Integer> inorder) {
        if (root == null) {
            return;
        }
        inorderHelper(root.left, inorder);
        inorder.add(root.val);
        inorderHelper(root.right, inorder);
    }
}