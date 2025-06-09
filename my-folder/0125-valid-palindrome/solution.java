class Solution {
    public boolean isPalindrome(String s) {
        // we can use a two-pointers approach 
        // if the left and right pointers match, move closer, else return false
        // once pointers meet/cross, str is a palindrome
        // we also need to avoid non-alphanumeric characters for O(1) space complexity
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !alphaNum(s.charAt(left))) {
                left++;
            }

            while (right > left && !alphaNum(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    public boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}

