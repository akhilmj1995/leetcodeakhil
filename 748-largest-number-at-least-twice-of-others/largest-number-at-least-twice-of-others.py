class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        new_array=nums.copy()
        new_array.sort()
        print(nums)
        print(new_array)
        if new_array[-1]>=2*new_array[-2]:
            return nums.index(new_array[-1])
        return -1
