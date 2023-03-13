f1=open("D:\\python workspace\\abc.txt","w")
f1.write("this file is created")

# x takla ki aadhichi file la error yeto ani w takla ki ti fike to overwrite krto
# x mode ne file new create krto 
#  modes in file handling 
#  r= read mode
#  a=apend mode
#  w=write mode
#  x=create a new file and error exixting file 
# rt=read text 
# rb=read binary file show image file 

f1=open("D:\\python workspace\\abc.txt","rt")
x=f1.read()
print(x)