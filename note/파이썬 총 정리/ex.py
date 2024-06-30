#list
#리스트의 인덱싱과 슬라이싱

#리스트의 연산: +, *
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)
print(len(a))

#리스트의 수정, 변경, 삭제
a = [1,2,3]
a[2] = 4
print(a)
a[1:2] = ['a','b','c']
print(a)

a[1:3] = []
print(a)
del a[1]
print(a)
del a

#리스트 관련 함수
#append
a = [1,2,3] 
a.append(4)
print(a)

#sort
a = [1,4,3,2]
a.sort()
print(a)

#reverse
a = ['a','c','b']
a.reverse()
print(a)

#index
a = [1,2,3]
print(a.index(3))

#insert
a = [1,2,3]
a.insert(0,4) #0번째에 4를 삽입, 나머지는 뒤로 밀림
print(a)

#remove
a = [1,2,3,1,2,3]
a.remove(3) #첫번째로 나오는 3을 삭제
print(a)

#pop
a = [1,2,3]
print(a.pop()) #맨 마지막 요소를 꺼내고 삭제
print(a)

