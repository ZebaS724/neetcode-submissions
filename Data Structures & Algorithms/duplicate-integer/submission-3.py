class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = list(dict.fromkeys(nums))
        a = len(nums)
        b = len(new_list)
        if a == b:
            return False
        else:
            return True
        