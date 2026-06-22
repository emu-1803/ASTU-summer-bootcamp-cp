n, t = map(int, input().split())
a=list(map(int, input().split()))
l=0
ct=0
max_books =0
for i in range(n):
    ct+=a[i]
    while ct>t:
        ct-=a[l]
        l+=1
    max_books=max(max_books, i-l+1)
print(max_books)
