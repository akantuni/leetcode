class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = {}

        for num in arr:
            memo[num] = memo.get(num, 0) + 1

        print(memo)

        if len(set(memo.values())) != len(memo.values()):
            return False
        
        return True
