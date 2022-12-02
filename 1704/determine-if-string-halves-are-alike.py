class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return self.countVowels(s[:(len(s)//2)]) == self.countVowels(s[(len(s)//2):])
    

    def countVowels(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        total = 0
        for char in s:
            if char.lower() in vowels:
                total += 1

        return total
