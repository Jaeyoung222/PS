n,m = map(int,input().split())

parent = [i for i in range(n)]

def find(x) :
    while x!= parent[x] :
        x = parent[x]
    return x

def union(a,b) :
    c = find(a)
    d = find(b)
    if c>d :
        parent[c] = d
    else :
        parent[d] = c
l = []
for i in range(m) :
    a,b = map(int,input().split())
    l.append((a,b))
for i in range(m) :
    a,b = l[i]
    
    if find(a)==find(b) :
        print(i+1)
        break
    else :
        union(a,b)
        if i == m-1 :
            print(0)
        else :
            continue
    