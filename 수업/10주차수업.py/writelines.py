# outFp = None
# outStr = ""

# outFp = open("C:/Temp/data2.txt","w")
# while True:
#     outStr = input("내용 입력: ")
#     if outStr !="":
#         outFp.writelines(outStr + "\n")
#     else:
#         break
# outFp.close()
# print("---정상적으로 파일에 씀---")

# inFp = None
# inList = ""

inFp = open("C:temp/data2.txt",'r')
inList = inFp.readlines()
for i in inList:
    print(i,end="")
inFp.close()

outFp = open("C:/Temp/data2.txt","w")
outStr = """파이썬최고
배고프다
먹을 거 없나?"""
outFp.writelines(outStr)
outFp.close()