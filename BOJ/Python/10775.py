import sys
input= sys.stdin.readline
sys.setrecursionlimit(100000)
g = int(input())
p = int(input())
gate = [i for i in range(g+1)]
c = 0

def find(x) :
    if gate[x] != x :
        gate[x] = find(gate[x])
    return gate[x]
l = []
for _ in range(p) :
    l.append(int(input()))
for n in l :    
    if find(n) == 0 :
        break
    else :
        c += 1
        gate[find(n)] -= 1
print(c)