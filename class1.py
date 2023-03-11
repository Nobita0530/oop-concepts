# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
        
# x=person("johan","doe")
# x.printname()

# class person:
#     def __init__(self,a,b):
#         self.c=a+b
#         self.d=a*b
#         self.e=a/b
#         self.f=a-b
#     def outp(self):
#         print("addtion is ",self.c)
#         print("substraction is ",self.f)
#         print("multiplication is ",self.d)
#         print("division is is ",self.e)        
# p=person(10,20)
# p.outp()

class arithmatic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        c=self.a+self.b
        print("addtion",c)
    def sub(self):
        c=self.a-self.b
        print("substraction",c)
    def multi(self):
        c=self.a*self.b
        print("multiplication",c)
    def div(self):
        c=self.a/self.b
        print("division",c)
a=arithmatic(10,10)
a.add()
a.sub()
a.multi()
a.div()