import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())

q = []
distance = [INF]*(n+1)

distance[start] = 0
heapq.heappush(q,(0,start))
while q :
    d, now = heapq.heappop(q)
    if distance[now] < d :
        continue
    
    for x,cost in graph[now] :
        if cost+d < distance[x] :
            distance[x] = cost+d
            heapq.heappush(q,(distance[x],x))

print(distance[end])