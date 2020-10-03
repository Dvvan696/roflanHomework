from random import randint
import Series23b
N=int(input())
l = [randint(3,N) for x in range(N)]
print(l)
print(Series23b.heh(N,l))

