for _ in range(int(input())):
    r=list(input())
    cost=0
    if r[0] == "u":
        r[0]="s"
        cost+=1
    if r[-1] == "u":
        r[-1]="s"
        cost+=1
 
    size_u=0
    for i in r:
        if i == "u":
            size_u +=1
        else:
            cost+=size_u//2
            size_u=0
    if size_u >0:
        cost+=size_u
    print(cost)
