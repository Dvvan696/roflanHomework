def LeftShift3():
    A = input()
    B = input()
    C = input()
    x=C
    C=B
    B=A
    A=x
    print(A,B,C)
LeftShift3()#описание функции передачи


for i in range(0,2):
    print('введите числа')
    LeftShift3()
