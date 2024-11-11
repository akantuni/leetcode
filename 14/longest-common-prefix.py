class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = map(len, strs)
        minLen = min(lens)

        for i in range(minLen - 1):
            prefixes = {s[: i + 1] for s in strs}
            print(prefixes)
            if len(prefixes) == 0:
                return "aaa"
            if len(prefixes) > 1:
                return strs[0][: i - 1]
            if i == minLen - 1:
                return strs[0][:minLen]
        return ""
