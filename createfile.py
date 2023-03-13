f1=open("D:\\python workspace\\abc.txt","w")
f1.write("this file is created")

# x takla ki aadhichi file la error yeto ani w takla ki ti fike to overwrite krto
# x mode ne file new create krto 
#  modes in file handling 
#  r= read mode  f1= open("file path already created this file ") 
#  a=apend mode  f1.apend("content")
#   already you created file using apend add the text in your old file
#  w=write mode  open("path for creating file and write a message ")   f1.write("content")
#  x=create a new file and error exixting file  fi.read() print x
# rt=read text  read the text file 
# rb=read binary file show image file   for example 01010101011100

f1=open("D:\\python workspace\\abc.txt","rt")
x=f1.read()
print(x)
