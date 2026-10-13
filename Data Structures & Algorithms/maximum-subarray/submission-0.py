class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        res = nums[0]
        
        for num in nums:
            cursum += num
            res = max(res,cursum)
            if cursum < 0:
                cursum = 0
            
            
        return res
        