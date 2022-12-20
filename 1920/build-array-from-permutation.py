class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        memo = []
        for i in range(len(nums)):
            print(i)
            memo.append(nums[nums[i]])
        return memo
