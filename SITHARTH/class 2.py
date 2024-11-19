class myclass():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
a1=myclass("sitharth",23)
a2=myclass("ashu",23)
print(a1,a2)
 
