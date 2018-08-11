import os 
import sys
def searchInDir(fileName,dirName,list):
    dirs = os.listdir(dirName)
    for f in dirs:
        if(fileName.lower() in f.lower()):
            list.append(dirName+"/"+fileName)
        if(len(f.split("."))==1):
            searchInDir(fileName,f,list)
    return list
def searchTree(fileName,Dir):
    l=[]
    l = searchInDir(fileName,Dir,l)
    print(l)
    # change to return

if(len(sys.argv) >= 2):
    fileName = sys.argv[1]
    dir = len(sys.argv) < 3 ? os.getcwd() : sys.argv[2]
else:
    fileName = input("enter name to search")
    dir = input("enter search start directory")

searchTree(fileName, dir)
print("Press Enter to continue..." + dir + ":" + fileName)
nothing = input()