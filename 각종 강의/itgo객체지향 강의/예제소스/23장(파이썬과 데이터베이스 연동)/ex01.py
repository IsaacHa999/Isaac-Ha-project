# 데이터의 입력에 대한 실습
# 파이썬에서 데이터를 입력하는 프로그래밍 순서
# 1. 데이터베이스에 연결(연결자 = sqlite3.connect("DB이름")
# 2. 커서 생성(데이터 입출력 통로, 커서이름 = 연결자.cursor())
# 3. 테이블 만들기(이미 만들어져 있다면 생략이 가능, 커서이름.execute("create table"))
# 4. 데이터 입력(커서 이름.execute("insert into")
# 5. 입력한 데이터를 물리적인 공간에 저장(연결자.commit())
# 6. 데이터베이스(리소스) 닫기(연결자.close())

import sqlite3       # sqlite3 모듈 가져오기
# sqlite 로 직접 접속해서 만든 naverDB 와 다른 naverDB 인 것을 잊지 않도록 한다.
con = sqlite3.connect("c:/PythonDB/naverDB")    # DB 연결
# print(con)   # 객체의 주소가 리턴
# 커서 생성
cur = con.cursor()
# print(cur)
# 아래 코드는 테이블을 한번 만들고 난 뒤 재차 실행시키면 테이블이 존재한다라는
# 에러를 발생시킨다.
# 1번째 해결방법
cur.execute("drop table if exists userTable")  # 기존 테이블 삭제
# id 는 중복가능하면 안되는 컬럼이므로 PK로 설정한다.(중복 허용방지, 
# 자동정렬은 되질 않는다.--> 오라클이나 MySQL 에서 PK를 설정하면 PK를 기준으로 자동정렬 됨)
cur.execute("create table userTable(id char(4) PRIMARY KEY, userName char(15),"
            "email char(15), birthYear int)")
# 아래 코드는 userTable 라는 테이블이 존재하지 않는다면 만들고 있다면 만들지 않고
# 에러를 발생시키지 않는다.
# 2번째 해결방법
# cur.execute("create table if not exists userTable(id char(4), userName char(15),"
#             "email char(15), birthYear int)")
# 테이블이 제대로 만들어졌는지 확인하는 쿼리문
# cur.execute("select name from sqlite_master where type='table';")
# print(cur.fetchall())

# 데이터 4건을 메모리에 올리고 있다.
cur.execute("insert into userTable values('john','john Bann','john@naver.com',1990)")
cur.execute("insert into userTable values('kim','Kim Chi','kim@daum.net',1992)")
cur.execute("insert into userTable values('lee','Lee Pal','lee@paran.com',1988)")
cur.execute("insert into userTable values('park','Park Su','park@gmail.com',1980)")

# 위와 같이 데이터를 insert into 를 통해서 입력했다고 하더라도 어디까지나
# 메모리(RAM)에 존재한다는 것이다.하여 물리적 디스크(서버단)에 완전히 저장
# 하고자 한다면 커밋(commit)을 해야 한다.
con.commit()
con.close()    # DB 연동 해제