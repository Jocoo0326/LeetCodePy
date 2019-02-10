#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = r = 0
        ml = 0
        for i, c in enumerate(s):
            if c in s[l:r]:
                l = s[l:r].index(c) + 1 + l
            r = i + 1
            ml = max(r - l, ml)
        return ml
                
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('pwwkew'))
