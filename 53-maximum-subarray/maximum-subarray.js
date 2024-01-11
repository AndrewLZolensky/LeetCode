/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var max = nums[0];
    var curr = 0;
    for (let i = 0; i < nums.length; i++) {
        curr = curr > 0 ? curr + nums[i] : nums[i];
        max = curr > max ? curr : max;
    }
    return max;
};