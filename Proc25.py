from math import sqrt
import random
t=[]
def sSquare(k):
    for i in range (len(k)):
        m=sqrt(k[i])
        if m%1==0:
            t.append('True')
        else:
            t.append('False')   #описание функции sSquare


N=int(input())
k = [random.randint(1,N) for d in range(10)]
print(k)
sSquare(k)


print(t)



