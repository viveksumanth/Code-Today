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
    public int findBottomLeftValue(TreeNode root) {
        List<TreeNode> queue = new LinkedList<>();
        int leftMost = 0;
        queue.add(root);
        
        while(!queue.isEmpty()) {
            int qSize = queue.size();
            boolean flag = false;
            for (int i=0; i<qSize; i++) {
                TreeNode currentNode = queue.removeFirst();
                if (flag == false) {
                    leftMost = currentNode.val;
                    flag = true;
                }
                TreeNode leftNode = currentNode.left;
                TreeNode rightNode = currentNode.right;

                if(leftNode != null) {
                    queue.addLast(leftNode);
                } 

                if (rightNode != null) {
                    queue.addLast(rightNode);
                }
            }
        }
        return leftMost;
    }
}