n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    c = find(a)
    d = find(b)
    if c>d :
        parent[c] = find(d)
    else :
        parent[d] = find(c)

for i in range(1,n+1) :
    l = list(map(int,input().split()))
    for j in range(1,n+1) :
        if l[j-1] == 0 :
            continue
        else :
            union(i,j)

l = list(map(int,input().split()))
ans = []
for x in l :
    if find(x) not in ans :
        ans.append(find(x))
if len(ans) == 1 :
    print("YES")
else :
    print("NO")

