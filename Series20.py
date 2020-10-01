from random import randint

N=int(input())
l = [randint(2,N) for x in range(N)]
print(l)
k=0
r=0
for g in l:
    if r <= N-2:
        if l[r]<l[r+1]:
            print(l[r])
            k+=1
    r+=1

print('кол-во чисел',k)






