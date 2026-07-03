t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    l=0
    r=n-1
    for i in range(1,n):
        if i == p[l]:
            l+=1
        elif i == p[r]:
            r-=1
        else:
            print("NO")
            break
    else:
        print("YES")
