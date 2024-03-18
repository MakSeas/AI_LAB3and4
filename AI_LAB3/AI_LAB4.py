import Arithmetics
import CoolDivide
import TaylorFunctions

while(True):
    print("Выбор действия:")
    print("0 - Арифмитические операции:")
    print("1 - Вычисление тригонометрических функций")
    print("2 - Деление с остатком")

    basicAct=input()

    if(basicAct=="0"):
        while True :
            print("Выбор арифмитической операции:")
            print("0 - сложение")
            print("1 - Вычитание")
            print("2 - Умножение")
            print("3 - Деление")
            print("4 - прекратить арифмитические действия")

            arithAct=input()
            print("Введите два слагаемых:")
            a, b=int(input())

            if(arithAct=="0"):          
                a, b=int(input())
                print(f"{a} + {b} = {Arithmetics.Summ(a,b)}")
            elif(arithAct=="1"):
                print(f"{a} - {b} = {Arithmetics.Sub(a,b)}")
            elif(arithAct=="2"):
                print(f"{a} * {b} = {Arithmetics.Mult(a,b)}")
            elif(arithAct=="3"):
                print(f"{a} / {b} = {Arithmetics.Divide(a,b)}")
            elif(arithAct=="4"):
                break
            break
    elif (basicAct=="1"):
        while(True):
            print("Выбор тригонометрической функции:")
            print("0 - sinus")
            print("1 - cosinus")
            print("2 - Прекратить работу с тригонометрическими функциями")

            trigAct=input()

            print("Введите аргумент функции и число членов ряда тейлора")
            x,y=input()

            if(trigAct=="0"):
                print(f"sin(x) = {TaylorFunctions.TaylorSinus(x,y)}")
            elif(trigAct=="1"):
                print(f"cos(x) = {TaylorFunctions.TaylorCosinus(x,y)}")
            elif(trigAct=="2"):
                break
    elif(basicAct=="2"):
        while(true):
            print("Введите делитель и делимое:")

            a,b=int(input())

            print(f"{a}/{b} Целая часть деления={CoolDivivde.GetDivideInt(a,b)}, Остаток от деления = {CoolDivide.GetDivideRem(a,b)}")