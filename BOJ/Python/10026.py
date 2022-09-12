from collections import deque

n = int(input())
graph = []
visited1  = []
visited2 = []
for _ in range(n) :
    graph.append(list(input()))
    visited1.append([0]*n)
    visited2.append([0]*n)

q = deque()
c1 = 0
c2 = 0
for i in range(n) :
    for j in range(n) :
        if visited1[i][j] == 1 :
            continue
        else :
            q.append((i,j))
            visited1[i][j] = 1
            t = graph[i][j]
            while q :
                a,b = q.popleft()
                for x,y in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)] :
                    if x>=0 and x<n and y>=0 and y<n :
                        if visited1[x][y]==0 and graph[x][y] == t :
                            q.append((x,y))
                            visited1[x][y] = 1
            c1 += 1
               
q = deque()
for i in range(n) :
    for j in range(n) :
        if visited2[i][j] == 1 :
            continue
        else :
            q.append((i,j))
            visited2[i][j] = 1
            t = graph[i][j]
            while q :
                a,b = q.popleft()
                for z,w in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)] :
                    if z>=0 and z<n and w>=0 and w<n :
                        if visited2[z][w]==0 and (t=='R' or t=='G') and (graph[z][w]=='R' or graph[z][w]=='G'):
                            q.append((z,w))
                            visited2[z][w] = 1
                        elif visited2[z][w]==0 and graph[z][w] == t and (t=='B') :
                            q.append((z,w))
                            visited2[z][w] = 1
            c2 += 1
print(c1,c2)
            

