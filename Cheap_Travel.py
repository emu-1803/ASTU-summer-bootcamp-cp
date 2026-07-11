import math
n,m,a,b=map(int,input().split())
op1=n*a
op2=((n//m)*b)+((n%m)*a)
op3=math.ceil(n/m)*b

ans=min(op1,op2,op3)
print(ans)
