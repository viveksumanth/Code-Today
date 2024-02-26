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
    private boolean isSame = true;
    private void dfs(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return;
        } 

        if (p == null && q != null) {
            isSame = false;
            return;
        }

        if (p != null && q == null) {
            isSame = false;
            return;
        } 

        if (p.val != q.val) {
            isSame = false;
        }
        dfs(p.left, q.left);
        dfs(p.right, q.right);

        return;
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        dfs(p, q);
        return isSame;
    }
}