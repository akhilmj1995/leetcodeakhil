class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        for i in nums:
            for j in nums[nums.index(i):]:
                if abs(i-j)<=i:
                    m=max(m,i^j)
        return m
