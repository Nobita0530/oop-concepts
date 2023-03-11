# def add():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a+b
#     print(c)

# def sub():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a-b
#     print(c)

# def multi():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a*b
#     print(c)
# def div():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a/b
#     print(c)
# add()
# sub()
# multi()
# div()

# print("parameterize functions")
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# def add(a,b):
#     c=a+b
#     print(c)
# def sub(a,b):
#     c=a-b
#     print(c)
# def multi(a,b):
#     c=a*b
#     print(c)
# def div(a,b):
#     c=a/b
#     print(c)
# add(x,y)
# sub(x,y)
# multi(x,y)
# div(x,y)

# print("fact")
# def fact(n):
#     s=1
#     i=1
#     while i<=n :
#         s=s*i
#         i=i+1
#         print (s)
# n=int(input("enter a number"))
# fact(n)

# print("reverse")
# def rev(n):
#     s=0
#     t=n
#     while n>0 :
#         r=n%10
#         s=s*10+r
#         n=int(n/10)
#     print(s)
# i=int(input())
# rev(i)

# print("prime no")

# def prime(n):
#     c=0
#     a=1
#     while c<=n:
#         r=r%a
#         if r==0:
#            c=c+1
#         a=a+1
           
# print("parameter")
# x=int(input())
# y=int(input())
# def add(a,b):
#     c=a+b
#     return(c)
# def sub(a,b):
#     c=a-b
#     return(c)
# def multi(a,b):
#     c=a*b
#     return(c)
# def div(a,b):
#     c=a/b
#     return(c)
# z=add(x,y)
# print("ans",z)
# z=sub(x,y)
# print("ans",z)
# z=multi(x,y)
# print("ans",z)
# z=div(x,y)
# print("ans",z)

def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def multi(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)
a=int(input("::"))
b=int(input("::"))    
print("enter your choice")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
ch=int(input())
if ch==1:
    add(a,b)
elif ch==2:
    sub(a,b)
elif ch==3:
    multi(a,b)
elif ch==4:
    div(a,b)
else :
    print("invalid input")
    