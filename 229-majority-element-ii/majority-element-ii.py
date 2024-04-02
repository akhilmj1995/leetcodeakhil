class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
         a=[]
         for i in nums:
            if i not in a: 
               if nums.count(i)>len(nums)//3:
                    a.append(i)
         return a