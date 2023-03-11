# m=int(input("enter marks"))
# if m<32:
#     print("Fail")
# else :
#     print("Pass") 

    
# m=int(input("enter number :"))
# if m<0 :
#     print("negative")
# else :
#     print("positve")

    
# m=int(input("enter number :"))
# if m<10 :
#     print("single digit")
# else :
#     print("double digit")

    
# n=(input("enter Student name :"))
# r=int(input("enter roll number :"))
# m1=int(input("enter marks 1 :"))
# m2=int(input("enter marks 2 :"))
# m3=int(input("enter marks 3 :"))
# print("name is ",n)
# print("roll no is ",r)
# m4=m1+m2+m3
# print("total marks  ",m4)
# m5=m4/3
# print("percentage is ",m5)


# m=int(input("enter age :"))
# if m<19 :
#     print("your not eligible for voting")
# else:
#     print("eligible for voting")


# m=int(input("enter marks :"))
# if m<35 :
#     print("fail")
# elif m<50 :
#     print("pass")
# elif m<70 :
#     print("2nd class")
# elif m<80 :
#     print("1st class")
# else :
#     print("distiction")
    
    
# amt=int(input("Enter a amount"))
# if amt<300000:
#     tax=0
# elif amt<600000 :
#     tax=amt/100*5
# elif amt<900000:
#     tax=amt/100*10
# elif amt<1200000:
#     tax=amt/100*15
# elif amt<1500000:
#     tax=amt/100*20
# else:
#     tax=amt/100*30
# total=amt-tax
# print("your amount is ",amt)
# print("your tax is ",tax)
# print("your total is ",total)

# a=int(input("enter a number "))
# b=int(input("enter a number "))
# if a>b:
#     print(a,"is greater than",b)
# else :
#     print(b,"is greater than",a)

pcode=int(input("enter product code"))
amt=int(input("enter purchase ammount :"))

if pcode==1 :
    if amt<1000 :
        dis=amt/100*20
    else :
        dis=0
elif pcode==2:
    if amt<500:
        dis=amt/100*10
    else:
        dis=0
elif pcode==3:
    if amt<100:
        dis=amt/100*5
    else:
        dis=0
else:
    dis=0
total=amt-dis
print("your total is",total)
print("your discount is",dis)