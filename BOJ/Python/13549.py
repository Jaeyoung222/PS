n,k = map(int,input().split())

graph = [[] for _ in range(100001)]
for i in range(100001) :
    if i>=0 and i+1 <= 100001 and 2*i<200001 :
        graph[i].append((1,i-1))
        graph[i].append((1,i+1))
        graph[i].append((0,2*i))

q = []

import heapq
INF = int(1e9)
distance = [INF]*(100001)

heapq.heappush(q,(0,n))
distance[n] = 0
visited = [0]*(100001)

while q :
    dist,now = heapq.heappop(q)
    if visited[now] == 1 :
        continue
    else :
        visited[now] = 1

    for cost,nxt in graph[now] :
        tot = cost + dist
        visited[now] = 1
        if nxt<100001 and distance[nxt] > tot :
            distance[nxt] = tot
            heapq.heappush(q,(tot,nxt))
            

print(distance[k])