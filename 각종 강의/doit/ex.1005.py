def func1(a,b):
    c = a.split()
    b = b.split()
    b1 = b[0]; b2 = b[1]
    
    for i in range(0,len(c)-1):
        if c[i] == b1:
            c[i] = "*" * len(b1)
        elif c[i] == b2:
            c[i] = "*" * len(b2)
    return " ".join(c)


a = "문자열을 입력하시오. : "
b = "금칙어를 입력하시오. : "

print(func1(a,b))
