class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        m= sqrt(num)
        print(m)
        if m%1==0:
            return True
        return False
        