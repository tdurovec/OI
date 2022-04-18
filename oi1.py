def najkratsia_cesta(cesta, N):
    maxp = 6
    mozne_cesty = []

    if cesta[N-1] == '-1':
        return '-1'

    if maxp > N:
        maxp = N-1

    for i in range(maxp,0,-1):

        if cesta[i] != "-1":
            rebrik = i + int(cesta[i])
            if [rebrik] not in mozne_cesty:
                mozne_cesty.append([rebrik])

    if mozne_cesty == []:
        return '-1'

    count = 0
    while count < N:

        lst = []
        for i in mozne_cesty: 
            krok = i[-1]
            posun = krok + maxp

            if posun >= N:
                posun = N-1

            if posun != krok:
                for c in range(posun,  krok, -1):
                    alst = i.copy()
                    if cesta[c] != "-1":
                        rebrik = c + int(cesta[c])
                        if cesta[rebrik] == "-1":
                            alst.append(c)
                        else:
                            alst.append(rebrik)
                        lst.append(alst)

                mozne_cesty = lst

        cesty_do_ciela = []
        for cesta in mozne_cesty:
            if cesta[-1] == N-1:
                cesty_do_ciela.append(cesta)
                
        if cesty_do_ciela != []:
            mozne_kroky = sorted([len(i) for i in cesty_do_ciela])[0]
            return mozne_kroky            

        count +=1


cesta = '0 0 6 0 0 3 0 0 11 0 0 0 0 0 4 0 0 0 0 0'.split(' ')
N = len(cesta)

res = najkratsia_cesta(cesta, N)
print(res)