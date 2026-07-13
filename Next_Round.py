n, k=map(int,input().split())
a= list(map(int,input().split()))
score=a[k-1]

c=0
for i in a:
    if i>=score and i>0:
        c+=1
print(c)
