from collections import deque
n,m = map(int,input().split())

graph = [0]*101
dict_ladder = dict()
dict_snake = dict()
for i in range(n) :
    a,b = map(int,input().split())
    dict_ladder[a] = b
for ii in range(m) :
    c,d = map(int,input().split())
    dict_snake[c] = d

q = deque()
qnext = deque()

c = 1
visited = [0]*101
for init in range(2,8) :
    q.append(init)
while True :
    while q :
        num = q.popleft()
        

        if num in dict_ladder :
            if graph[dict_ladder[num]] ==0 or graph[dict_ladder[num]] > c :
                graph[dict_ladder[num]] = c
                q.append(dict_ladder[num])
        elif num in dict_snake :
            if graph[dict_snake[num]] ==0 or graph[dict_snake[num]] > c :
                graph[dict_snake[num]] = c
                q.append(dict_snake[num])
        else :
            if graph[num] == 0 :
                graph[num] = c
            else :
                graph[num] = min(graph[num],c)

        for x in range(1,7) :
            if (num not in dict_snake) and num+x <= 100 and visited[num+x] == 0:
                qnext.append(num+x)
                visited[num+x] = 1
    
    if not qnext :
        break
    else :
        q = qnext
        qnext = deque()    
        c += 1


print(graph[100])