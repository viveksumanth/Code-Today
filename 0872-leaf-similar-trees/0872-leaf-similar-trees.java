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
    
    public void dfs(TreeNode root, int listNum){
        if (root == null) {
            return;
        }
        
        if (root.left == null && root.right == null) {
            if(listNum == 1) {
                root1List.add(root.val);
            } else if (listNum == 2) {
                root2List.add(root.val);
            }
        }
        
        dfs(root.left, listNum);
        dfs(root.right, listNum);
        return;
    }
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        
        dfs(root1, 1);
        dfs(root2, 2);
        
        if(root1List.size() != root2List.size()) {
            return false;
        }
        
        for(int i = 0; i<root1List.size(); i++) {
            if (root1List.get(i) != root2List.get(i)) {
                return false;
            }
        }
        return true;
    }
}