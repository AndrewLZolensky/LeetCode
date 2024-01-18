class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # take the list, split in half
        # three cases: 1) drop happens at split, 2) left of split, 3) right of split
        # if 1, the rightmost of left is bigger than leftmost of right
        # if 2, rightmost smaller than leftmost for left list, opposite for right
        # if 3, rightmost smaller than leftmost for right list, opposite for left

        # Base cases:
        # 1) if list has 1 number, return it
        # 2) if list only has 2 numbers, return rightmost
        # if list has 3 numbers, return min (2nd - 1st), (3rd - 2nd)
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return min(nums[0], nums[1])
        elif n == 3:
            return min(nums[0], nums[1], nums[2])
        else:
            if nums[0] < nums[-1]:
                return nums[0]
            half = n // 2
            left = nums[:half]
            right = nums[half:]
            if left[half - 1] > right[0]:
                return right[0]
            elif left[0] > left[half - 1]:
                return self.findMin(left)
            else:
                return self.findMin(right)
        