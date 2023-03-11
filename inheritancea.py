# class prog:
#     def input(self):
#         self.a=int(input("enter a roll no :"))
# class prog2(prog):
#     def marks(self):
#         self.m1=int(input("enter marks 1 :"))
#         self.m2=int(input("enter marks 2 :"))
#         self.m3=int(input("enter marks 3 :"))
# class prog3(prog2):
#     def total(self):
#         print("roll no is",self.a)
#         print("your marks is :""m1=",self.m1,"m2=",self.m2,"m3=",self.m3)
#         total=self.m1+self.m2+self.m3
#         print("total is ",total)
#         print("percentage is :",total/3)
# p=prog3()
# p.input()
# p.marks()
# p.total()


class prog:
    def input (self):
        self.a=int(input("enter a number :"))
        self.b=int(input("enter a number :"))
class prog1(prog):
    def add(self):
        self.c=self.a+self.b
class prog2(prog):
    def multi(self):
        self.z=self.a*self.b
class prog3(prog1,prog2):
    def result(self):
        print(self.c)
        print(self.z)
p=prog3()
p.input()
p.add()
p.multi()
p.result()