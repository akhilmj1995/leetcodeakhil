class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max=0
        for i in nums:
            for j in nums[nums.index(i):]:
                if abs(i-j)<=min(i,j):
                    if (i^j)>max:
                       max=i^j
        return max
