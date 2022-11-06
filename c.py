c, x1, x2 = [int(i) for i in input().split()]

def to_bin(x):
    x0 = x2 = x//2
    x1 = x%2
    return (x0, x1, x2)


def all_to_bins_delay(lst):
    c = 0
    while not(all( i <= 1 for i in lst )):
        
        if lst[c] > 1:
            binrs = to_bin(lst[c])
            lst.pop(c)
            
            idx = c
            for binr in binrs:
                lst.insert(idx, binr)
                idx += 1

            c = 0
            continue

        c+=1

    return sum([i for i in lst[x1-1 : x2] if i == 1])


print(all_to_bins_delay([c]))
