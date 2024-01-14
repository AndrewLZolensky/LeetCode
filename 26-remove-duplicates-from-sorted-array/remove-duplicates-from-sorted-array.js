/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let top = 0;
    let bottom = 0;
    let prev = -(nums[0] + 1);

    while (top < nums.length) {
        if (nums[top] != prev) {
            nums[bottom] = nums[top];
            bottom++;
        }
        prev = nums[top];
        top++;
    }
    return bottom;
};