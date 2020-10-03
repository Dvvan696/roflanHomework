
def heh(N,l):
    k=0
    r=0
    for g in l:
        if r <= N - 2:
            if l[r] < l[r + 1]:
                print(l[r])
                k += 1
        r += 1
    return k