class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        lis=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        a,b=0,0
        for j in range(0,len(nums)):
            if j%2==0:
              lis.append(pos[a])
              a+=1
            else:
                lis.append(neg[b])
                b+=1
        return lis

