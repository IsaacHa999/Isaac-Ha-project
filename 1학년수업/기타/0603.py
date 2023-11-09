inFp, outFp  = None,None
inStr = ""

inFp = open("C:/ex code/picture1.jpg", "rb")
outFp = open("C:/Temp/picture1.jpg", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("---이진 파일이 정상적으로 복사되었음---")
