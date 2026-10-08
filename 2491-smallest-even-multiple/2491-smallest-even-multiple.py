class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        n=int(n)
        if n%2==0:
            return(n)
        else:
            return(n*2)