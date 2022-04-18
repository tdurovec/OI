import math

def fact(n,_factcache={}):
    if n not in _factcache:
        _factcache[n] = math.factorial(n)
    return _factcache[n]


a, b = 4, 10
c = 0

for i in range(a,11):

    f = str(fact(i))
    if f[-1] == "0":
        rf = reversed(f) 
        for j in rf:
            if j != "0":
                break
            c+=1

print(c)

