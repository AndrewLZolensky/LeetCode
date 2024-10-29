class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        w = m + n - 1
        r1 = m - 1
        r2 = n - 1
        while (w >= 0):
            if (r1 < 0):
                nums1[w] = nums2[r2]
                r2 -= 1
            elif (r2 < 0):
                nums1[w] = nums1[r1]
                r1 -= 1
            else:
                if (nums1[r1] >= nums2[r2]):
                    nums1[w] = nums1[r1]
                    r1 -= 1
                else:
                    nums1[w] = nums2[r2]
                    r2 -= 1
            w -= 1
        return nums1