n, m = [int(i) for i in input().split()]

on = []
for _ in range(n):
    on.append(tuple( [int(i) for i in input().split()] ))


def take_stap(r, s):
    step = None
    for i in [(r-1, s), (r, s-1), (r, s+1), (r+1, s)]:
        
        if i[0] == 0 or i[1] == 0 or \
           i[0] > n or i[1] > n or \
           i in used or \
           i not in on:
            continue

        step = i
        used.append(i)

    return step


r = s = 1
used = [(r, s)]

def main(r, s):    
    blick = 0
    step = (r,s)

    while step != (n, n):
        step = take_stap(r, s)

        if step is None:
            blick += 1
            for i in range(s+1, n+1):
                on.append((r, i))

            if (r,s) == on[-1]:
                return -1

            continue

        r, s = step

    return blick


print(main(r, s))
