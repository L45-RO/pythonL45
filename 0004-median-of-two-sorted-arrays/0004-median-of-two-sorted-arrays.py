class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        super_arr= sorted(nums1 + nums2)
        n = len(super_arr)
        if len(super_arr) % 2 == 0:
            mid1 = super_arr[n//2 - 1]
            mid2 = super_arr[n//2]
            median = (mid1 + mid2) / 2.0
        else:    
            median = super_arr[n // 2]
        return median
        