# 문제3
# 문장의 한 단어의 빈도수를 계산하여 DB에 저장하고 출력하는 프로그램을 작성하시오.
# 인용할 문장 : 같같같같같같이 다하지 없이 별에도 어머니 못 했던 가난한 이웃 버리었습니다.
# 어머님, 위에도 많은 언덕 봄이 버리었습니다. 이름과, 풀이 프랑시스 흙으로 다
# 헤는 쉬이 듯듯듯듯듯합니다. 위에 흙으로 잔디가 별에도 동경과 쉬이 까닭이요, 내 있습니다.
# 무엇인지 별을 덮어 계십니다. 별 쉬이 토끼, 때 청춘이 있습니다.
# 계집애들의 별 이름과 나의 위에도 나는 내 가을로 언덕 계십니다.
# 마리아 언덕 이웃 봅니다. 하나에 청춘이 노루, 까닭입니다.
# 벌레는 강아지, 하나에 청춘이 계십니다. 하나에 이름을 흙으로 가을 보고,
# 별들을 나는 봅니다.
# 출력결과
# 단어     빈도수
# -------------
#  같        1
#  이        4 .....
# -----------------------------------------------------------------------------
# 풀이
import sqlite3
# 전역변수 선언
statement = """같같같같같같같같같같같같같같같같같같이 다하지 없이 별에도 어머니 못 했던 가난한 이웃 버리었습니다.
어머님, 위에도 많은 언덕 봄이 버리었습니다. 이름과, 풀이 프랑시스 흙으로 다 헤는 쉬이 
듯듯듯듯듯합니다. 위에 흙으로 잔디가 별에도 동경과 쉬이 까닭이요, 내 있습니다.
무엇인지 별을 덮어 계십니다. 별 쉬이 토끼, 때 청춘이 있습니다.
계집애들의 별 이름과 나의 위에도 나는 내 가을로 언덕 계십니다.
마리아 언덕 이웃 봅니다. 하나에 청춘이 노루, 까닭입니다.
벌레는 강아지, 하나에 청춘이 계십니다. 하나에 이름을 흙으로 가을 보고,
별들을 나는 봅니다."""

con, cur = None, None
oneChar, count = "", 0

if __name__ == "__main__":
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()
    cur.execute("drop table if exists countTable")
    # 컬럼이 2개, 문자, 개수
    cur.execute("create table countTable(oneChar TEXT, count INT)")

    for ch in statement:
        # ch가 한글이라면..........
        if '가' <= ch and ch <= '힣':
            # ch가 담고 있는 문자와 같은 것을 다 조회하시오
            cur.execute("select * from countTable where oneChar = ?",(ch))
            # 한 문자씩 가져온다.
            row = cur.fetchone()
            # print(row)
            # row 값이 None 이라는 것은 저장되어진 글자가 없다는 것을 의미하는 것이다.
            # 하여, None 이 반환되면 해당 글자를 DB 에 저장해야 한다.
            if row == None:
                cur.execute("insert into countTable values(?,?)",(ch,str(1)))
            # row 값이 None 이 아니라는 것은 이미 글자가 DB 에 저장되어 있다는 뜻이다.
            # 하여 count 값을 1을 증가를 시키도록 한다.
            else:
                cnt = row[1]    # 빈도수를 저장
                cur.execute("update countTable set count = ? where oneChar = ?", (str(cnt+1), ch))
    con.commit()

    # 저장된 데이터를 출력하는 코드
    cur.execute("select * from countTable order by count desc")
    print("원문\n", statement)
    print("--------------------------------------------")
    print("문자\t빈도수")
    print("--------------------------------------------")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        ch = row[0]
        cnt = row[1]
        print("%4s  %3d" % (ch, cnt))
    con.close()

