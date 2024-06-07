import os
import shutil
from pathlib import Path

print(os.getcwd())

os.chdir("/Users/hasht/Desktop/Videos")
print(os.getcwd())


for file in os.listdir():
   
    name, ext = os.path.splitext(file)

    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"

    os.rename(file, new_name)

   


Path("data").mkdir(exist_ok=True)


if not os.path.exists("data"):
    os.mkdir("data")


shutil.move('f', 'd')  


shutil.copy("src", "dest")
shutil.copy2("src", "dest")


os.remove("filename")  
os.rmdir("folder")  
shutil.rmtree("folder")  
