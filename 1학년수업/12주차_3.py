from tkinter import*
from tkinter import messagebox

## 함수 선언 부분#3
def keyEventUp(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + "위쪽 화살표")
    
def keyEventDown(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + "아래쪽 화살표")
    print(event.keycode)
    
def keyEventLeft(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + "왼쪽 화살표")
    print(event.keycode)

def keyEventRight(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + "오른쪽 화살표")
    print(event.keycode)
    
## 메인 코드 부분 ##
window = Tk()


window.bind("<Shift-Up>", keyEventUp)
window.bind("<Shift-Down>", keyEventDown)
window.bind("<Shift-Left>", keyEventLeft)
window.bind("<Shift-Right>", keyEventRight)


window.mainloop()
