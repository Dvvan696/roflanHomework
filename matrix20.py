import random
L=int(input())#диапозон чесел в матрице
N = int(input())#кол-во столбиков
M = int(input())#кол-во строк

def matrixgenerator(N,M):
    marx = [[random.randint(0,L) for j in range(N)] for i in range(M)]
    print(marx)
    sum=1
    for i in range(M):
        for j in range(N):
            sum*=marx[j][i]

        print(sum)
        sum = 1
matrixgenerator(N,M)




