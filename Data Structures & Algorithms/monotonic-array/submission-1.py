class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        IncFlag = True
        DecFlag = True
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if num < nums[idx-1]:
                IncFlag = False
            if num > nums[idx-1]:
                DecFlag = False
        
        return IncFlag or DecFlag
