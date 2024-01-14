/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0;
    let cand = 0;
    for (let i = 0; i < nums.length; i++) {
        cand = (count == 0) ? nums[i] : cand;
        count = (nums[i] == cand) ? count+1 : count-1;
    }
    return cand;
};