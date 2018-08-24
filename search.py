import os 
import sys


def search_dir(fileName,dirName,list):
    dirs = os.listdir(dirName)
    for f in dirs:
        if(fileName.lower() in f.lower() and dirName+"/"+fileName not in list):
            list.append(dirName+"/"+fileName)
        if(os.path.isdir(dirName + "/" + f)):
            list = search_dir(fileName, dirName + "/" + f, list)
    return list
def search_tree(fileName,Dir):
    l=[]
    l = search_dir(fileName,Dir,l)
    print(l)
    return l

if(len(sys.argv) >= 2):
    fileName = sys.argv[1]
    dir = os.getcwd() if len(sys.argv) < 3 else sys.argv[2]
else:
    fileName = input("enter name to search")
    dir = input("enter search start directory")

def start(path):
    os.system(path)


search_tree(fileName, dir)
print("Press Enter to continue..." + dir + ":" + fileName)
nothing = input()
