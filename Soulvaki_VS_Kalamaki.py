for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(1,n-1,2):
        if a[i]==a[i+1]:
            print("YES")
            break
    else:
        print("NO")
