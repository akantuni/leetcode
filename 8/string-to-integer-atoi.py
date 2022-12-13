class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        accepted = {"+", "-"}
        sign = ""
        bound = 0

        if not s[0].isdigit():
            if s[0] not in accepted:
                return 0
            sign = s[0]
            bound += 1

        for char in s[bound:]:
            if not char.isdigit():
                break
            bound += 1
        if len(s[:bound]) == 1 and not s[0].isdigit():
            return 0

        num = int(float(s[:bound]))
        MAX_INT = 2 ** 31 - 1
        MIN_INT = (-2) ** 31

        return MAX_INT if num > MAX_INT else MIN_INT if num < MIN_INT else num
