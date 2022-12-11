class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        for i in range(len(s)):
            used = set()
            for j in range(len(s) - i):
                if s[j+i] in used:
                    break
                used.add(s[j+i])
            if len(used) > mx:
                mx = len(used)
        
        return mx
