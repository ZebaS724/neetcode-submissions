class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(nums[i],i) for i in range (len(nums))]
        arr.sort()
        low = 0
        high = len(nums) - 1
        while low < high:
            current_num = arr[low][0] + arr[high][0]
            if current_num < target:
                low += 1
            elif current_num > target:
                high -=1
            else:
                return sorted([arr[low][1], arr[high][1]])
        return [-1,-1]