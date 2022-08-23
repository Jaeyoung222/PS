import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t) :
    x,y,a,b = map(int,input().split())
    seta = set()
    setb = set()
    for i in range(y) :
        seta.add(x*i+a)
    for j in range(x) :
        setb.add(y*j+b)
    ansset = seta.intersection(setb)
    if not ansset :
        print(-1)
        continue
    else :
        ans = min(ansset)    
    
    gcd = 0
    for num in range(1,min(x,y)+1) :
        if x%num == 0 and y%num == 0 :
            if gcd < num :
                gcd = num
    lcm = (x*y)//gcd
    if ans > lcm  :
        print(-1)
    else :
        print(ans)
    