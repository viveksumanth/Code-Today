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
    private List<Integer> root1List = new ArrayList<>();
    private List<Integer> root2List = new ArrayList<>();
    
    public void dfs(TreeNode root, List<Integer> listNum){
        if (root == null) {
            return;
        }
        
        if (root.left == null && root.right == null) {
            listNum.add(root.val);
        }
        
        dfs(root.left, listNum);
        dfs(root.right, listNum);
        return;
    }
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        
        dfs(root1, root1List);
        dfs(root2, root2List);
        return root1List.equals(root2List);
    }
}