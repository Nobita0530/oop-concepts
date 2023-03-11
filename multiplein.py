class prog:
    def __init__(self):
        print("prog 1")
class prog2(prog):
    def __init__(self):
        super().__init__()
        print("prog 2")
class prog3(prog2):
    def __init__(self):
        super().__init__()
        print("prog 3")
p=prog3()
