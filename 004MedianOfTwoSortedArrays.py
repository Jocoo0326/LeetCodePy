#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :nums1: List[int]
        :nums2: List[int]
        :returns: float
        """
        i = j = 0
        count = len(nums1) + len(nums2)
        center = (count + 1) / 2 if count % 2 == 1 else (count / 2 + 1)
        temp = []
        while (i + j) < center:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    temp.append(nums1[i])
                    i += 1
                else:
                    temp.append(nums2[j])
                    j += 1
            elif i > len(nums1) - 1:
                temp.append(nums2[j])
                j += 1
            else:
                temp.append(nums1[i])
                i += 1
        print(temp)
        if count % 2 == 0:
            return sum(temp[-2:]) / 2
        else:
            return temp[-1]

if __name__ == '__main__':
    l1 = [1, 2]
    l2 = [3, 4]
    print(Solution().findMedianSortedArrays(l1, l2))
