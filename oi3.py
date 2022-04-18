lst = "4 5 2".split(' ')
#lst = "7 8 10 4 2".split(' ')
#lst = "7 7 1 4 5".split(' ')
lst = [int(i) for i in lst]

check = sorted(lst)

c = 0
for i in range(len(lst)):
    
    minNum = sorted(lst)[c]
    if lst[i] != minNum:
        idx = lst.index(minNum)

        if i+1 < len(lst) and i+1 != idx:
            v = lst[i]
            lst[i] = minNum
            lst[idx] = v

    c += 1

if check == lst:
    print("ano")
else:
    print("nie")