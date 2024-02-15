class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        max=0
        for i in nums:
            for j in nums[nums.index(i):]:
                if abs(i-j)<=i:
                    if (i^j)>max:
                       max=i^j
        return max
