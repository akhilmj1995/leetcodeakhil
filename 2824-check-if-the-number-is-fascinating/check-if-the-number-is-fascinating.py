class Solution:
    def isFascinating(self, n: int) -> bool:
        num=str(n)+str(2*n)+str(3*n)
        if "0" not in num:
            for i in num:
                if num.count(i)!=1:
                    return False
            return True
        return False