from os import walk


def heh(dir):
    for (path,names,files) in walk(dir):
            for file in files:
                print(file)
            if len(names)!=0:
                for i in range(len(names)):
                    print(dir+'//'+names[i])
                    heh(dir+'//'+names[i])
            return 0
heh('Documents')
                    
            
