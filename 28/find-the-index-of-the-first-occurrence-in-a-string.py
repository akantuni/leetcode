class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sp = haystack.split(needle)
        if len(sp) == 1:
            return -1
        return len(sp[0])
