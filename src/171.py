class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return reduce(lambda x, y:x * 26 + y, map(lambda c:ord(c) - ord('A') + 1, s), 0)