class prog:
    def add(self):
        print("base")
class prog1(prog):
    def add(self):
        super().add()
        print("derive")
p=prog1()
p.add()