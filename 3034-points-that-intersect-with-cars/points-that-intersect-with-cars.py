class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
           cord=[]
           for i in range(len(nums)):
               for j in range(nums[i][0],nums[i][1]+1):
                   cord.append(j)    
           return len(set(cord))
           
        