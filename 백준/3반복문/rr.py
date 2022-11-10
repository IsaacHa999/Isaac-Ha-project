

def countx(n):
    if n > 10:
        a10 = n//10
        a = n%10
        sum = a10 + a
        sum = sum%10
        n2 = 10*a + sum
        print(n2)
        return n2
    elif n<10:
        a10 = 0
        a = n
        sum = a10 + A
        n2 = 10*a + sum
        return n2


n = int(input())
A = n
num = 0

while True:
    countx(n)
    n = countx(n)
    num += 1
    if A == n:
        break
    
print(num)