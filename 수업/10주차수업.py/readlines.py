inFp  =None
fName, inList, inStr = "",[],""

fName = "C:/Temp/data1.txt"
inFp = open(fName, "r")

inList = inFp.read()


for inStr in inList:
    print(inStr, end ="")

inFp.close()