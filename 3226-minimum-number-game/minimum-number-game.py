class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        for i in range(len(nums)):
          if i%2==0:
             arr.append(nums[i+1])
             arr.append(nums[i])
        return arr

