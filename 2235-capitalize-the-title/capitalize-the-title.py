class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        caps=[ word.lower() if len(word)<3 else word.capitalize() for word in words]
        return " ".join(caps)