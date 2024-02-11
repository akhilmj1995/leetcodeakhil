class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0
        for i in accounts:
            sum=0
            for j in range(len(i)):
                sum+=i[j]
            if sum>wealth:
                wealth=sum
        return wealth