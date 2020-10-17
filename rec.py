m=[1,2,3,[4,5,6,[7,8,9,['qwe']],10,11],12,13]
def heh(x):
    for i in range(len(x)):
            if type(x[i])==list:
               (heh(x[i]))
            else:
                print(x[i])


heh(m)