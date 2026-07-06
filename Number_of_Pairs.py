def counter(x):
    start=0
    end=len(arr)-1
    count=0
    while start<end:
        if arr[start]+arr[end]<=x:
            count+=end-start
            start+=1
        else:
            end-=1
    return count


for _ in range(int(input())):
    n,l,r=map(int,input().split())
    arr=sorted(list(map(int,input().split())))
    ans=counter(r)-counter(l-1)
    print(ans)
