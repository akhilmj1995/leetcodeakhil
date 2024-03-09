class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            a.append(nums.count(i))
        return a.count(max(a))

        