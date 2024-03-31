class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for i in range(len(nums)):
            m=[]
            for j in range(len(nums)):
                if nums.count(nums[j])>=i+1 and nums[j] not in m:
                      m.append(nums[j])
            if m:
              a.append(m)
        print(a)
        return a