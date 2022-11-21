class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
//         find all paris that add up to zero
        /*
          
        [-1,0,1,2,-1.-4]
        
        sort
          |
        [-4,-1,-1,0,1,2]
            |
        
        */
        // List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> result = new HashSet<List<Integer>>();
        Arrays.sort(nums);
        
        for(int i = 0; i< nums.length; i++){
            
            int req = nums[i];
            int l = i+1;
            int r = nums.length-1;
            // System.out.println(r);
            while(l < r){
                
                if(nums[l] + nums[r] + req == 0){
                   result.add(Arrays.asList(nums[l],nums[r],req));
                   r = r - 1;
                }else if (nums[l] + nums[r] + req < 0)
                    l += 1;
                else
                    r -= 1;
                
            }
        }

        List<List<Integer>> resultList =  new ArrayList<List<Integer>>(result);
        return resultList;
    }
}