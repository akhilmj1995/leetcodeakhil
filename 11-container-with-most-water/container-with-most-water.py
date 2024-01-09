class Solution:
    def maxArea(self, height: List[int]) -> int:
        x=[]
        area=0
        l=0
        r=len(height)-1
        while l<r:
            area=(r-l)*min(height[r],height[l])
            x.append(area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max(x)   


                   


