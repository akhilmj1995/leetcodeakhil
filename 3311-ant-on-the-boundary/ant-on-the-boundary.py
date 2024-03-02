class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        k=0
        for i in nums:
            count+=i
            if count==0:
                k+=1
        return k
