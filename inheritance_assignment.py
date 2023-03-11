class c1:
    def __init__(self):
        self.r=int(input("enter a roll no"))
class c2(c1):
    def __init__(self):
        super().__init__()
        self.n=input("enter a name ")
class c3(c2):
    def __init__(self):
        super().__init__()
        self.c=input("enter your city name ")
    def dis(self):
        print("******************* your responce*******************")
        print("roll no is",self.r)
        print("name is ",self.n)
        print("city is",self.c)
p=c3()
p.dis()



# class c1:
#     def __init__(self,r):
#         self.r=r
# class c2(c1):
#     def __init__(self,n,r):
#         super().__init__(r)
#         self.n=n
# class c3(c2):
#     def __init__(self,c,r,n):
#         super().__init__(r,n)
#         self.c=c
#     def dis(self):
#         print("roll no is",self.r)
#         print("name is ",self.c)
#         print("city is",self.c)
# p=c3(1,"prasad","malegaon")
# p.dis()
