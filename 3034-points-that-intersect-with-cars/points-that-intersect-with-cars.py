class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
           cord=[]
           for i in range(len(nums)):
               k=nums[i][0]-nums[i][1]
               a=nums[i][0]
               while a<=nums[i][1]:
                   cord.append(a)
                   a+=1
           return len(set(cord))
           
        