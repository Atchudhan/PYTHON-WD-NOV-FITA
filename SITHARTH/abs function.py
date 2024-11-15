def myfunc(n):
    return abs(n-50)

list1=[100,50,23,82,65]
list1.sort(key = myfunc)

print(list1)
