def countx(n):
    if n >= 10:
        a10 = n//10   # 십의자리 2
        a = n%10       # 일의자리 6
        sum = a10 + a  # 십의자리 + 일의자리 8
        dsum = sum%10   # sum 의 일의자리 8
        n2 = 10*a + dsum  # 68   일의자리a + 합의 일의자리dsum   68
        print("새로운 수 : %d" % n2)
        return n2
    elif n<10:  
        a10 = 0    # 0
        a = n     # 8
        sum = a10 + a  # 8
        dsum = sum 
        n2 = 10*a + dsum  # 88
        print("새로운 수 : %d" % n2)
        return n2


n = int(input())
A = n
num = 0

while True:
    n = countx(n)
    num +=1

    if A == n:
        break
    
    
print(num)