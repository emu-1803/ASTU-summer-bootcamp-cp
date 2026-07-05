n, k= map(int, input().split())
h=list(map(int, input().split()))
window=sum(h[:k])
min_window=window
ans=1
for i in range(k, len(h)):
    window+=h[i]-h[i-k]
    if window<min_window:
        min_window=window
        ans=i-k+2
print(ans)
