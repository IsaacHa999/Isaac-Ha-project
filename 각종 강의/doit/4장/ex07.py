f = open("test.txt", 'r')
a = f.read()
a2 = a.replace("java", "python")
f.close()
print(a)
print(a2)

f2 = open("test.txt", 'w')
f2.write(a2)
f2.close()



