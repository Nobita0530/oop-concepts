class prog:
    def input(self):
        self.a=int(input("enter a no"))
        self.b=int(input("enter a no"))
class prog2:
    def input1(self):
        self.x=int(input("enter a no"))
        self.y=int(input("enter a no"))
class prog3(prog,prog2):
    def add(self):
        c=self.a+self.b
        print(c)
    def multi(self):
        z=self.x*self.y
        print(z)
p=prog3()
p.input()
p.add()
p.input1()
p.multi()
