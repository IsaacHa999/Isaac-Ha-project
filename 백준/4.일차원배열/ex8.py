# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

#
# hap = 0
# indx= 0
# 
##
mystr = "OOXXOOXXOO"
# mylist = []

# def sum1(n):
#     hap = 0
#     for i in range(1,n+1):
#         hap += i
#     return hap



def checking(mystr):
    score = 0
    val = 0
    for i in range(len(mystr)):
        if mystr[i] == "O":
            val +=1
            score += val 
        elif mystr[i] == "X":  #초기화
            val = 0
    print(score)

##
a = int(input());

for i in range(a):
    b = input()
    checking(b)
    