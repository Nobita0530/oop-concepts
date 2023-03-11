# fileptr=open("file.txt","r")
# if fileptr:
#     print("file open sucessfully")
#     fileptr.close()
    
# else:
#     print("not found")

fileptr=open("file2.txt","w+")

fileptr.write('''''python is morden day language.It makes things so simple.''')
if fileptr:
    print("file create sucessfully")
    fileptr.close()