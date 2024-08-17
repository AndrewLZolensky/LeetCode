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
    public TreeNode invertTree(TreeNode root) {

        // null guard
        if (root == null) {
            return null;
        }

        // otherwise switch right and left children, then visit them
        TreeNode holder = root.left;
        root.left = root.right;
        root.right = holder;

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}