class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        # 1: 1
        # 2: 2
        # 3: 3
        # 4: 5
        # 5: 8
        # 6: 13
        # 7: 21
        # 8: 34
        # 9: 55
        # 10: 89

        if n <= 1:
            return 1
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
