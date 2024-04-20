import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence=list(sentence)
        sentence.sort
        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
        return True

        