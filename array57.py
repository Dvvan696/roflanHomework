import random

n = int(input())
l = [random.randint(0, n) for x in range(n)]

print(l)
b = []
m = []
for i in range(len(l)):  # четные в один массив
   while i <= len(l) - 1:
        b.append(l[i])
        i = i + 2
        print(b)
    break
for t in range(1, len(l)):  # нечетные в один массив
    while t <= len(l) - 1:
        m.append(l[t])
        t = t + 2
        print(m)
    break
b.extend(m)
print(b)
