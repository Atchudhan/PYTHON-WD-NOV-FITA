tuple1=(1,2,34,5,5)
print(tuple1)
print(len(tuple1))
print(type(tuple1))
a=tuple([1,2,34,5,5])
print(a)
b=("1",)
c=("1")
print(type(b))
print(type(c))
print(tuple1[1:5])
print(tuple1[-4:-2])
print(tuple1[:5])
print(tuple1[1:])


x=("1","2","333","4444","55555")
print(x)
y=list(x) #to change the tuple value ,first change into list ,then change the value and change into tuple
y[1]="22"
print(tuple(y))
