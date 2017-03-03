# -*- coding: utf-8 -*-

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        return [word for word in words if any([set(word.lower()) <= row for row in [set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')]])]