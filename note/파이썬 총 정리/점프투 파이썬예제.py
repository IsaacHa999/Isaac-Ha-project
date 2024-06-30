#by 점프 투 파이썬 예제
def 기타필수():
    # 타입 확인
    a = 10
    type(a) # <class 'int'>

def 문자열포매팅():
    # 문자열 포매팅
    # 1. 숫자 바로 대입
    "I eat %d apples." % 3

    # 4. 2개 이상의 값 넣기
    number = 10
    day = "three"
    "I ate %d apples. so I was sick for %s days." % (number, day)

    # %s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있음
    "I have %s apples" % 3
    "rate is %s" % 3.234

    # 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 씀
    "Error is %d%%" % 98

    # format() 함수를 사용한 포매팅
    # 숫자 바로 대입
    "I eat {0} apples".format(3)

    # f 문자열 포매팅
    name = '홍길동'
    age = 30
    f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

def 문자열함수정리():
    # 문자열 관련 함수들 정리
    # count() : 문자열에서 특정 문자열이 몇 번 나오는지 알려줌
    a = "hobby"
    a.count('b')

    # find() : 문자열에서 특정 문자열이 처음으로 나온 위치를 반환
    a = "Python is the best choice"
    a.find('b')

    # index() : find()와 같은 역할을 수행하지만 찾는 문자열이 없을 때 -1이 아닌 오류를 발생시킴
    a = "Life is too short"
    a.index('t')

    # join() : 문자열을 삽입할 문자열과 함께 삽입
    ",".join('abcd')

    # upper() : 소문자를 대문자로 변환
    a = "hi"
    a.upper()

    # lower() : 대문자를 소문자로 변환
    a = "HI"
    a.lower()

    # lstrip() : 문자열 왼쪽에 있는 공백을 지움
    a = " hi "
    a.lstrip()

    # rstrip() : 문자열 오른쪽에 있는 공백을 지움
    a = " hi "

    # strip() : 문자열 양쪽에 있는 공백을 지움
    a = " hi "
    a.strip()

    # replace() : 문자열 바꾸기
    a = "Life is too short"

    # split() : 문자열 나누기
    a = "Life is too short"
    a.split()

def 리스트():
    # 리스트의 인덱싱과 슬라이싱
    a = [1,2,3]
    a[-1]  # 3

    # 리스트 연산하기 : +, *

    # 리스트의 수정, 변경, 삭제
    a = [1,2,3]
    a[2] = 4
    a[1:2] = ['a','b','c']
    a[1:3] = []
    del a[1]
    del a

    # 리스트 관련 함수들
    a = [1,2,3]
    # 조회
    a.index(3)  # 2
    len(a)
    # 추가, 삭제
    a = [1,2,3]
    a.append(4) # a = [1,2,3,4]
    a.insert(0,4)   # a = [4,1,2,3,4], 뒤로 밀림
    a.remove(3) # a = [1,2,4]
    a.pop() # a = [1,2]
    # 정렬
    a.sort()
    a.reverse()
    # 위치 반환
    a.index(3)
    # 리스트에 포함된 요소 x의 개수 세기
    a.count(3)
    # 리스트 확장
    a.extend([5,6])

def 딕셔너리():
    # 딕셔너리 쌍 추가, 삭제하기
    a = {1: 'a'}
    a[2] = 'b' # a = {1: 'a', 2: 'b'}
    del a[1]    # a = {2: 'b'}

    # 딕셔너리 관련 함수들
    a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
    # key 리스트 만들기
    a.keys()    # dict_keys(['name', 'phone', 'birth'])
    list(a.keys())  # ['name', 'phone', 'birth']
    # value 리스트 만들기
    a.values()  # dict_values(['pey', '0119993323', '1118'])
    # key, value 쌍 얻기
    a.items()   # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118'])
    
    # 조회
    a.get('name')
    a['name']  # 둘 다 'pey' 반환
    
    # 해당 key가 딕셔너리 안에 있는지 조사하기
    'name' in a

