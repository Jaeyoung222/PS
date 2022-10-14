# **0.5로는 시간초과나고 math 라이브러리 써야했음.

import math
import sys
input = sys.stdin.readline

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

        


t = int(input())
for _ in range(t) :
    n = int(input())
    point = [[0,0,0]]
    parent = [i for i in range(n+1)]
    for _ in range(n) :
        point.append(list(map(int,input().split())))
    for a in range(1,n+1) :
        for b in range(a+1,n+1) :
            x1 = point[a][0]
            y1 = point[a][1]
            r1 = point[a][2]
            x2 = point[b][0]
            y2 = point[b][1]
            r2 = point[b][2]
            if math.sqrt((x2-x1)**2 + (y2-y1)**2) <= r1+r2 :
                union(a,b)
    
    ans = set()
    for y in range(1,n+1) :
        ans.add(find(y))
    print(len(ans))
