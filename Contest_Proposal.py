for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    p1, p2=0, 0
    counter=0
    while p2< len(b) and p1<=p2:
        if a[p1]>b[p2]:
            p2+=1
            counter+=1
        else:
            p1+=1
            p2+=1
    print(counter)
