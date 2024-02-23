class Solution:
    def defangIPaddr(self, address: str) -> str:
        k=address.count('.')
        address=address.replace('.','[.]',k)
        return address