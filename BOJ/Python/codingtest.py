from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    graph = [['.']*(m+1) for _ in range(n+1)]
    graph[x][y] = 'S'
    graph[r][c] = 'E'
    command_list = []
    q = deque()
    q.append((x,y,'',0))
    while q :
        cx, cy,command,count = q.popleft()
        if count <= 4 :
            q.append((cx,cy-1,command+'l',count+1))
            q.append((cx,cy+1,command+'r',count+1))
            q.append((cx-1,cy,command+'u',count+1))
            q.append((cx+1,cy,command+'d',count+1))
        elif count==5 :
            if cx==r and cy==c :
                command_list.append(command)
        
        else :
            continue
    command_list.sort()
    answer = command_list[0]
    return answer
print(solution(3,4,2,3,3,1,5))