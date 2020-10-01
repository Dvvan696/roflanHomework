n=int(input())
f=0
if n > 0:
    f=1
for i in range(1,n):
    f*=i
print(f)