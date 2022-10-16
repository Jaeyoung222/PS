n = int(input())
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

for _ in range(n-2) :
    a,b = map(int,input().split())
    union(a,b)

ans = set()
ans_list = []
for i in range(1,n+1) :
    find(i)
    if parent[i] not in ans :
        ans.add(parent[i])
        ans_list.append(i)

print(*ans_list)


