import os


os.system('CLS')
a = float(input("Введите число:\t"))
b = 999

while (True):
    
    action = input("Введите индекс действия:\n1)+\n2)-\n3)/\n4)*\n5)**\n")

    b = float(input("Введите число:\t"))
    
    print("Ответ:\t")

    if (action == "1"): 
        a = a+b
        print(a)    
    elif (action == "2"): 
        a = a-b
        print(a)
    elif (action == "3"):
        if(b == 0):
            print("На 0 делить нельзя!") 
        else:
            a = a/b
            print(a)
    elif (action == "4"): 
        a = a*b
        print(a)
    elif (action == "5"): 
        a = a**b
        print(a)
    else:
        print("Случилась ошибка!")


