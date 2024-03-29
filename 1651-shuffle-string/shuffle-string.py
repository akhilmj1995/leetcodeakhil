class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=dict()
        x=str()
        for i in indices:
            t[i]=s[indices.index(i)]
        for j in range(len(t)):
            x+=t[j]
        return x
