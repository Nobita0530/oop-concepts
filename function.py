# def add():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=a+b
#     print(c)
# add() 

# # parameterize functions
# def multi(a,b):
#     c=a*b
#     print(c)
# multi(10,5)

# # return values

# def add(a,b):
#     c=a+b
#     return(c)
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# z=add(x,y)
# print(z)

# reverse

def rev(n):
    s=0
    t=n
    while n>0 :
        r=n%10
        s=s*10+r
        n=int(n/10)
    return(s)
i=int(input("enter a number"))
z=rev(i)
print(z)
if i==z:
    print("palendrom")
else:
    print("not palendrom")