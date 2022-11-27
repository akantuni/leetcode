class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, num in enumerate(nums):
            ind = memo.get(num)
            if ind is not None:
                return [ind, i]
            memo.update({target - num: i})
