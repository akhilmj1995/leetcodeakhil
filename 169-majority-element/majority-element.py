class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        b=len(nums)/2
        if len(nums)==1:
            return nums[0]
        elif b%2==0:
            return nums[int(b-1)]
        else:
            return nums[int(b-0.5)]
           
        
        
           
                 
           
           
              