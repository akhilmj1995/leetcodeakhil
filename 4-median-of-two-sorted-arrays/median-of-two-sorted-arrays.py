class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        k=float()
        l=len(a)//2
        if len(a)%2==0:
            u=l-1
            k=(a[l]+a[u])/2
            return k
        else:
            return a[l]
            
