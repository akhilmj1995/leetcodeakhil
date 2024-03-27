class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        m=nums.count(pivot)
        for i in range(len(nums)):
            if nums[i]<pivot:
                a.append(nums[i])
            if nums[i]>pivot:
                b.append(nums[i])
        for i in range(m):
            a.append(pivot)
        return a+b
        
            
            
