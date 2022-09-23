n = int(input())
l = []
for _ in range(n) :
    l.append(int(input()))

if len(l) == 1 :
    print(l[0])
elif len(l) == 2 :
    print(sum(l))
else :
    dp = [0]*n
    dp[0] = l[0]
    dp[1] = l[1] + l[0]
    dp[2] = max(l[2]+l[1], dp[0]+l[2], dp[1])
    for i in range(3,n) :
        dp[i] = max(dp[i-3]+l[i-1]+l[i],dp[i-2]+l[i],dp[i-1])
    print(dp[-1])