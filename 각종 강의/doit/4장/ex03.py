# # 05
# avg =0
# sum = 0

# A = [70,60,55,75,95,80,85,100]
# for i in A:
#     sum +=i
# avg = sum / len(A)

# print(avg)

# ##06
# numbers = [1,2,3,4,5]

# result= [(n*2) for n in numbers if n % 2 == 1]
# print(result)

# # for n in numbers:
# #     if n % 2 == 1:
# #         result.append(n*2)
# # print(result)


numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n %2 != 0]
print(result)