def heh(N,l):
    r = 0
    for g in l:
        if r <= N - 2:
            if l[r - 1] > l[r] and l[r] < l[r + 1]:
                print(0)
            elif l[r - 1] < l[r] and l[r] > l[r + 1]:
                print(0)
            else:
                print(l[r])
        r += 1
