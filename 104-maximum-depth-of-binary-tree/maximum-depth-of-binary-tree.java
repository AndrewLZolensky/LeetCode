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
    public int maxDepth(TreeNode root) {

        // base case 1: null node, max depth = 0
        if (root == null) {
            return 0;
        }

        // base case 2: no children, max depth = 1
        if ((root.left == null) && (root.right == null)) {
            return 1;
        }

        // left child only: max depth = max depth left child + 1
        if (root.right == null) {
            return maxDepth(root.left) + 1;
        }

        // right child only: max depth = max depth right child + 1
        if (root.left == null) {
            return maxDepth(root.right) + 1;
        }

        // both children: max depth = max (max depth left child + 1, max depth right child + 1)
        int left_depth = maxDepth(root.left);
        int right_depth = maxDepth(root.right);
        if (left_depth > right_depth) {
            return left_depth + 1;
        }
        return right_depth + 1;
    }
}