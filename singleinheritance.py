class prog:
    def input(self):
        self.a=int(input("enter a no"))
        self.b=int(input("enter a no"))
class prog2(prog):
    def add(self):
        c=self.a+self.b
        print(c)
p=prog2()
p.input()
p.add()