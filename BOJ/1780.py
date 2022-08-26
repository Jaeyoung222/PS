import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))


plusone = 0
zero = 0
minusone = 0

def cut(graph) :
    global plusone
    global zero
    global minusone

    t = len(graph)
    if t == 3 :
        for row in range(t) :
            for col in range(t) :
                if graph[row][col] == 1 :
                    plusone += 1
                    continue
                elif graph[row][col] == 0 :
                    zero += 1
                    continue
                elif graph[row][col] == -1 :
                    minusone += 1
                    continue
        return
        

    else :
        p = t//3
        for x,y in [(0,0),(0,p),(0,2*p),(p,0),(p,p),(p,2*p),(2*p,0),(2*p,p),(2*p,2*p)] :
            s = set()
            for i in range(p) :
                for j in range(p) :
                    s.add(graph[x+i][y+j])
                    
            if len(s) == 1 :
                if 1 in s :
                    plusone += 1
                    continue
                elif -1 in s :
                    minusone += 1
                    continue
                elif 0 in s :
                    zero += 1
                    continue
            else :
                secondgraph = []
                
                for ii in range(p) :
                    secondgraph.append(graph[x+ii][y:y+p])
                
                cut(secondgraph)
                continue
        return

cut(graph)
print(minusone)
print(zero)
print(plusone)