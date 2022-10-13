'''
ccw 뭔지 찾고 공부할 것.

n = int(input())
p = [[0,0]]
parent = [i for i in range(n+1)]
for i in range(n) :
    p.append(list(map(int,input().split())))

def meet(p1,p2) :
    p1_x1,p1_y1,p1_x2,p1_y2 = p1
    p2_x1,p2_y1,p2_x2,p2_y2 = p2

    if p1_x1==p1_x2 and p2_x1==p2_x2:
        if p1_x1 != p2_x1 :
            return False
        else :
            if (max(p1_y1,p1_y2) < min(p2_y1,p2_y2)) or (min(p1_y1,p1_y2) > max(p2_y1,p2_y2)) :
                return False
            else :
                return True

    if p1_x1 == p1_x2 :
        if max(p1_x1,p1_x2) < min(p2_x1,p2_x2) or min(p1_x1,p1_x2) > max(p2_x1,p2_x2) :
            return False
        if (((p2_y2-p2_y1)/(p2_x2-p2_x1))*(p1_x1-p2_x1)+p2_y1 > max(p1_y1,p1_y2)) or (((p2_y2-p2_y1)/(p2_x2-p2_x1))*(p1_x1-p2_x1)+p2_y1 < min(p1_y1,p1_y2)) :
            return False
        else :
            return True

    if p2_x1 == p2_x2 :
        if max(p1_x1,p1_x2) < min(p2_x1,p2_x2) or min(p1_x1,p1_x2) > max(p2_x1,p2_x2) :
            return False
        if (((p1_y2-p1_y1)/(p1_x2-p1_x1))*(p2_x1-p1_x1)+p1_y1 > max(p2_y1,p2_y2)) or (((p1_y2-p1_y1)/(p1_x2-p1_x1))*(p2_x1-p1_x1)+p1_y1 < min(p2_y1,p2_y2)) :
            return False
        else :
            return True

    else :
        p1x1 = min(p1_x1,p1_x2)
        if p1x1 == p1_x1 :
            p1x2 = p1_x2
            p1y1 = p1_y1
            p1y2 = p1_y2
        else :
            p1x2 = p1_x1
            p1y1 = p1_y2
            p1y2 = p1_y1
        
        p2x1 = min(p2_x1,p2_x2)
        if p2x1 == p2_x1 :
            p2x2 = p2_x2
            p2y1 = p2_y1
            p2y2 = p2_y2
        else :
            p2x2 = p2_x1
            p2y1 = p2_y2
            p2y2 = p2_y1

        k1 = (p1y2-p1y1)/(p1x2-p1x1)
        k2 = (p2y2-p2y1)/(p2x2-p2x1)

        if p1x2 < p2x1 or p1x1 > p2x2 :
            return False
        
        if p1x2==p2x1 :
            if p1y2==p2y1 :
                return True
            else :
                return False
        
        if p1x1==p2x2 :
            if p1y1==p2y2 :
                return True
            else :
                return False
        
        

        if p1x1 < p2x1 and p1x2 > p2x1 :
            a = k1*(p2x1-p1x1)+p1y1-p2y1
            b = p1y1-k2*(p1x1-p2x1)-p2y1
            if a*b > 0 :
                return False 
            else :
                return True
        
        if p1x1 > p2x1 and p1x1 < p2x2 :
            a = k1*(p2x2-p1x1)+p1y1-p2y2
            b = p1y1-k2*(p1x1-p2x1)-p2y1
            if a*b > 0 :
                return False 
            else :
                return True

        if p1x1<=p2x1 and p1x2 >= p2x2 :
            a = k1*(p2x1-p1x1)+p1y1-p2y1
            b = k1*(p2x2-p1x1)+p1y1-p2y2
            if a*b > 0 :
                return False 
            else :
                return True
        
        if p2x1<=p1x1 and p2x2 >= p1x2 :
            a = k2*(p1x1-p2x1)+p2y1-p1y1
            b = k2*(p1x2-p2x1)+p2y1-p1y2
            if a*b > 0 :
                return False 
            else :
                return True
    
    return False


def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    if meet(p[a],p[b]) :
        parent[a] = find(b)

for i in range(1,n+1) :
    for j in range(1,n+1) :
        union(i,j)

for i in range(1,n+1) :
    parent[i] = find(i)

ans = [0]*(n+1)
for x in parent :
    ans[x] += 1
c = 0
for i in range(1,n+1) :
    if ans[i] != 0 :
        c += 1

print(c)
print(max(ans))

'''

import sys
input = sys.stdin.readline
n = int(input())
s = []
parent = []
parent_ = []
def getParent(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = getParent(parent[a])
        return parent[a]
def union(x, y):
    parentX = getParent(x)
    parentY = getParent(y)
    if parentX > parentY:
        parent[parentX] = parentY
    elif parentY > parentX:
        parent[parentY] = parentX
def ccw(p1, p2, p3):
    temp = (p1[0] * p2[1]) + (p2[0] * p3[1]) + (p3[0] * p1[1])
    temp = temp - (p1[1] * p2[0]) - (p2[1] * p3[0]) - (p3[1] * p1[0])
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0
def checkCross(li1, li2):
    li1p1 = [li1[0], li1[1]]
    li1p2 = [li1[2], li1[3]]
    li2p1 = [li2[0], li2[1]]
    li2p2 = [li2[2], li2[3]]
    result1 = ccw(li1p1, li1p2, li2p1) * ccw(li1p1, li1p2, li2p2)
    result2 = ccw(li2p1, li2p2, li1p1) * ccw(li2p1, li2p2, li1p2)
    if result1 <= 0 and result2 <= 0:
        if ((li1p1[0] > li2p1[0] and li1p1[0] > li2p2[0] and li1p2[0] > li2p1[0] and li1p2[0] > li2p2[0]) 
        or (li1p1[0] < li2p1[0] and li1p1[0] < li2p2[0] and li1p2[0] < li2p1[0] and li1p2[0] < li2p2[0])):
            return False
        elif ((li1p1[1] > li2p1[1] and li1p1[1] > li2p2[1] and li1p2[1] > li2p1[1] and li1p2[1] > li2p2[1]) 
        or (li1p1[1] < li2p1[1] and li1p1[1] < li2p2[1] and li1p2[1] < li2p1[1] and li1p2[1] < li2p2[1])):
            return False
        else:
            return True
    return False
for i in range(n):
    s.append(list(map(int, input().split())))
    parent.append(i)
    parent_.append(0)
for i in range(n - 1):
    for j in range(i + 1, n):
        if checkCross(s[i], s[j]):
            union(i, j)
cnt = 0
max_num = 0
for i in range(n):
    if parent[i] == i:
        cnt += 1
    parent_[getParent(i)] += 1
    if parent_[getParent(i)] > max_num:
        max_num = parent_[getParent(i)]
print(cnt)
print(max_num)