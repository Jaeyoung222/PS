n = int(input())
l = list(map(int,input().split()))

one = 0
two = 0
three = 0

i = 0
c = 0

while i != n :
    if l[i] == 0 :
        if c == 1 :
            one += 1
        elif c == 2 :
            two += 1
        c = 0
        i += 1
    
    elif l[i] != 0 and i!=n-1 :
        l[i] -= 1
        c += 1
        if c == 3 :
            three += 1
            c = 0
        
        if l[i] == 0 :
            i += 1
            continue
        else :
            one += l[i]-l[i+]
            l[i] = 1
            if c == 1 :
                one += 1
            elif c == 2 :
                two += 1
            c = 0
    elif i==n-1 and c!=0 :
        one += l[i]-1
        c += 1
        if c == 2 :
            two += 1
        if c == 3 :
            three += 1
        l[i] = 0
    elif i==n-1 :
        one += l[i]
        l[i] = 0

print(one*3 + two*5 + three*7)