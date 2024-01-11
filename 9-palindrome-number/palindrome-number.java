class Solution {
    public boolean isPalindrome(int x) {
        int n = x;
        int rev = 0;
        while (n > 0) {
            rev = rev*10 + (n%10);
            n = n/10;
        }
        return x==rev;
    }
}