n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    c = find(a)
    d = find(b)
    if c > d :
        parent[c] = find(d)
    else :
        parent[d] = find(c)

for _ in range(m) :
    a,b = map(int,input().split())
    union(a,b)
ans = 0
l = list(map(int, input().split()))
for i in range(len(l)-1) :
    if find(l[i]) != find(l[i+1]) :
        ans += 1
print(ans)