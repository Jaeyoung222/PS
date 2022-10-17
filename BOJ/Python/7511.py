import sys
input = sys.stdin.readline

def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    c = find(a)
    d = find(b)

    if c>d :
        parent[c] = find(d)
    else :
        parent[d] = find(c)

t = int(input())
for test in range(1,t+1) :
    print("Scenario {}:".format(test))
    n = int(input())
    k = int(input())
    parent = [i for i in range(n+1)]
    for _ in range(k) :
        a,b = map(int,input().split())
        union(a,b)
    m = int(input())
    for _ in range(m) :
        u,v = map(int,input().split())
        if find(u) != find(v) :
            print(0)
        else :
            print(1)
    print()

