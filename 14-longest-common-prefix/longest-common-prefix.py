class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      strs.sort()
      prefix=[]
      flag=0
      for i in range(len(strs[0])):
           prefix.append(strs[0][i])
           for j in range(len(strs)):
               if prefix[-1]!=strs[j][i]:
                  prefix.pop()
                  flag=1
                  break
           if flag==1:
              break
      return "".join([str(i) for i in prefix])
            
        
            
            

        