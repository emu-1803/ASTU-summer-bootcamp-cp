import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a[0]+=1
    for i in range(n):
        res=math.prod(a)
    print(res)
