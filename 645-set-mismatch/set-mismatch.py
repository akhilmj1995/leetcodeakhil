class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==2:
                if nums[i] not in a:
                     a.append(nums[i])
                     break
        for i in range(len(nums)):
            if i+1 not in nums:
                a.append(i+1)
                break
        return a
            
                
        
                
