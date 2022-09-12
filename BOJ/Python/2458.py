n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a][b] = 1


for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
        
            if graph[i][k] != INF and graph[k][j] != INF and graph[i][j] > graph[i][k]+graph[k][j] :
                graph[i][j] = graph[i][k]+graph[k][j]

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] != INF :
            graph[j][i] = graph[i][j]

for i in range(1,n+1) :
    graph[i][i] = 0
c=0
for i in range(1,n+1) :
    if INF not in graph[i][1:] :
        c += 1

print(c)