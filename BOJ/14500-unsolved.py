import copy
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []
visited = []
visited_origin = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))
    visited.append([0]*m)
for __ in range(n) :
    visited_origin.append([0]*m)

def findmax(x,y,graph,visited,n,m) :
    a=0
    b=0
    sss = 0
    for z,w in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] :
        if z>=0 and z<n and w>=0 and w<m :
            if visited[z][w] == 0 and sss<graph[z][w] :
                visited[z][w] = 1
                sss = graph[z][w]
                a=z
                b=w
    return a,b,sss

max = 0

for i in range(n) :
    for j in range(m) :
        c = 1
        s = graph[i][j]
        visited[i][j] = 1
        ii = i
        jj = j

        while c<=3 :
            xx,yy,ss = findmax(ii,jj,graph,visited,n,m)
            s += ss
            c += 1
            ii = xx
            jj = yy

        if s > max :
            max = s

        visited = copy.deepcopy(visited_origin)

        if i>=1 and i<=n-2 :
            if j>=0 and j<=n-2 : 
                if max < graph[i][j]+graph[i-1][j]+graph[i+1][j]+graph[i][j+1] :
                    max = graph[i][j]+graph[i-1][j]+graph[i+1][j]+graph[i][j+1]
            if j>=1 and j<=n-1 :
                if max < graph[i][j]+graph[i-1][j]+graph[i+1][j]+graph[i][j-1] :
                    max = graph[i][j]+graph[i-1][j]+graph[i+1][j]+graph[i][j-1]
        if j>=1 and j<=n-2 :
            if i>=0 and i<=n-2 :
                if max < graph[i][j]+graph[i][j-1]+graph[i][j+1]+graph[i+1][j] :
                        max = graph[i][j]+graph[i][j-1]+graph[i][j+1]+graph[i+1][j]
            if i>=1 and i<n-1 :
                if max < graph[i][j]+graph[i][j-1]+graph[i][j+1]+graph[i-1][j] :
                        max = graph[i][j]+graph[i][j-1]+graph[i][j+1]+graph[i-1][j]

print(max)