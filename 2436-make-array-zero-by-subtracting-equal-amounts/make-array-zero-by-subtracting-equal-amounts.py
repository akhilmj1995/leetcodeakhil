class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        x=0
        for i in range(0, len(nums)):
          if (nums[i] == 0):
            continue
          else:
              k=nums[i]
              for j in range(i,len(nums)):
                nums[j] = nums[j] - k
              x = x + 1
        return x