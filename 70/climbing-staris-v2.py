class Solution:
    def climbStairs(self, n: int) -> int:
        return int(round(((((1 + 5 ** 0.5) / 2) ** (n + 1)) - (((1 - 5 ** 0.5) / 2) ** (n + 1))) / 5 ** 0.5))
