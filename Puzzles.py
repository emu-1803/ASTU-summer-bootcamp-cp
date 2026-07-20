n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
l=0
r=n-1
z_min=float('inf')
while l<=r and r<m:
    if arr[r]-arr[l]<z_min:
        z_min=arr[r]-arr[l]
    l+=1
    r+=1
print(z_min)
