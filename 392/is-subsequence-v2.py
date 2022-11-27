class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pos = 0

        for char in t:
            if pos < len(s) and char == s[pos]:
                pos += 1

        return pos == len(s)
