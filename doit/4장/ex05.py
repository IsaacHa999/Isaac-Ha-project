i = input("사용자 입력: ")

f = open("itext.txt", "a")
f.write(i)
f.write("\n")
f.close()

f2 = open("itext.txt", "r")
print(f2.read())
f2.close()

