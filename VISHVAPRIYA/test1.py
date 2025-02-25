def myfunc():
  a = 300
  print(a)




def hellofunc():
  b = 600
  def myinnerfunc():
    print(b)
  myinnerfunc()




x = 453

def globalfunc():
    
    print(x)

print(x)


def abcd():
  global x
  x = 300
  print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  print(x)


