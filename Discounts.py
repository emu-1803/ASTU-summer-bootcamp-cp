for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=sorted([int(x) for x in input().split()],reverse=True)
    discounts=sorted([int(x) for x in input().split()])
   
    idx=0
    sum=0
    for i in discounts:
        if idx+i >n:
            break
        for j in range(idx,idx+i-1):
            sum += arr[j]
        
        idx+=i
    while idx <n:
        sum += arr[idx]
        idx+=1
    print(sum)
