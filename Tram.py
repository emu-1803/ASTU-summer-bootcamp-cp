n=int(input())

initial=0
max_p=0
for _ in range(n):
    ai,bi=map(int,input().split())

    initial-=ai
    initial+=bi
    
    max_p=max(max_p,initial)
print(max_p)
