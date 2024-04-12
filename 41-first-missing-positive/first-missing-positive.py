class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        k=[i for i in range(1,len(nums)+2)]
        m=[i for i in nums if i>0]
        for i in range(0,len(nums)):
            try:
               if k[i]!=m[i]:
                   return k[i]
            except:
                if i==0:
                    return 1
                else:
                    return m[len(m)-1]+1
        return m[len(m)-1]+1
        
        
        
        