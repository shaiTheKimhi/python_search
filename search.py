import os 
import sys
def searchInDir(fileName,dirName,list):
    dirs = os.listdir(dirName)
    for f in dirs:
        if(f.lower()==fileName):
            list.append(dirName+"/"+fileName)
        if(len(f.split("."))==1):
            searchInDir(fileName,f,list)
    return list
def searchTree(fileName,Dir):
    l=[]
    l = searchInDir(fileName,Dir,l)
    print(l)
    # change to return

dir = os.getcwd()
fileName = sys.argv[1]
searchTree(fileName, dir)
print("Press Enter to continue...")
nothing = input()