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
    public boolean isValidBST(TreeNode root) {
        return isValidSubtree(root, null, null);
    }

    public boolean isValidSubtree(TreeNode root, Integer min, Integer max) {

        // check condition
        if ((min != null) || (max != null)) {
            if (min == null) {
                if (root.val >= max) {
                    return false;
                }
            } else if (max == null) {
                if (root.val <= min) {
                    return false;
                }
            } else {
                if ((root.val <= min) || (root.val >= max)) {
                    return false;
                }
            }
        }

        // if we get this far, we will need to recurse

        // if no children, return true
        if ((root.left == null) && (root.right == null)) {
            return true;
        }

        // if only left child, recurse left with new max
        if (root.right == null) {
            return isValidSubtree(root.left, min, root.val);
        }

        // if only right child, recurse right with new min
        if (root.left == null) {
            return isValidSubtree(root.right, root.val, max);
        }

        // if both children, recurse left with new max and right with new min
        return (isValidSubtree(root.left, min, root.val) && isValidSubtree(root.right, root.val, max));
    }
}