/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    var count = 0;
    var curr = 0;
    var last = 0;

    for (c of s) {
        curr = romanValues[c];
        count += curr;
        if (curr > last) {
            count -= 2*last;
        }
        last = curr;
    }

    return count;
};