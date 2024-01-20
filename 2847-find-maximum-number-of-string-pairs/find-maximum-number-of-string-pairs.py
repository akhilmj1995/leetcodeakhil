class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            if i==len(words)-1:
                break
            if words[i][::-1] in words[i+1:len(words)]:
                count+=1
        print(count)
        return count
              
            
            
            
            
 
              
        
        