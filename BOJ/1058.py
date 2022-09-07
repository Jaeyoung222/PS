n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(input()))

v = [[0]*n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            if i == j :
                continue
            if graph[i][j] == 'Y' or (graph[i][k]=="Y" and graph[k][j] == 'Y') :
                v[i][j] = 1

ans = 0
for i in range(n) :
    if ans < sum(v[i]) :
        ans = sum(v[i])
print(ans)