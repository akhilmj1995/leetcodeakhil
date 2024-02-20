class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2=0,0
        for i in nums1:
            if i in nums2:
                c1+=1         
        for j in nums2:
            if j in nums1:
                c2+=1
        a=[c1,c2]
        return a