N,M=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(N)]
maximum=0

def maxcheck(arr,n,m,i,j):
    global maximum
    # 일자
    if j<=m-4:
        num=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]
        if num>maximum:
            maximum=num
    if i<=n-4:
        num=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
        if num>maximum:
            maximum=num
    # 네모
    if j<=m-2 and i<=n-2:
        num=arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]
        if num>maximum:
            maximum=num
    # L자
    if j<=m-2 and i<=n-3:
        num=arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
        if num>maximum:
            maximum=num
    if j>=1 and i<=n-3:
        num=arr[i][j]+arr[i][j-1]+arr[i+1][j-1]+arr[i+2][j-1]
        if num>maximum:
            maximum=num
    if j<=m-2 and i>=2:
        num=arr[i][j]+arr[i][j+1]+arr[i-1][j+1]+arr[i-2][j+1]
        if num>maximum:
            maximum=num
    if j>=1 and i>=2:
        num=arr[i][j]+arr[i][j-1]+arr[i-1][j-1]+arr[i-2][j-1]
        if num>maximum:
            maximum=num
    
    if j<=m-3 and i>=1:
        num=arr[i][j]+arr[i-1][j]+arr[i-1][j+1]+arr[i-1][j+2]
        if num>maximum:
            maximum=num
    if j>=2 and i>=1:
        num=arr[i-1][j-2]+arr[i-1][j-1]+arr[i-1][j]+arr[i][j]
        if num>maximum:
            maximum=num
    if j<=m-3 and i<=n-2:
        num=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
        if num>maximum:
            maximum=num
    if j>=2 and i<=n-2:
        num=arr[i+1][j-2]+arr[i+1][j-1]+arr[i+1][j]+arr[i][j]
        if num>maximum:
            maximum=num
    
    # ㄱㄴ
    if j<=m-2 and i<=n-3:
        num=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]
        if num>maximum:
            maximum=num
    if j>=1 and i<=n-3:
        num=arr[i][j]+arr[i+1][j]+arr[i+1][j-1]+arr[i+2][j-1]
        if num>maximum:
            maximum=num
    if j<=m-3 and i>=1:
        num=arr[i][j]+arr[i][j+1]+arr[i-1][j+1]+arr[i-1][j+2]
        if num>maximum:
            maximum=num
    if j>=2 and i>=1:
        num=arr[i][j]+arr[i][j-1]+arr[i-1][j-1]+arr[i-1][j-2]
        if num>maximum:
            maximum=num

    #ㅗ
    if j<=m-3 and i<=n-2:
        num=arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i][j+2]
        if num>maximum:
            maximum=num
    if j<=m-3 and i>=1:
        num=arr[i][j]+arr[i][j+1]+arr[i-1][j+1]+arr[i][j+2]
        if num>maximum:
            maximum=num
    if j<=m-2 and i>=2:
        num=arr[i][j]+arr[i-1][j]+arr[i-1][j+1]+arr[i-2][j]
        if num>maximum:
            maximum=num
    if j>=1 and i>=2:
        num=arr[i][j]+arr[i-1][j]+arr[i-1][j-1]+arr[i-2][j]
        if num>maximum:
            maximum=num


for i in range(N):
    for j in range(M):
        maxcheck(array,N,M,i,j)

print(maximum)