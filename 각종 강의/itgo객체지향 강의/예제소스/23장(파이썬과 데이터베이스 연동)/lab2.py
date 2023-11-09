# 문제2
# 문제1에서 입력한 데이터 3건을 아래와 같이 출력해주는 프로그램을 작성하시오.(select문 이용)
# 출력결과
# 제품코드      제품명     가격(만)   재고수량
# -----------------------------------------
# p001         노트북     110       5
# p002         마우스     3         22
# p003         키보드     2         11
# -------------------------------------------------------------------------------
# 풀이
import sqlite3
# 전역변수 선언
con, cur = None, None
pCode, pName, price, amount = "", "", "", ""
row = None

if __name__ == "__main__":
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()

    cur.execute("select * from productTable")
    print("제품코드     제품명     가격(만)       재고수량")
    print("----------------------------------------------")

    while True:
        row = cur.fetchone()
        if row == None:
            break

        pCode = row[0]
        pName = row[1]
        price = row[2]
        amount = row[3]
        print("%5s   %7s    %7d     %10d" % (pCode, pName, price, amount))

    con.close()





