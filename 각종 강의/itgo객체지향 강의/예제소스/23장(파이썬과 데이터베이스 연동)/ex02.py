# 사용자로부터 데이터를 입력받아서 DB에 저장하는 실습
import sqlite3

# 전역 변수 선언
con, cur = None, None    # 연결자, 커서를 저장하는 변수 초기화
id, userName, email, birthYear = "", "", "", ""
sql = ""
# 메인코드 부분
if __name__ == "__main__":
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()

    # 무한루프를 돌면서 사용자로부터 데이터를 입력받는 코드
    while True:
        id = input("사용자 ID ==> ")
        # 무한루프의 탈출하는 곳 만들기
        # 사용자가 더 이상 입력을 하지 않고 엔터키를 입력한 경우에 루프를 빠져나온다.
        if id == "":
            break
        userName = input("사용자 이름 ==> ")
        email = input("이메일 ==> ")
        birthYear = input("출생연도 ==> ")
        # 사용자가 입력한 데이터를 이용하여 쿼리문 작성하는 코드
        # statement 식의 insert into 방식
        # sql = "insert into userTable values('" + id +"','" + userName +"','" + email +"'," + birthYear +")"
        # preparedStatement 식의 insert into 방식(와일드 카드 사용 방식)
        # statement 식을 이용하는 것보다 가독성이 좋다. 그리고 헤깔릴 이유가 없다.와일드
        # 카드의 갯수를 헤아려서 그에 맞는 저장할 데이터를 제공만 시켜주면 된다.(권장)
        cur.execute("insert into userTable(id, userName, email, birthYear) values(?, ?, ?, ?)",
                   (id, userName, email, birthYear))
    con.commit()

    # cur.execute("select * from userTable")
    # while True:
    #     row = cur.fetchone()
    #     if row == None:
    #         break
    #     id = row[0]
    #     userName = row[1]
    #     email = row[2]
    #     birthYear = row[3]
    #     print("%5s  %15s    %15s    %5d" % (id, userName, email, birthYear))
    con.close()

