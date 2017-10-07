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
        node1 = l1
        node2 = l2
        result = None
        last = None
        j = 0
        while node1 or node2 or j == 1:
            s = 0
            if node1:
                s += node1.val
            if node2:
                s += node2.val
            s += j

            if s > 9:
                j = 1
                s = s - 10
            else:
                j = 0
            temp = ListNode(s)

            if result is None:
                result = last = temp
            else:
                last.next = temp
                last = last.next

            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
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
