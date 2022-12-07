class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0

        mystr = [str(num) for num in nums]
        full = ''.join(mystr)
        formatted = full.split('0')

        for i in formatted:
            if len(i) > mx:
                mx = len(i)
                
        return mx
