class RandomizedSet {
    Map<Integer, Integer> lookup;
    List<Integer> lookupKeys;
    Random rand = new Random();
    
    public RandomizedSet() {
        lookup = new HashMap<>();
        lookupKeys = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        // System.out.println("insert");
        // System.out.println(lookup);
        if(lookup.containsKey(val)){
            return false;
        } else {
            lookupKeys.add(val);
            lookup.put(val, lookupKeys.size()-1);
        }
        return true;
    }
    
    public void swapAndUpdate(int index) {
        int lastElement = lookupKeys.get(lookupKeys.size()-1);
        lookupKeys.set(index, lastElement);
        lookup.put(lastElement, index);
        lookupKeys.remove(lookupKeys.size()-1);
            
    }
    
    public boolean remove(int val) {
        // System.out.println("remove");
        // System.out.println(lookup);
        if (lookup.containsKey(val)) {
            int index = lookup.get(val);
            swapAndUpdate(index);
            lookup.remove(val);
            return true;
            } 
        return false;
    }
    
    public int getRandom() {
        return lookupKeys.get(rand.nextInt(lookupKeys.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */