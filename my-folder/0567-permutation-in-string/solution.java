class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // fixed sliding window --> k = s1.length()
        // we should compare frequency maps to see if the strings are equal 

        // make sure it is even possible for s1 to be a substring
        if (s1.length() > s2.length()) {
            return false;
        }

        int[] s1Freq = new int[26];
        int[] s2Freq = new int[26];

        for (char c: s1.toCharArray()) {
            s1Freq[c - 'a']++;
        }
        
        // compute first window 
        int k = s1.length();
        for (int i = 0; i < k; i++) {
            s2Freq[s2.charAt(i) - 'a']++;
        }
        if (Arrays.equals(s1Freq, s2Freq)) {
            return true;
        }

        // compute the rest
        for (int i = k; i < s2.length(); i++) {
            s2Freq[s2.charAt(i) - 'a']++;
            s2Freq[s2.charAt(i - k) - 'a']--;

            if (Arrays.equals(s1Freq, s2Freq)) {
                return true;
            }
        }

        return false;
    }
}

