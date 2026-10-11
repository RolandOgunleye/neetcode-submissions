class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            find = target- nums[i]
            if find in map:
                return [map[find],i]
            map[n] = i
        return 
