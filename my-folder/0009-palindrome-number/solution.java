class Solution {
    public boolean isPalindrome(int x) {
        String number = Integer.toString(x);
        String[] numberArray = number.split("");
        String[] reversedNumberArray = new String[numberArray.length];

        int count = 0;
        for (int i=numberArray.length-1; i>=0;i--) {
            reversedNumberArray[count] = numberArray[i];
            count++;
        }

        int palindromeCheck = 0;
        for (int i=0; i<numberArray.length; i++) {
            if (numberArray[i].equalsIgnoreCase(reversedNumberArray[i])) {
                palindromeCheck++;
            }
        }

        if (palindromeCheck == numberArray.length) {
            return true;
        } else {
            return false;
        }
    }
}
