/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int is_balanced = getDepth(root);
        if (is_balanced == -1) {
            return false;
        }
        return true;
    }

    int getDepth(TreeNode* root) {

        // if this node is null, depth is 0
        if (root == nullptr) {
            return 0;
        }

        // check if we already detected imbalance
        int left_depth = getDepth(root->left);
        int right_depth = getDepth(root->right);
        if ((left_depth == -1) || (right_depth == -1)) {
            return -1;
        }

        // check actual depth balance
        int depth_diff = left_depth - right_depth;
        if ((depth_diff > 1) || (depth_diff < -1)) {
            return -1;
        }

        // compute new depth and return it
        int depth = left_depth > right_depth ? left_depth : right_depth;
        depth++;
        return depth;
    }
};