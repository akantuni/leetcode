class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        memo = []
        for i in range(len(nums)):
            memo.append(sum(nums[: i + 1]))
        return memo
