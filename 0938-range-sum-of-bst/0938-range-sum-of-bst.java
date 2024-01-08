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
    private int totalSum = 0;

    public int rangeSumBSTHelper(TreeNode root, int low, int high){
        
        if(root == null){
            return 0;
        }

        if(root.val >= low && root.val <= high){
            totalSum += root.val;
        }
        rangeSumBSTHelper(root.left,low,high);
        rangeSumBSTHelper(root.right,low,high);

        return 0;
    }
    
    public int rangeSumBST(TreeNode root, int low, int high) {
        
        rangeSumBSTHelper(root,low,high);
        return totalSum;

    }
}