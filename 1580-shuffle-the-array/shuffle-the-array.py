class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        n=int(len(nums)/2)
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a

        


        
