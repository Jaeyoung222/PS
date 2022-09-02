n,m = map(int,input().split())

ans = 1
for i in range(m) :
    ans = ans*(n-i)//(i+1)

print(ans)