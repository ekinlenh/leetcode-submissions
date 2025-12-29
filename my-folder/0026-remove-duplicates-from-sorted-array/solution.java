class Solution {
    public int removeDuplicates(int[] nums) {

        int k = 1;

        int left = 0;
        int right = left + 1;
        while (right < nums.length) {
            if (nums[left] != nums[right]) {
                nums[k] = nums[right];
                k++;
            }

            left++;
            right++;
        }

        return k;
    }
}
