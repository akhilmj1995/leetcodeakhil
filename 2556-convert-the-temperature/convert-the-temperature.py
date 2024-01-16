class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k=celsius+273.15
        F=celsius*1.80+32.00
        a=[]
        a.append(k)
        a.append(F)
        return a
        