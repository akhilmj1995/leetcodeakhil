class Solution:
    def isFascinating(self, n: int) -> bool:
        second=2*n
        third=3*n
        num=str(n)+str(second)+str(third)
        if "0" not in num:
            for i in num:
                if num.count(i)!=1:
                    return False
            return True
        return False