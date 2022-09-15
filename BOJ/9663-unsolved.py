N = int(input())
column = [True]*N
Slash = [True]*(2 * N - 1)
backSlash = [True]*(2 * N - 1)
def putQueen(y):
    if y == N:
        return 1
    count = 0
    for x in range(N):
        if column[x] and Slash[y+x] and backSlash[y-x]:
            column[x] = Slash[y+x] = backSlash[y-x] = False
            count += putQueen(y+1)
            column[x] = Slash[y+x] = backSlash[y-x] = True
    return count
print(putQueen(0))