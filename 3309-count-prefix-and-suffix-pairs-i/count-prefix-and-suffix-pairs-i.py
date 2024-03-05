class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
          for j in range(i+1,len(words)):
              a=len(words[i])
              word=words[j]
              if words[i]==word[:a] and words[i]==word[-a:]:
                  count+=1
        return count
