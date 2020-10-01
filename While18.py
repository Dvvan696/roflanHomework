i=int(input())
c=0
s=0
while i!=0:
    s=s+i%10
    i=i//10
    c+=1
print(c)
print(s)