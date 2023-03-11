class prog:
    def input(self):
        self.a=int(input("enter a no :"))
        self.b=int(input("enter a no :"))
class prog2(prog):
    def add(self):
        c=self.a+self.b
        print("addition is",c)
class prog3(prog2):
    def multi(self):
        c=self.a*self.b
        print("multi is ",c)
            
p=prog3()
p.input()
p.add()
p.multi()