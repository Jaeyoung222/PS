n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(n) :
    if parent[n] != n :
        parent[n] = find(parent[n])
    return parent[n]

def union(n1, n2) :
    r1 = find(n1)
    r2 = find(n2)
    if r1 < r2 :
        parent[r2] = r1
    else :
        parent[r1] = r2

l = list(map(int,input().split()))
for i in range(l.pop(0)) :
    parent[l[i]] = 0

parties = []
for _ in range(m) :
    party = list(map(int,input().split()))
    p = party.pop(0)
    for i in range(p-1) :
        union(party[i],party[i+1])
    parties.append(party)

answer = 0

for party in parties :
    know = False
    for i in range(len(party)) :
        if find(party[i]) == 0 :
            know = True
            break
    if not know :
        answer += 1

print(answer)