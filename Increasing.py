for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    visited=set(a)
    if len(visited)==n:
        print("YES")
    else:
        print("NO")
