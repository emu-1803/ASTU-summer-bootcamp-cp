t= int(input())
for i in range(t):
    n, k=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    l=0
    r=n-1
    ans=0
    while l<r:
        s=a[l]+a[r]
        if s==k:
            ans += 1
            l+=1
            r-=1
        elif s<k:
            l+=1
        else:
            r-=1
    print(ans)
