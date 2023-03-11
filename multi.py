class prog:
    def input(self):
        self.a=int(input("enter a no"))
        self.b=int(input("enter a no"))
class prog2(prog):
    def add(self):
        c=self.a+self.b
        print("addition is",c)
class prog3(prog):
    def multi(self):
        c=self.a*self.b
        print("multiplication is",c)
p2=prog3()
p=prog2()
p.input()
p.add()
p2.input()
p2.multi()