import random
L=int(input())#диапозон чесел в матрице
M = int(input())#кол-во столбиков
N = int(input())#кол-во строк
#marx=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]
marx = [[random.randint(0,L) for j in range(M)] for i in range(N)]
print(marx)
a=0
su=0
for i in range(M):
    if marx[1][i] >= marx[0][i]:
        c=1
        b=1
    else:
        c=-1
        b=-1
    if su==(N-1):
        break
    else:
        su=0
    for j in range(1,N):
        if marx[j][i]>=marx[j-1][i]:
            c=1
            if c == b and a<=marx[j][i]:
                a=marx[j][i]
                su+=1
            b = 1
        elif marx[j][i]<marx[j-1][i]:
            c=-1
            if c == b and a <= marx[j-1][i]:
                a = marx[j-1][i]
                su+=1
            b=-1
if su==N-1:
    print(a)
else:
    print(0)