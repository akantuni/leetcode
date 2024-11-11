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
    public List<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> postorder = new ArrayList<>();
        postorderHelper(root, postorder);
        return postorder;
    }

    private void postorderHelper(TreeNode root, ArrayList<Integer> postorder) {
        if (root == null) {
            return;
        }
        postorderHelper(root.left, postorder);
        postorderHelper(root.right, postorder);
        postorder.add(root.val);
    }
}