import os

# print(os.system("date"))

#os.mkdir(r"C:\Users\vaish\Desktop\c99\newFolder")


print(os.getcwd())

#check if folder exists
path=r"C:\Users\vaish\Desktop\c99\main.py"
isExist=os.path.exists(path)
print(isExist)

#spilt the name and extention 
root_ext=os.path.splitext(path)
print(root_ext)
print("root part ,",root_ext[0])
print("ext part ,",root_ext[1])

#list
print(os.listdir())

#copy one file to another
import shutil

source=r"C:\Users\vaish\Desktop\c99\abc.txt"
destination=r"C:\Users\vaish\Desktop\c99\abc1.txt"
dest=shutil.copy(source,destination)