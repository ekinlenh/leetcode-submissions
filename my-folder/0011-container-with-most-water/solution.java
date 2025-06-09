class Solution {
    public int maxArea(int[] heights) {

        int area = 0;
        int left = 0;
        int right = heights.length - 1;

        while (left < right) {
            int currentArea = Math.min(heights[left], heights[right]) * (right - left);
            area = Math.max(area, currentArea);

            if (heights[left] <= heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return area;
    }
}

