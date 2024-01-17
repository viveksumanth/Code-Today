class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> lookup = new HashMap<>();
        Set<Integer> uniqueValues = new HashSet<>();

        for (int eachNum : arr) {
            lookup.merge(eachNum, 1, Integer::sum);
        }

        return lookup.values().stream()
                .noneMatch(value -> !uniqueValues.add(value));
    }
}