import sys
input = sys.stdin.readline
from collections import deque
t = int(input().rstrip())
for _ in range(t) :
    ff = list(input().rstrip())
    f = deque(ff)
    n = int(input().rstrip())
    ll = input().rstrip()
    l = deque()
    if ll != "[]":
        l = deque(list(map(int,(ll[1:-1]).split(','))))
    c = 0
    r = 0
    while f :
        func = f.popleft()
        try :
            if func == 'R' :
                r += 1
            elif func == 'D' :
                if r % 2 == 0 :
                    l.popleft()
                else :
                    l.pop()
        except :
            c = 1
            print('error')
            break
    
    if r % 2 == 1 :
        l.reverse()
    if c == 0 and len(l) > 0:
        print('[',end="")
        for i in range(len(l)) :
            if i == len(l) -1 :
                print(l[i],end="")
            else :
                print(l[i],end=',')
        print(']')
    elif c == 0 and len(l) == 0 :
        print('[]')