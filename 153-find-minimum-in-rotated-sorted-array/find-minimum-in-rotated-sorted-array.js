/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let start = 0;
    let end = nums.length - 1;
    let middle;
    while (start < end) {
        middle = Math.floor((start + end) / 2);
        if (nums[middle] < nums[end]) {
            end = middle;
        } else {
            start = middle + 1;
        }
    }
    return nums[start];
};