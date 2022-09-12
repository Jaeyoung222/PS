n = int(input())
graph = []
ans = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))
    ans.append([0]*n)

from collections import deque            

for row in range(n) :
    qrow = deque()
    visited = [0]*n
    for i in range(n) :
        if graph[row][i]== 1 :
            qrow.append(i)
            visited[i] = 1
            ans[row][i] = 1
    while qrow :
        t = qrow.popleft()
        for ii in range(n) :
            if graph[t][ii] == 1 and visited[ii]==0:
                qrow.append(ii)
                visited[ii] = 1
                ans[row][ii] = 1

for iii in range(n) :
    print(*ans[iii])
