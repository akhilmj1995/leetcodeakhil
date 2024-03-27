class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                a.append(nums[i])
            if nums[i]==pivot:
                c.append(nums[i])
            if nums[i]>pivot:
                b.append(nums[i])

        return a+c+b
        
            
            
