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
    private int maximumLength = 0;

    private void dfs(TreeNode root, int length, String dirn) {
        if (root == null) {
            return;
        }
        maximumLength = Math.max(maximumLength, length);
        
        if (dirn.equals("right")) {
            dfs(root.left, length+1, "left");
            dfs(root.right, 1, "right");
        } else {
            dfs(root.right, length+1, "right");
            dfs(root.left, 1, "left");
        }
        return;
    }
    public int longestZigZag(TreeNode root) {
        if (root == null) {
            return 0;
        }
        dfs(root.right, 1, "right");
        dfs(root.left, 1, "left");
        return maximumLength;
    }
}