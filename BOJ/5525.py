import sys
input = sys.stdin.readline

n = int(input())
target = "I"+("OI"*n)

m = int(input())

s = input()
c = 0
for x in range(len(s)-(2*n+1)) :
    if s[x:(x+(2*n)+1)] == target :
        c += 1

print(c)
