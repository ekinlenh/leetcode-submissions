class Solution {
    public int characterReplacement(String s, int k) {

        int left = 0;
        int maxFreq = 0;
        HashMap<Character, Integer> count = new HashMap<>();
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            count.put(s.charAt(right), count.getOrDefault(s.charAt(right), 0) + 1);
            maxFreq = Math.max(maxFreq, count.get(s.charAt(right)));
            
            while ((right - left + 1) - maxFreq > k) {
                count.put(s.charAt(left), count.get(s.charAt(left)) - 1);
                left++;
            }

            maxLength = Math.max(right - left + 1, maxLength);
        }

        return maxLength; 
    }
}

