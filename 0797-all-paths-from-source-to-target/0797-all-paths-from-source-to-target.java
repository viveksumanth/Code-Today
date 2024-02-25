class Solution {
    List<List<Integer>> paths;

    public void dfs(int[][] graph, List<Integer> currentPath, int src, int dest) {
        if (currentPath.size() > 0 && currentPath.get(currentPath.size()-1) == dest) {
            paths.add(new ArrayList<Integer>(currentPath));
            return;
        }
        for (int i = 0; i < graph[src].length; i++) {
            currentPath.add(graph[src][i]);
            dfs(graph, currentPath, graph[src][i], dest);
            currentPath.remove(currentPath.size()-1);
        }
        return;
    }

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int src = 0;
        int target = graph.length-1;
        paths = new ArrayList<>();
        var currentPath = new ArrayList<Integer>();
        currentPath.add(src);
        dfs(graph, currentPath, src, target);
        return paths;
    }
}