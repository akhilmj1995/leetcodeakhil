class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    a.append(i)
            return a
        else:
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    a.append(i)
            return a
                    