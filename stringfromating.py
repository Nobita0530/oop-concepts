# capitalize()
s1="python programming"
s2=s1.capitalize() #store in s2 
print(s2)
#  center()
s1="python programming"
s2=s1.center(20,'*') 
print(s2)

# count()
s1="python programming"
s2=s1.count('o') # count('o',5,18) index number 5 is starting and 18 is ending  
print(s2)

# decode()
s1=b"python programming"
s2=s1.decode() 
print(s2)

# encode()
s1="python programming"
s2=s1.encode() 
print(s2)

# endswith()
s1="python programming is easy to learn."
s2=s1.endswith('learn.') # end with word learn.
print(s2)

s1="python programming is easy to learn."
s2=s1.endswith('easy',7,26) #7 and 26 is index number the given string... 
print(s2)

# expandtabs()
s1="python\tprogramming"
s2=s1.expandtabs(20) # using /t use tab 
print(s2)

# enumerate()
s1=["orange","mango","banana","apple"]
s2=enumerate(s1) 
print(list(s2))

# find
s1="python programming"
s2=s1.find('prog',15) 
print(s2)


# isdigit()
s1="1234"
s2=s1.isdigit() #its imagine a digits
print(s2)

s2="Yash"
b=s2.isdigit()
print(b)

# isalpha
s1="Yash"
c=s1.isalpha()
print(c)

# isalpha()
s2="1234"
x=s2.isalpha()
print(x)

# isalnum()
s1="yas21"
s=s1.isalnum()
print(s)

s2="yash"
z=s2.isalnum()
print(z)

# islower()
s1="python"
b=s1.islower()
print(b)

# isupper()
s1="PYTHON"
b=s1.isupper()
print(b)

# isnumeric()
s1="13287"
b=s1.isnumeric()
print(b)

# isspace
s1="  "
b=s1.isspace()
print(b)

# istitle()
s1="Python Programming"
b=s1.istitle()
print(b)