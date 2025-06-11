class Solution {
    public int findDuplicate(int[] nums) {
        // Linked List Cycle and Floyd's Algorithm

        // first find intersection where slow and fast pointer meet
        int slow = 0;
        int fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        // initialize another slow pointer, and when both slow pointers meet
        // is the duplicate number in the array
        int slow2 = 0;
        while (true) {
            slow = nums[slow];
            slow2 = nums[slow2];
            if (slow == slow2) {
                return slow;
            }
        }

    }
}

