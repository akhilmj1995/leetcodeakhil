class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m=list()
        a='Fizz'
        b='Buzz'
        c=a+b
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                m.append(c)
            elif i%3==0:
                m.append(a)
            elif i%5==0:
                m.append(b)
            else:
                m.append(str(i))
        return m
            
