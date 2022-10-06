n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    p = find(a)
    q = find(b)
    if p < q :
        parent[p] = find(q)
    else :
        parent[q] = find(p)

for _ in range(m) :
    d,a,b = map(int,input().split())
    if d == 0 :
        union(a,b)
    elif d == 1 :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")