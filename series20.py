from random import randint
N=(int(input()))
l=[randint(2,N) for x in range(N)]
print(l)
r=open('total.txt','w')
f=open('text_int.txt','r')
f=f.read()
def heh(N,l,f):
    a=list(map(int,f.split()))
    for g in l:
        if a[1]<=N-2:
            if l[a[1]]<l[a[1]+1]:
                print(l[a[1]])
                a[0]+=1
        a[1]+=1
    return a[0]
heh(N,l,f)
r.write('кол-во чисел'+ str (heh(N,l,f)))
r.close()
f.close()

    

