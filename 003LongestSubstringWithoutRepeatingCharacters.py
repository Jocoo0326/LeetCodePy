#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :s: str
        :returns: int
        """
        temp = []
        length = 0
        for i, c in enumerate(s):
            if c in temp:
                length = max(len(temp), length)
                temp = temp[temp.index(c)+1:]
            temp.append(c)
        return max(len(temp), length)

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('asdfasdzzqwefzdfsd'))