def 집합자료형():
    # 집합 자료형
    # 집합 자료형은 set 키워드를 사용해 만들 수 있음
    s1 = set([1,2,3])
    s2 = set("Hello")   # {'H','e','l','o'}
    # 중복을 허용하지 않음
    s1 = set([1,2,3,1,2,3])    # {1,2,3}
    # 순서가 없음
    s1 = set([1,2,3])   # {1,2,3}
    s2 = set("Hello")   # {'H','e','l','o'}

    # 교집합, 합집합, 차집합
    s1 = set([1,2,3,4,5,6])
    s2 = set([4,5,6,7,8,9])
    s1 & s2 # {4,5,6}
    s1.intersection(s2) # {4,5,6}
    s1 | s2 # {1,2,3,4,5,6,7,8,9}
    s1.union(s2)    # {1,2,3,4,5,6,7,8,9}
    s1 - s2 # {1,2,3}
    s1.difference(s2)   # {1,2,3}

    # 집합 자료형 관련 함수들
    s1 = set([1,2,3])
    # 값 1개 추가하기
    s1.add(4)
    # 값 여러 개 추가하기
    s1.update([5,6])
    # 특정 값 제거하기
    s1.remove(3)

    # 리스트, 튜플로 변환
    s1 = set([1,2,3])
    l1 = list(s1)   # [1,2,3], 순서가 없기 때문에 무작위로 변환
    t1 = tuple(s1)  # (1,2,3)

    # 리스트를 중복을 허용하지 않는 집합 자료형으로 변환
    l1 = [1,2,3,4,5,5,5]
    s1 = set(l1)    # {1,2,3,4,5}

def 기타필수함수():
    #type() : 자료형 확인
    type("abc")
    #len() : 길이 구하기
    len("python")
    #int() : 정수형으로 변환
    int('3')
    #str() : 문자열로 변환
    str(3)
    #dict() : 딕셔너리로 변환
    #max() : 최댓값
    #sum() : 합
    #abs() : 절댓값
    #pow() : 제곱
    #round() : 반올림
    #all() : 모두 참이면 True
    #any() : 하나라도 참이면 True
    #enumerate() : 인덱스와 값 반환
    enumerate([1,2,3]) # [(0,1),(1,2),(2,3)]
    #eval() : 문자열 수식 계산
    eval('1+2')   # 3
    #filter() : 함수를 통과한 값만 반환
    def positive(x):
        return x > 0
    list(filter(positive, [1,-3,2,0,-5,6]))  # [1,2,6]
    #map() : 모든 요소에 함수 적용
    def two_times(x):
        return x*2
    list(map(two_times, [1,2,3,4]))    # [2,4,6,8]
    #zip() : 묶어서 반환
    list(zip([1,2,3],[4,5,6])) # [(1,4),(2,5),(3,6)]
    #sorted() : 정렬
    #reversed() : 역순으로 반환
    #chr() : 아스키 코드를 문자로 변환
    chr(97) # 'a'
    #ord() : 문자를 아스키 코드로 변환
    ord('a')    # 97
    #divmod() : 몫과 나머지 반환
    divmod(7,3) # (2,1)
    #hex() : 16진수로 변환
    hex(234)    # '0xea'
    #oct() : 8진수로 변환
    oct(34) # '0o42'
    #bin() : 2진수로 변환
    bin(3) # '0b11'
    #id() : 주소값 반환
    id('a') # 140715366000048
    #open() : 파일 열기
    open('test.txt','w')   # write
    #range() : 범위 반환
    list(range(5))  # [0,1,2,3,4]

def if문설명():
    # if문
    #기본 구조
    # if 조건문:
    #     수행할 문장
    # else:
    #     수행할 문장
    
    # 연산자 and, or , not
    # if 조건문1 and 조건문2:
    #     수행할 문장

    # x in s, x not in s
    # if x in 리스트:
    #     수행할 문장
    if 1 in [1,2,3]:
        print("1이 있습니다.")
    # pass : 아무것도 하지 않음
    if 1 in [1,2,3]:
        pass
    # elif : 다양한 조건 판단
    if 'a' in ['a','b','c']:
        print("a")
    elif 'b' in ['a','b','c']:
        print("b")
    else:
        print("c")
    # 조건부 표현식
    score = 60
    message = "success" if score >= 60 else "failure"

