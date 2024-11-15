def  myfunc(n):
    return lambda a :a*n
num3 = myfunc(3)
print(num3(22))
