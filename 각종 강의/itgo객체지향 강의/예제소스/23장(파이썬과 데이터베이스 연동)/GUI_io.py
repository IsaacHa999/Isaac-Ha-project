# GUI(tkinter 모듈 이용) 환경을 만들어서 데이터를 입력, 출력해주는 프로그램 실습
import sqlite3
from tkinter import *
from tkinter import messagebox

# 전역 변수 선언 및 초기화
con, cur = None, None
id, userName, email, birthYear = "", "", "", ""
# "저장"버튼을 클릭했을 때, 처리하는 이벤트 핸들러 함수 insertData() 선언 및 구현
def insertData():
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()

    id = edit1.get()
    userName = edit2.get()
    email = edit3.get()
    birthYear = edit4.get()
    try:
        cur.execute("insert into userTable(id, userName, email, birthYear) values(?, ?, ?, ?)",
                    (id, userName, email, birthYear))
    except:
        messagebox.showerror("오류발생","데이터 입력 오류 발생")
    else:
        messagebox.showinfo("저장 완료","데이터 저장 완료")

    con.commit()
    con.close()

def selectData():
    strData1 = []; strData2 = []; strData3 = []; strData4 = []
    con = sqlite3.connect("c:/PythonDB/naverDB")
    cur = con.cursor()
    cur.execute("select * from userTable")
    # 위의 strData1 ~ 4까지의 초기화되어진 리스트에 데이터를 추가함
    strData1.append("사용자 ID");      strData2.append("사용자 이름")
    strData3.append("이메일");         strData4.append("출생연도")
    strData1.append("----------");    strData2.append("----------")
    strData3.append("----------");    strData4.append("----------")

    while True:
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0]);  strData2.append(row[1])
        strData3.append(row[2]);  strData4.append(row[3])

    # 조회를 재차 클릭을 했을 때 리스트 박스의 내용을 전체 삭제 후 내용 출력하게끔 함.
    listData1.delete(0, listData1.size()-1); listData2.delete(0, listData2.size()-1)
    listData3.delete(0, listData3.size()-1); listData4.delete(0, listData4.size() - 1)


    # zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 해당 객체가 담고 있는
    # 요소를 차례로 접근할 수 있게끔 반복자(iterator)를 반환한다.
    # 루프를 돌면서 각각의 해당하는 요소들의 값들을 ListBox 에 추가하고 있다.
    for id, userName, email, birthYear in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, id);      listData2.insert(END, userName)
        listData3.insert(END, email);   listData4.insert(END, birthYear)

    con.close()

if __name__ == "__main__":
    window = Tk()                       # 윈도우 생성
    window.geometry("600x300")          # 화면크기 설정
    window.title("GUI 데이터 입출력")     # 윈도우의 제목 설정

    editFrame = Frame(window)           # Frame 컨네이너를 윈도우에 생성함
    # pack()는 기본 값으로 side 매개변수에 TOP 값을 가진다.하여 위로 정렬시키면서
    # Frame 컨테이너 속의 위젯들을 중앙 배치를 해준다.
    editFrame.pack()
    # 조회결과를 출력할 Frame 컨테이너를 윈도우에 생성함.
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    # 위젯들 배치(editFrame 배치)
    # Entry 위젯에서 width 속성은 픽셀값이 아니고, 텍스트 단위임을 상기하자.
    edit1 = Entry(editFrame, width=10); edit1.pack(side=LEFT, padx=10, pady=10)
    edit2 = Entry(editFrame, width=10); edit2.pack(side=LEFT, padx=10, pady=10)
    edit3 = Entry(editFrame, width=10); edit3.pack(side=LEFT, padx=10, pady=10)
    edit4 = Entry(editFrame, width=10); edit4.pack(side=LEFT, padx=10, pady=10)

    # 데이터를 저장하는 버튼이며 insertData()를 이벤트 핸들러로 등록함.
    btnInsert = Button(editFrame, text="저장", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    # 데이터를 조회하는 버튼이며 selectData()를 이벤트 핸들러로 등록함.
    btnSelect = Button(editFrame, text="조회", command=selectData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    # listFrame 컨테이너에 ListBox 위젯을 만들어서 레이아웃 배치를 한다.
    # 리스트 박스는 여러 문자열을 위에서 아래로 나열할 때 사용하는 위젯이다.
    listData1 = Listbox(listFrame, bg="yellow")
    # pack()는 기본 값으로 side 매개변수에 LEFT 값을 주어 왼쪽 기준 정렬이 되며,
    # 할당된 공간 양쪽을 다 채우고, 할당되지 않은 미사용 공간을 현재 위젯의 할당된
    # 공간으로 변경한다.
    listData1.pack(side=LEFT, fill=BOTH, expand=1)
    listData2 = Listbox(listFrame, bg="yellow")
    listData2.pack(side=LEFT, fill=BOTH, expand=1)
    listData3 = Listbox(listFrame, bg="yellow")
    listData3.pack(side=LEFT, fill=BOTH, expand=1)
    listData4 = Listbox(listFrame, bg="yellow")
    listData4.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()


    
# 과제 : update, delete 하는 것을 함수로 정의하여 이벤트 처리하여 보자.