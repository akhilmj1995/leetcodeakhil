class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        triple=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    triple.append((nums[i]-nums[j])*nums[k])
        a=max(triple)
        if a<0:
            return 0
        else:
            return a
               
        