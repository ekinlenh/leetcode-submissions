class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] count = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) {
            count[i] = new ArrayList<>();
        }   
        
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int num: nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        for (int key: freqMap.keySet()) {
            count[freqMap.get(key)].add(key);
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = count.length - 1; i >= 0 && index < k; i--) {
            for (int num: count[i]) {
                res[index++] = num;
                if (index == k) {
                    return res;
                }
            }
        }

        return res; 
    }
}

