for _ in range(int(input())):
    n,k = map(int,input().split())
    a= list(map(int,input().split()))
    a1=set(a)
    for i in a:
        if i-k in a1:
            print("YES")
            break
    else:
        print("NO")
