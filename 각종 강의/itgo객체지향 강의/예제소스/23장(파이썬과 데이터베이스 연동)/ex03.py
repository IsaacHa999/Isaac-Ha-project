# 파이썬에서 데이터를 조회하는 프로그래밍의 순서
# 1. DB 연동
# 2. 커서 생성
# 3. 데이터 조회(select 문) : 커서를 통해서 조회를 하는데 조회된 내용은 전부 커서에
# 저장이 된다.(메모리 저장)
# 4. 조회된 내용들은 출력 : 커서를 이용하여 fetchone(), fetchall() 함수들을 통해서
# 콘솔에 출력하게 된다.
# 4. DB 연결 종료
# commit()이 빠진 이유는 조회부분이기 때문에 디스크에 저장, 삭제, 수정 이런 쿼리가 아니
# 기 때문에 commit()을 사용할 이유가 전혀 없다.

import sqlite3
# 전역변수 선언
con, cur = None, None
id, userName, email, birthYear = "", "", "", ""
row = None       # 한 행을 가져와서 저장할 전역변수
rows = None      # 전체 행을 가져와서 저장할 전역변수

if __name__ == "__main__":
    # DB 연결
    con = sqlite3.connect("c:/PythonDB/naverDB")
    # 커서 생성
    cur = con.cursor()
    cur.execute("select * from userTable")  # 조회된 데이터 전부 저장됨
    # 1990년 포함 이후에 출생한 사용자들을 출력하는 쿼리
    # cur.execute("select * from userTable where birthYear >= 1990")
    # 아래 쿼리는 출생연도 컬럼을 기준으로 오름차순 정렬을 하는 쿼리이다.
    # 단, 기본값이 asc 이기 때문에 asc 는 생략가능하다.
    # cur.execute("select * from userTable order by birthYear asc")
    # 아래 쿼리는 출생연도 컬럼을 기준으로 내림차순 정렬을 하는 쿼리이다.
    # 단, 기본값이 asc 이기 때문에 asc 는 생략가능하다.하지만, 내림차순을 하는
    # desc 생략을 하면 안된다.
    # cur.execute("select * from userTable order by birthYear desc")
    # 아래 쿼리문은 한 명만 출력해주는 쿼리문이다.
    # cur.execute("select * from userTable where id = 'john'")
    print("사용자ID    사용자이름       이메일             출생년도")
    print("--------------------------------------------------------")
    # row = cur.fetchone()   # 튜플형태로 행의 값을 리턴해준다.
    # print(row)
    # 무한루프를 돌면서 1행씩 가져와서 출력을 한다.
    while True:
        row = cur.fetchone()   # 행을 하나씩 가져온다.
        # 무한루프를 빠져나가는 상황
        if row == None:   # 더이상 가져올 데이터가 없다면 탈출
            break
        # 한 행에 있는 데이터를 각각 전역변수에 저장후 출력
        id = row[0]
        userName = row[1]
        email = row[2]
        birthYear = row[3]
        print("%5s  %15s    %15s        %5d" % (id, userName, email, birthYear))
    # 테이블 구조를 살펴보는 쿼리문
    # cur.execute("select * from sqlite_master where type = 'table'")
    # for row in cur:
    #    print(row)

    # print("전체 행을 한번에 가져오는 fetchall()함수 사용")
    # fetchall()함수를 사용하면 튜플리스트 형태로 전체 행을 반환해준다.
    # rows = cur.fetchall()
    # for data in rows:
    #     print(data)

    # DB 연결 해제
    con.close()




