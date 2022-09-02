t = int(input())
from collections import deque
class BinaryTreeNode :
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None
        self.up = None

    
    def winnercount(self, treenode) :
        s = set()
        v = treenode.value
        while treenode.up :
            s.add(treenode.up.value)
            treenode = treenode.up
        if v in s :
            s.remove(v)
        return len(s)
    
    def losercount(self, treenode) :
        s = set()
        v = treenode.value
        q = deque()
        q.append(treenode)
        while q :
                q.append(nod.left)
            nod = q.popleft()
            s.add(nod.value)
            if nod.left :
            if nod.right :
                q.append(nod.right)
        s.remove(v)
        return len(s)
    
                
for _ in range(t) :
    n = int(input())
    result = list(map(int,input().split()))
    tier = []
    for x in range(n) :
        tier.append(result[-(2**(x+1)-1):-((2**x)-1)])
    tier.pop(0)
    tier = [[result[-1]]]+tier
    tier.append(list(range(1,(2**n)+1)))

    tree = []
    for i in range(n+1) :
        tree.append([])
        for x in range(len(tier[i])) :
            tree[i].append(BinaryTreeNode(tier[i][x]))
    
    for tiers in range(len(tree)-1) :
        for node in range(len(tree[tiers])) :
                tree[tiers][node].left = tree[tiers+1][2*node]
                tree[tiers][node].right = tree[tiers+1][(2*node)+1]
                tree[tiers+1][2*node].up = tree[tiers][node]
                tree[tiers+1][(2*node)+1].up = tree[tiers][node]

    ans = []
    for xx in range((2**n)+1) :
        ans.append([0,0])
    
    for row in range(len(tree)) :
        for no in range(len(tree[row])) :
            if ans[tree[row][no].value] == [0,0] :
                ans[tree[row][no].value] = [BinaryTreeNode.winnercount(tree[row][no],tree[row][no]),BinaryTreeNode.losercount(tree[row][no],tree[row][no])]
    
    m = list(map(int,input().split()))
    for target in range(1,len(m)) :
        print("Player {} can be ranked as high as {} or as low as {}.".format((m[target]),(ans[m[target]][0]+1),((2**n)-ans[m[target]][1])))
    print("")