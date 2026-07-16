for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    visited=set()
    ans=0

    for i in range(n-1,-1,-1):
        if a[i] in visited:
            ans=i+1
            break
        else:
            visited.add(a[i])

    print(ans)
