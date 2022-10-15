'''
n,m = map(int,input().split())

parent = [[m*i]*m for i in range(n)]
for i in range(n) :
    for j in range(m) :
        parent[i][j] += j

map = []
for _ in range(n) :
    map.append(list(input()))

def find(i,j,p,q) :
    if m*i+j<m*p+q :
        p = i
        q = j
    elif m*i+j == m*p+q :
        parent[i][j] = m*i+j
        return parent[i][j]
    
    if parent[i][j] != m*i+j :
        parent[i][j]= find(parent[i][j]//m, parent[i][j]%m, p, q)
    return parent[i][j]

def union(i,j) :
    if map[i][j] == "D" :
        parent[i][j] = parent[i+1][j]
    elif map[i][j] == "U" :
        parent[i][j] = parent[i-1][j]        
    elif map[i][j] == "R" :
        parent[i][j] = parent[i][j+1]
    elif map[i][j] == "L" :
        parent[i][j] = parent[i][j-1]
    
for i in range(n) :
    for j in range(m) :
        union(i,j)

ans = set()
for i in range(n) :
    for j in range(m) :
        ans.add(find(i,j,n,m))

print(parent)
print(ans)
print(len(ans))
'''