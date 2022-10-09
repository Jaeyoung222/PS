from collections import deque
n,m = map(int,input().split())

graph = [[0]*(n+1) for i in range(n+1)]

for _ in range(m) :
    a,b,c = map(int,input().split())
    if graph[a][b] == 0 :
        graph[a][b] = c
        graph[b][a] = c
    else :
        graph[a][b] = max(graph[a][b],c)
        graph[b][a] = max(graph[b][a],c)

a,b = map(int,input().split())
q = deque()
answer = []
for i in range(1,n+1) :
    if graph[a][i] !=0 :
        q.append((a,i,graph[a][i]))

while q :
    start, des, weight = q.popleft()
    if graph[start][des] == -1 :
        continue
    if des == b :
        answer.append(weight)
    else :
        for i in range(1,n+1) :
            if graph[des][i] != 0 :
                q.append((des,i,min(graph[des][i],weight)))
    graph[start][des] = -1
print(max(answer))