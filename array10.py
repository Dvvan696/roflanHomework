import random
n=int(input()) #введите четное число
l = [random.randint(0, n) for x in range(n)]
print(l)
for i in range (n//2):
    l[i*2], l[i * 2+1]  = l[i * 2+1] , l[i*2]

print(l)

