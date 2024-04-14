class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
     k=str()
     for i in range(100):
        if i>=len(word1)and i>=len(word2):
            break
        try:
            if word1[i]:
             k+=word1[i]
        except:
            pass
        try:
            if word2[i]:
                k+=word2[i]
        except:
              continue
     return k 
          
        
        