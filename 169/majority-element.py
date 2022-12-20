class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
        for num in memo.keys():
             if memo[num] > len(nums) /2:
                   return num
