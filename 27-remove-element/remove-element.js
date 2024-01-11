/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var s = 0;
    var e = nums.length;
    while (s < e) {
        if (nums[s] == val) {
            nums[s] = nums[e - 1];
            e--;
        } else {
            s++;
        }
    }
    return s;
};