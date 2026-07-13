for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    cur_max=max(a)
    for _ in range(m):
        c,l,r= input().split()
        l=int(l)
        r=int(r)
        
        if l<= cur_max <=r:
            if c=="+":
                cur_max+=1
            else:
                cur_max-=1
        print(cur_max, end=" ")

    print()
