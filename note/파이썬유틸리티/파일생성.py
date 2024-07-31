# 원하는 위치에 파일을 생성하는 프로그램, for문으로 여러 파일을 만드는 프로그림

import os
os.mkdir(r"C:\Users\gladi\study\temp") # temp 폴더 생성
for i in range(1, 15):
    # 파일 이름 입력 받는다
    fname = input("파일 이름을 입력하세요: {0}번째 파일 생성: ".format(i))
    f = open(r"C:\Users\gladi\study\temp\Ex1_" + str(i) + fname + ".java", "w") 
    f.close()