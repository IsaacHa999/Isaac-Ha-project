# 문제1
# naverDB 에 productTable 을 만들고 열의 개수 4개로 하는데 구체적인 열 이름은
# pCode char(5), pName char(20), price int, amount int 와 같이 한다.
# 테이블을 만들고 난 뒤 사용자로부터 3개의 데이터를 입력을 받아서 출력한 결과는
# 아래와 같다.하여 아래와 같이 출력이 되도록 파이썬 프로그램으로 작성하시오.
# 출력 결과
# 제품코드      제품명     가격(만)   재고수량
# -----------------------------------------
# p001         노트북     110       5
# p002         마우스     3         22
# p003         키보드     2         11
# -----------------------------------------

# 풀이
import sqlite3

# 전역변수 선언 및 초기화
con, cur = None, None
pCode, pName, price, amount = "", "", "", ""

if __name__ == "__main__":
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()
    # 테이블 만들기
    cur.execute("drop table if exists productTable")
    cur.execute("create table productTable(pCode char(5), pName char(20), price int, amount int)")
    # 사용자로부터 데이터 입력 받아서 insert into 쿼리문으로 메모리에 적재시키도록 한다.
    while True:
        pCode = input("제품코드 ==> ")
        if pCode == "":
            break
        pName = input("제품명 ==> ")
        price = input("가격 ==> ")
        amount = input("재고수량 ==> ")
        # preparedStatement 방식을 이용하여 입력하기
        cur.execute("insert into productTable(pCode, pName, price, amount) values(?, ?, ?, ?)",
                   (pCode, pName, price, amount))

    cur.execute("select * from productTable")

    # while True:
    #     row = cur.fetchone()
    #     if row == None:
    #         break
    #     pCode = row[0]
    #     pName = row[1]
    #     price = row[2]
    #     amount = row[3]
    #     print("%5s  %15s    %15s    %5d" % (pCode, pName, price, amount))

    con.commit()
    con.close()