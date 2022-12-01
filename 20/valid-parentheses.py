class Solution:
    def isValid(self, s: str) -> bool:
        memo = {"]": "[", "}": "{", ")": "("}

        if len(s) % 2 != 0:
            return False

        opn = []
        for char in s:
            if memo.get(char) is not None:
                if len(opn) == 0:
                    return False
                if opn[-1] != memo.get(char):
                    return False
                opn.pop(-1)
            else:
                opn.append(char)
        
        return len(opn) == 0
