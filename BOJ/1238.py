import sys
input = sys.stdin.readline
n,m,x = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for i in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

import heapq

total_distance = [0]*(n+1)

for stu in range(n+1) :
    q = []
    distance = [INF]*(n+1)
    heapq.heappush(q,(0,stu))
    distance[stu] = 0
    while q :
        d, now = heapq.heappop(q)
        if distance[now] < d :
            continue
        for nxt,c in graph[now] :
            cost = d + c
            if distance[nxt] > cost :
                distance[nxt] = cost
                heapq.heappush(q,(cost,nxt))

    if stu == x :
        for ii in range(n+1) :
            total_distance[ii] += distance[ii]
    else :
        total_distance[stu] += distance[x]

print(max(total_distance[1:]))
    

