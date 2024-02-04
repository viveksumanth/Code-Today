/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {

        Map<Integer, Set<Integer>> lookup = new HashMap<>();
        for (int i = 0; i < n; i++) {
            var currentList = new HashSet<Integer>();
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (knows(i,j) == true) {
                        currentList.add(j);
                    }
                }
            }

            if (!lookup.containsKey(i)) {
                lookup.put(i, currentList);
            } else {
                var temp = lookup.get(i);
                temp.addAll(currentList);
                lookup.put(i, temp);
            }
        }

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (Map.Entry<Integer,Set<Integer>> entry: lookup.entrySet()) {
                if (entry.getValue().contains(i)) {
                    count += 1;
                }

                if (count == n-1 && lookup.get(i).size() == 0) {
                    return i;
                }
            }
        }

        return -1;
    }
}