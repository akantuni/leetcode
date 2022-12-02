class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2
        return self.countVowels(s[:mid]) == self.countVowels(s[mid:])
    

    def countVowels(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        total = 0
        for char in s:
            if char.lower() in vowels:
                total += 1

        return total
