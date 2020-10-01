from random import randint
N=int(input())
l = [randint(3,N) for x in range(N)]
print(l)
k=0
r=0
for g in l:
    if r <= N-2:
        if l[r-1]>l[r] and l[r]<l[r+1]:
            print(0)
        elif l[r-1]<l[r] and l[r]>l[r+1]:
            print(0)
        else:
            print(l[0])
    r+=1

