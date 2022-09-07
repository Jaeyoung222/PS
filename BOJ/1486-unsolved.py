n,m,t,d = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(input()))

for i in range(n) :
    for j in range(m) :
        if ord(graph[i][j]) <=90 :
            graph[i][j] = ord(graph[i][j])-65
        else :
            graph[i][j] = ord(graph[i][j])-71

