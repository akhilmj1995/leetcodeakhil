class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum=0
        for i in range(len(nums)):
            ans=bin(i).replace('0b','')
            if ans.count('1')==k:
              sum+=nums[i]
        return sum