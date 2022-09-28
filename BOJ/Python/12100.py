from collections import deque
import copy
def left(graph) :
    for i in range(len(graph)) :
        tmp = deque()
        for j in range(len(graph)) :
            if j == len(graph) -1 :
                if graph[i][j] == 0 :
                    break
                else :
                    tmp.append(graph[i][j])
                    break
            if graph[i][j] == 0 :
                continue
            
            for k in range(1,len(graph)-j) :
                if graph[i][j+k] == 0 :
                    if k==len(graph)-j-1 :
                        tmp.append(graph[i][j])
                    continue
                else :
                    if graph[i][j] == graph[i][j+k] and graph[i][j]!=0 :
                        tmp.append(graph[i][j]+graph[i][j+k])
                        graph[i][j] = 0
                        graph[i][j+k] = 0
                        break
                    else :
                        tmp.append(graph[i][j])
                        break

        tmp = list(tmp)
        tmp += [0]*(len(graph)-len(tmp))
        graph[i] = tmp
    return

def right(graph) :
    for i in range(len(graph)) :
        tmp = deque()
        for j in range(len(graph)-1,-1,-1) :
            if j == 0 :
                if graph[i][j] == 0 :
                    break
                else :
                    tmp.appendleft(graph[i][j])
                    break
            if graph[i][j] == 0 :
                continue

            for k in range(1,j+1) :
                if graph[i][j-k] == 0 :
                    if k==j :
                        tmp.appendleft(graph[i][j])
                    continue
                else :
                    if graph[i][j] == graph[i][j-k] and graph[i][j]!=0 :
                        tmp.appendleft(graph[i][j]+graph[i][j-k])
                        graph[i][j-k] = 0
                        graph[i][j] = 0
                        break
                    else :
                        tmp.appendleft(graph[i][j])
                        break

        tmp = list(tmp)
        tmp = [0]*(len(graph)-len(tmp)) + tmp
        graph[i] = tmp 
    return 

def up(graph) :
    for i in range(len(graph)) :
        tmp = deque()
        for j in range(len(graph)) :
            if j == len(graph)-1 :
                if graph[j][i] == 0 :
                    break
                else :
                    tmp.append(graph[j][i])
                    break

            if graph[j][i] == 0 :
                continue

            for k in range(1,len(graph)-j) :
                if graph[j+k][i] == 0 :
                    if k==len(graph)-j-1 :
                        tmp.append(graph[j][i])
                    continue
                else :
                    if graph[j][i] == graph[j+k][i] and graph[j][i]!=0 :
                        tmp.append(graph[j][i]+graph[j+k][i])
                        graph[j+k][i] = 0
                        graph[j][i] = 0
                        break
                    else :
                        tmp.append(graph[j][i])
                        break

        tmp = list(tmp)
        tmp += [0]*(len(graph)-len(tmp))
        
        for k in range(len(graph)) :
            graph[k][i] = tmp[k]
    return 

def down(graph) :
    for i in range(len(graph)) :
        tmp = deque()
        for j in range(len(graph)-1,-1,-1) :
            if j == 0 :
                if graph[j][i] == 0 :
                    break
                else :
                    tmp.appendleft(graph[j][i])
                    break

            if graph[j][i] == 0 :
                continue

            for k in range(1,j+1) :
                if graph[j-k][i] == 0 :
                    if k==j :
                        tmp.appendleft(graph[j][i])
                    continue
                else :
                    if graph[j][i] == graph[j-k][i] and graph[j][i]!=0 :
                        tmp.appendleft(graph[j][i]+graph[j-k][i])
                        graph[j-k][i] = 0
                        graph[j][i] = 0
                        break
                    else :
                        tmp.appendleft(graph[j][i])
                        break

        tmp = list(tmp)
        tmp = [0]*(len(graph)-len(tmp)) + tmp
        
        for k in range(len(graph)) :
            graph[k][i] = tmp[k]
    return

n = int(input())
original_graph = [list(map(int,input().split())) for _ in range(n)]

checklist = []
q = deque()
q.append('')
while q :
    s = q.popleft()
    if len(s) == 5 :
        checklist.append(s)
    else :
        for x in ['l','r','u','d'] :
            q.append(s+x)
graph = copy.deepcopy(original_graph)
m = 0
for x in checklist :
    for j in range(5) :
        if x[j] == 'l' :
            left(graph)
        elif x[j] == 'r' :
            right(graph)
        elif x[j] == 'u' :
            up(graph)
        elif x[j] == 'd' :
            down(graph)
    
    for i in range(len(graph)) :
        if m < max(graph[i]) :
            m = max(graph[i])

    graph=copy.deepcopy(original_graph)

print(m)