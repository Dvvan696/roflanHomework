n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    S = a * b
    if i == 0:
        min = S

    if min > S:
        min = S

print(min)
