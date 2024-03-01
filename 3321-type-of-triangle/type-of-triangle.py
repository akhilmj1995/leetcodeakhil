class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if (nums[0]+nums[1])>nums[2]:
            if len(set(nums))==1:
                return 'equilateral'
            elif len(set(nums))==2:
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'