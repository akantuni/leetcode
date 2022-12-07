class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        amount = 0

        for i in nums:
            ln = len(str(i))
            if ln % 2 == 0:
                amount += 1

        return amount
