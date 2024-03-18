def GetDivideInt(x,y):
    result=0

    if(y!=0):
        return x//y
    else:
        return "Ответ не существует т.к. делитель равен нулю"

def GetDivideRem(x,y):
    if(y!=0):
        return x%y
    else:
        return "Ответ не существует т.к. делитель равен нулю"
