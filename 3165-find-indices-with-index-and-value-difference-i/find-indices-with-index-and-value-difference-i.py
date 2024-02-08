class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        k=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
                    k.append(i)
                    k.append(j)
                    return k
        m=[-1,-1]
        return m