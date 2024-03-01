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
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        int step = 0;
        boolean increasingCheck = false;
        int prevNumber = 0;

        while(!queue.isEmpty()) {
            
            if (step % 2 == 0) {
                // check from left to right -> increasing 
                increasingCheck = true;
                prevNumber = Integer.MIN_VALUE;
            } else {
                increasingCheck = false;
                prevNumber = Integer.MAX_VALUE;
            }

            int stepSize = queue.size();

            for (int i = 0; i<stepSize; i++) {
                TreeNode currentNode = queue.poll();
                if (increasingCheck == true) {
                    if (currentNode.val > prevNumber && currentNode.val%2 != 0) {
                        prevNumber = currentNode.val;
                    } else {
                        return false;
                    }
                } else {
                     if (currentNode.val < prevNumber && currentNode.val%2 == 0) {
                        prevNumber = currentNode.val;
                    } else {
                        return false;
                    }
                }

                if (currentNode.left != null) {
                    queue.add(currentNode.left);
                } 
                
                if (currentNode.right != null){
                    queue.add(currentNode.right);
                }
            }
            step++;
        }

        return true;
    }
}