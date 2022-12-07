class Solution:
    def reverse(self, x: int) -> int:
        temp = int(str(abs(x))[::-1])
        if x < 0:
            temp *= -1

        if temp > 2147483647 or temp < -2147483648:
            return 0
        return temp
