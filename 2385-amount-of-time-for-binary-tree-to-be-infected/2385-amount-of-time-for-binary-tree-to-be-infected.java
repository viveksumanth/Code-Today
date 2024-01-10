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
    private Map<Integer, List<Integer>> graph = new HashMap<>();
    private int time = 0;
    
    public void insertIntoGraph(int rootValue, int nodeValue) {
        List<Integer> temp = null;
        if(graph.containsKey(rootValue)) {
            temp = graph.get(rootValue);
        } else {
            temp = new ArrayList<>();
        }
        temp.add(nodeValue);
        graph.put(rootValue, temp);
    }
    
    public int dfs(TreeNode root) {
        if (root == null) {
            return -1;
        }
        
        int leftVal = dfs(root.left);
        int rightVal = dfs(root.right);
        
        if(leftVal != -1) {
            int rootValue = root.val;
            insertIntoGraph(rootValue, leftVal);
            insertIntoGraph(leftVal, rootValue);
        }
        
        if(rightVal != -1) {
            int rootValue = root.val;
            insertIntoGraph(rootValue, rightVal);
            insertIntoGraph(rightVal, rootValue);
        }
        
        return root.val;
    }
    
    
    public void bfs(int start) {
        List<Integer> queue = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        
        visited.add(start);
        queue.add(start);
    
        while(queue.size() != 0) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                int currentNode = queue.remove(0);
                
                List<Integer> tempList = graph.get(currentNode);
                
                if(tempList != null) {
                    for (int newNode : tempList) {
                        if(!visited.contains(newNode)) {
                            visited.add(currentNode);
                            queue.add(newNode);
                        }
                    }
                }
            }
            time++;
            // System.out.println("Here");
            // System.out.println(time);
        } 
    }
    
    public int amountOfTime(TreeNode root, int start) {
        dfs(root);
        bfs(start);
        return time-1;
    }
}