#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is not None:
            return "%s -> %s" % (self.val, self.next)
        else:
            return "%s" % self.val

class Solution(object):
    """docstring for Solution"""
    def addTwoNums(self, l1, l2):
        carry = 0
        result = last = None
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            temp = ListNode(carry % 10)
            if result:
                last.next = temp
                last = last.next
            else:
                result = last = temp
            carry = 1 if carry > 9 else 0
        return result

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    print(l1)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(l2)
    print(Solution().addTwoNums(l1, l2))
