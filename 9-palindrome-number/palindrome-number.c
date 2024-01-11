bool isPalindrome(int x) {
    long int rev = 0;
    long int n = x;
    while (n > 0) {
        rev = rev*10 + n%10;
        n = n/10;
    }
    return (rev == x);
}