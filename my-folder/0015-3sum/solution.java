class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Time-Complexity: O(n^2)
        // Space-Complexity: O(1) or O(n) extra space for sorting, O(m) space for output list
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (nums[i] > 0) {
                break;
            } 

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;
        
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];

                // check for result = 0, > 0, and < 0
                if (total == 0) {
                    list.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }

                } else if (total < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return list;
    }

}

