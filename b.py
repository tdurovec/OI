from itertools import permutations
nums = 0

n = int(input())
lst = [int(i) for i in input().split()]
lst.append(n)
all_perms = permutations(lst)


def postupne(a, b):
    
    if a % 2 == 0:
        eq = a-1
    else:
        eq = a+1

    if a == eq or \
       b == eq:
        return True

    return False

if len(lst) > 3:
    for perm in all_perms:
        lst = list(perm)

        c = 1
        while True:
            if len(lst) <= 1:
                break
            if c >= len(lst):
                break

            a, b = lst[c-1], lst[c]
            if postupne(a, b):
                lst.pop(c-1)
                lst.pop(c-1)
                c-=2

            c+=1

        if len(lst) <= 1:
            nums+=1

    print(nums)
else:
    print(len(list(all_perms)))

