class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum=[] 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                 a=[int(k) for k in str(nums[i])]
                 b=[int(m) for m in str(nums[j])]
                 if max(a)==max(b):
                     sum.append(nums[i]+nums[j])
        if sum:
            return max(sum)
        else:
            return -1

                 
                
                 
                     
       
