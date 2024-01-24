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
    private int pCount = 0;
    
    private int dfs(TreeNode root, Map<Integer, Integer> nodeValues){
        if (root == null){
            return pCount;
        }
        
        if (nodeValues.containsKey(root.val)) {
            nodeValues.put(root.val, nodeValues.get(root.val)+1);
        } else {
            nodeValues.put(root.val, 1);
        }
        
        if (root.left == null && root.right == null){
            int oddCount = 0;
            
            for(Map.Entry<Integer, Integer> entry: nodeValues.entrySet()){
                int key = entry.getKey();
                int value = entry.getValue();
                if (value%2 != 0) {
                    oddCount += 1;
                }
            }
            
            if (oddCount <= 1) {
                pCount += 1;
            }
        }
        
        dfs(root.left, nodeValues);
        dfs(root.right, nodeValues);
        
        if (nodeValues.containsKey(root.val)) {
            nodeValues.put(root.val, nodeValues.get(root.val)-1);
            if (nodeValues.get(root.val) == 0) {
                nodeValues.remove(root.val);
            }
        } 
        
        return pCount;
    }
    
    public int pseudoPalindromicPaths (TreeNode root) {
        dfs(root, new HashMap<Integer, Integer>());
        return pCount;
    }
}