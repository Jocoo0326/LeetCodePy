#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TwoSum(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, item in enumerate(nums):
            if target - item in lookup:
                return [lookup[target - item], i]
            else:
                lookup[item] = i
        return []

if __name__ == "__main__":
    print(TwoSum().twoSum([2, 7, 11, 15, 18], 9))
