start = "Lucenec"

with open("oi4.txt", "r") as fp:
    txt = fp.read().split("\n")

mesta = txt[0].split(",")
cesty = txt[1:]
km = 0

for cesta in cesty:
    cesta = cesta.split(",")
    if cesta[0] == start:
        start = cesta

vzd = [int(i) for i in start[1:]]
minVzd = sorted(vzd)[1]
idx = vzd.index(minVzd)+1

mesto = mesta[1:][idx]

print(mesto)