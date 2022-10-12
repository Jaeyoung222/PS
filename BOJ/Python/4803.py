def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    c = find(a)
    d = find(b)
    if c > d :
        parent[c] = find(d)
    else :
        parent[d] = find(c)
i = 0
while True :
    i += 1
    n,m = map(int,input().split())
    if n == 0 & m == 0 :
        break
    parent = [i for i in range(n+1)]
    s = set()
    l = []
    for _ in range(m) :
        a,b = map(int,input().split())
        if find(a) == find(b) :
            l.append(a)
            l.append(b)
        union(a,b)
    for j in range(1,n+1) :
        parent[j] = find(parent[j])
    for k in range(1,n+1) :
        s.add(find(k))
    for x in l :
        if parent[x] in s :
            s.remove(parent[x])
    ans = len(s)
    if ans == 0 :
        print("Case {}: No trees.".format(i))
    elif ans == 1 :
        print("Case {}: There is one tree.".format(i))
    else :
        print("Case {}: A forest of {} trees.".format(i,ans))
