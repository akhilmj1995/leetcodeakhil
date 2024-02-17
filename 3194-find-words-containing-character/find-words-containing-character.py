class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        m=[]
        for i in range(len(words)):
            if x in words[i]:
                m.append(i)
        return m