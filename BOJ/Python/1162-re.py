import heapq
inf = float(1e20)
n,m,k = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for road in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dp = [[inf for _ in range(k+1)] for _ in range(n+1)]
dp[1] = [0]*(k+1)
q = []
heapq.heappush(q,(0,1,0))
while q :
    distance, now, pack = heapq.heappop(q)
    if dp[now][pack] < distance :
        continue
    for next_node, cost in graph[now] :
        # 포장함
        if pack < k :
            if distance < dp[next_node][pack+1] :
                dp[next_node][pack+1] = distance
                heapq.heappush(q,(distance,next_node, pack+1))
        # 포장 안함
        if distance+cost < dp[next_node][pack] :
            dp[next_node][pack] = distance+cost
            heapq.heappush(q,(distance+cost,next_node, pack))

print(min(dp[n]))