class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        new_nums = sorted(nums)
        for i in range(n-1):
            if new_nums[i+1] == new_nums[i]:
                return True
        return False
        