def for문설명():
    # 전형적인 for 문
    test_list = ['one','two','three']
    for i in test_list:
        print(i)
    # 다양한 for문의 사용
    a = [(1,2),(3,4),(5,6)]
    for (first, last) in a:
        print(first + last)
    # for 문과 함께 자주 사용하는 range 함수
    for i in range(10):
        print(i)
    # 리스트 컴프리헨션 사용하기
    a = [1,2,3,4]
    result = []
    for num in a:
        result.append(num*3)
    print(result)
    # 리스트 컴프리헨션 사용
    a = [1,2,3,4]
    result = [num*3 for num in a]
    print(result)

def 함수설명() :
    # 일반적인 함수
    def add(a, b):  # a, b는 매개변수
        return a+b
    # 입력값과 결과값에 따른 함수의 형태
    # 입력값이 있고 결과값이 있는 함수
    def add(a, b):
        return a+b
    # 입력값이 없고 결과값이 있는 함수
    def say():
        return 'Hi'
    # 입력값이 있고 결과값이 없는 함수
    def add(a,b):
        print("%d, %d의 합은 %d입니다." % (a,b,a+b))
    # 입력값도 없고 결과값도 없는 함수
    def say():
        print('Hi')
    
    # 매개변수 지정하여 호출하기
    def add(a,b):
        return a+b
    result = add(a=3,b=7)
    print(result)
    # 입력값이 몇 개가 될지 모를 때
    def add_many(*args):
        result = 0
        for i in args:
            result += i
        return result
    result = add_many(1,2,3)
    print(result)
    # 키워드 파라미터 kwargs
    def print_kwargs(**kwargs):
        print(kwargs)
    print_kwargs(a=1)
    # 함수의 결과값은 언제나 하나
    def add_and_mul(a,b):
        return a+b, a*b
    result = add_and_mul(3,4)
    print(result)
    # return의 또 다른 쓰임새
    def say_nick(nick):
        if nick == '바보':
            return
        print('나의 별명은 %s입니다.' % nick)
    say_nick('야호')
    say_nick('바보')
    # 매개변수에 초깃값 미리 설정하기
    def say_myself(name, age, man=True): 
        print("나의 이름은 %s 입니다." % name) 
        print("나이는 %d살입니다." % age) 
        if man: 
            print("남자입니다.")
        else: 
            print("여자입니다.")
    say_myself("박응용", 27)
    say_myself("박응용", 27, True)

    #lambda
    add = lambda a, b: a+b
    result = add(3,4)
    print(result)

def 사용자입출력():
    # 사용자 입력과 출력
    # input : 사용자 입력
    a = input()
    # print : 사용자 출력
    print(a)
    # input 사용 시 주의사항
    number = input("숫자를 입력하세요: ")
    print(number)

def print자세히알기():
    # print 자세히 알기
    a = 123
    print(a)
    a = "Python"
    print(a)
    a = [1,2,3]
    print(a)
    print("life" "is" "too short")
    print("life"+"is"+"too short")
    print("life","is","too short")
    for i in range(10):
        print(i, end=' ')
    # 파일 객체를 이용한 출력
    f = open("test.txt",'w')
    print("life","is","too short", file=f)
    f.close()

def 파일입출력():
    # 파일 읽고 쓰기
    # 파일 생성하기
    f = open("새파일.txt",'w')
    f.close()
    # 파일을 쓰기 모드로 열어 출력값 적기
    f = open("새파일.txt",'w')
    for i in range(1,11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
    # readline() 함수 사용하기
    f = open("새파일.txt",'r')
    line = f.readline()
    print(line)
    f.close()
    # readline() 함수 사용하기
    f = open("새파일.txt",'r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    # readlines() 함수 사용하기
    f = open("새파일.txt",'r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    # read() 함수 사용하기
    f = open("새파일.txt",'r')
    data = f.read()
    print(data)
    f.close()
    # 파일에 새로운 내용 추가하기
    f = open("새파일.txt",'a')
    for i in range(11,20):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
    # with문과 함께 사용하기
    with open("foo.txt",'w') as f:
        f.write("Life is too short, you need python")
    
# 클래스 예제
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result




