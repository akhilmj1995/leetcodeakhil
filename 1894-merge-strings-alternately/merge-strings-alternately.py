class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
     k=str()
     if len(word1)>len(word2):
        minlen=len(word2)
        remain=word1[minlen:]
     else:
        minlen=len(word1)
        remain=word2[minlen:]
     for i in range(minlen):
        k+=word1[i]
        k+=word2[i]
     k+=remain
     return k
           
          
        
        