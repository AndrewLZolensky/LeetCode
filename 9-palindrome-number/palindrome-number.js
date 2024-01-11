/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var n = x;
    var ans = 0;
    while(n > 0) {
        ans = 10*ans + n % 10;
        n = Math.floor(n/10);
    };
    return (ans == x);
};