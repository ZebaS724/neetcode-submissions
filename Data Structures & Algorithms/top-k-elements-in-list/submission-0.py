class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            res[nums[i]] = 1 + res.get(nums[i],0)

        sorted_res = sorted(res.items(), key = lambda x:x[1], reverse = True)

        return [x[0] for x in sorted_res[:k]]

        
        