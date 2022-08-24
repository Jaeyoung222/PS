n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))


from collections import deque

for i in range(n) :
    for j in range(n) :
        qij = deque()
        if graph[i][j] == 1 :
            graph[j][i] = 1
            qij.append(j)
        while qij :
            visited = [0]*n
            
        
            

for row in range(n) :
    qrow = deque()
    
    for x in graph[row] :
        visited = [0]*n
        if x == 1 :
            y = graph[row].index(x)
            qrow.append(y)
            visited[y] = 1
            while qrow :
                t = qrow.popleft()
                graph[row][t] = 1
                for xx in graph[t] :
                    if xx == 1 and visited[graph[t].index(xx)]==0:
                        qrow.append(graph[t].index(xx))
                        visited[graph[t].index(xx)] = 1

for ii in range(n) :
    print(graph[ii])
