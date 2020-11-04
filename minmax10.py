import random
n = int(input())
l = [random.randint(0, n) for x in range(n)]
print(l)
for i in range(len(l)):
    if i == 0:
        min = l[i]
        max = l[i]
        z = i
        x = i
    if l[i] > max:
        z = i
        max = l[i]
    if l[i] < min:
        x = i
        min = l[i]
if x < z:
    print(min)
else:
    print(max)
print(min, max)
