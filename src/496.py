# -*- coding: utf-8 -*-

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        d = {}
        for x in nums:
            while s and s[-1]<x:
                d[s.pop()] = x
            s.append(x)
        return [d.get(x, -1) for x in findNums ]