

A=float(input())
k=2
ak1=1
ak=2
while A<= abs(ak-ak1):
    ak2 = ak1
    ak1 = ak
    k+=1
    ak=(ak2+2*ak1)/3
print (k,' ',ak,' ',ak1)




