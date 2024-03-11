class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        b=sum(nums)-sum(set(nums))
        c=sum(range(1,len(nums)+1))-sum(set(nums))
        return [b,c]       
        
                
