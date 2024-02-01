class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a=[]
        for i in range(len(nums)):
            ans=bin(i).replace('0b','')
            if ans.count('1')==k:
                a.append(i)
        sum=0
        for i in a:
            sum+=nums[i]
        return sum