k=int(input()) #выпало 2 одинаковых задания, поэтому взял это на рандом
fk1=1
fk2=1
for i in range(3, k):
    fk=fk1+fk2
    fk2 = fk1
    fk1 = fk
    print(fk)
