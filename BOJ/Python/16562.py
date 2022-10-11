n,m,k = map(int,input().split())

cost = list(map(int,input().split()))
cost = [0]+cost
parent = [i for i in range(n+1)]
def find(x) :
    while x != parent[x] :
        x = parent[x]
    return x
def union(a,b) :
    c = find(a)
    d = find(b)
    if c>d :
        parent[c] = find(d)
    else :
        parent[d] = find(c)



for _ in range(m) :
    a,b = map(int,input().split())
    union(a,b)

price = [[] for i in range(n+1)]
for i in range(n+1) :
    price[find(i)].append(i)
price.pop(0)
ans = 0

for people_list in price :
    if people_list!=[] :
        minimum = 10000
        for x in people_list :
            minimum = min(minimum,cost[x])
        ans += minimum


if ans <= k :
    print(ans)
else :
    print("Oh no")