class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        most = 1
        count = 1
        n = len(nums)

        for i in range(1,n):
            
            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] + 1:
                count += 1
                
            else:
                count = 1
            
            most = max(most,count)
            
        return most
            
        