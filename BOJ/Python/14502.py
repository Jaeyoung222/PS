from collections import deque

def spread(graph) :
    visited = [[0]*len(graph[0]) for _ in range(len(graph))]
    q = deque()
    for i in range(len(graph[0])) :
        for j in range(len(graph)) :
            if graph[j][i] == 1 :
                visited[j][i] = 1
            elif graph[j][i] == 2 :
                q.append((j,i))
                visited[j][i] = 1
    while q :
        b,a = q.popleft()
        for y,x in [(b-1,a),(b+1,a),(b,a-1),(b,a+1)] :
            if x >= 0 and y >= 0 and x <len(graph[0]) and y <len(graph) :
                if visited[y][x] == 0 :
                    visited[y][x] = 1
                    graph[y][x] = 2
                    q.append((y,x))
    return

def check_zero(graph) :
    c = 0
    for i in range(len(graph[0])) :
        for j in range(len(graph)) :
            if graph[j][i] == 0 :
                c += 1
    return c

n,m = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

zero_list = []
for i in range(len(graph[0])) :
    for j in range(len(graph)) :
        if graph[j][i] == 0 :
            zero_list.append((j,i))

import itertools
import copy
combination = itertools.combinations(zero_list, 3)

ans = 0
for combi in combination :
    test_graph = copy.deepcopy(graph)
    test_graph[combi[0][0]][combi[0][1]] = 1
    test_graph[combi[1][0]][combi[1][1]] = 1
    test_graph[combi[2][0]][combi[2][1]] = 1
    spread(test_graph)
    z = check_zero(test_graph)
    if z > ans :
        ans = z
print(ans)