class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        valid = True

        for base in range(2, n - 1):
            newNum = self.convertToBase(n, base)
            if not newNum == newNum[::-1]:
                valid = False
                break
        return valid

    def convertToBase(self, n, base):
        if n == 0:
            return "0"
        newNum = ""
        while n:
            newNum += str(int(n % base))
            n //= base
        return newNum[::-1]
