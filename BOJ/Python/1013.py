n = int(input())

for _ in range(n) :
    str = input()
    isno = False
    length = len(str)

    if length == 1 :
        print("NO")
        continue

    elif length == 2 :
        if str == "01" :
            print("YES")
            continue
        else :
            print("NO")
            continue
    
    elif length == 3 :
        print("NO")
        continue
    else :
        zero_one_index = []
        for i in range(len(str)-2) :
            if str[i] == '1' and str[i+1] == '0' and str[i+2] == '1' :
                zero_one_index.append(i+1)
        
        check_list = []
        if zero_one_index :
            for i in range(len(zero_one_index)) :
                if i == 0 :
                    if str[:zero_one_index[i]] :
                        check_list.append(str[:zero_one_index[i]])
                if i==(len(zero_one_index)-1) :
                    if str[zero_one_index[i]+2:] :
                        check_list.append(str[zero_one_index[i]+2:])
                    if str[zero_one_index[i-1]+2:zero_one_index[i]] :
                        check_list.append(str[zero_one_index[i-1]+2:zero_one_index[i]])
                else :
                    if str[zero_one_index[i-1]+2:zero_one_index[i]] :
                        check_list.append(str[zero_one_index[i-1]+2:zero_one_index[i]])
        else :
            check_list.append(str)
        
        while check_list :
            if not isno :
                target = check_list.pop(0)

                if len(target) == 1 :
                    print("NO")
                    isno = True
                    break

                elif len(target) == 2 :
                    if target == "01" :
                        continue
                    else :
                        print("NO")
                        isno = True
                        break
                
                elif len(target) == 3 :
                    print("NO")
                    isno = True
                    break

                else :
                    while True :
                        if target[:2] == "01" :
                            target = target[2:]
                        else :
                            break

                    if target[:3] != "100" :
                        print("NO")
                        isno = True
                        break

                    else :
                        one_start = len(target)
                        for i in range(3,len(target)) :
                            if target[i] == "1" and i < one_start :
                                one_start = i
                                continue

                            if i> one_start and target[i] == "0" :
                                if target[i-2:i+2] == "1100" :
                                    check_list.append(target[i-1:])
                                    break
                                else :
                                    print("NO")
                                    isno = True
                                    break

                        if one_start == len(target) :
                            isno = True
                            print("NO")
                            break
            else :
                break
    if not isno :
        print("YES")
        continue
    







