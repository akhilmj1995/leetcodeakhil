class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        stack = []
        k = []
        total_visited_integers = 0
        consecutive_prevs = 0
        for word in words:
            if word != "prev":
                consecutive_prevs = 0
                total_visited_integers += 1
                stack.append(int(word))
            else:
                consecutive_prevs += 1
                if consecutive_prevs > total_visited_integers:
                    k.append(-1)
                else:
                    k.append(stack[-consecutive_prevs])
                    
        return k

