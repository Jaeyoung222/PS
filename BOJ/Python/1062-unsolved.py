n,k = map(int,input().split())

l = [[0]*26 for _ in range(n)]

for i in range(n) :
    s = list(input())
    for x in s :
        if l[i][ord(x)-ord('a')] == 0 :
            l[i][ord(x)-ord('a')] = 1
ls = []
for x in l :
    s = ''.join(str(s) for s in x)
    
    ls.append(s)
print(ls)
ans = 0xb111111111111111111111111111111
for x in s :
    ans = (ans & x)
print(ans)
