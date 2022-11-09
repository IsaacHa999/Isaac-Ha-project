from tkinter import*
from tkinter.filedialog import*

##
def func_open():
    filename = askopenfilename(parent =window, filetypes = (("GIF 파일", "*.gif"),
                                                            ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()


##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel= Label(window, image =photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
    




'''from tkinter import*
from tkinter.filedialog import*

#
window = Tk()
window.geometry("400x100")

label1 = Label(window,text = "선택된 파일 이름")
label1.pack()

saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG파일","*jpg;*.jpeg"),("모든 파일", "*.*")))
label1.configure(text = saveFp)
saveFp.close()

window.mainloop()'''
                    
# 프로그램 1
'''from tkinter import*
from time import*

##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif"
             , "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None]*9
num = 0

##
def clickNext():
    global num
    num+=1
    if num>8:
        num =0
    photo = PhotoImage(file ="gif/" +fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image=photo

def clickPrev():
    global num
    num -=1
    if num<0:
        num =8
    photo = PhotoImage(file ="gif/" +fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image=photo

##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

photo = PhotoImage(file = "gif/" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x =250, y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=50)

    
window.mainloop()'''

## 마우스 이벤트
'''from tkinter import*
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "gif/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()'''

## 매개변수
'''from tkinter import*

#
def clickMouse(event):
    txt = ""
    if event.num ==1:
        txt += "마우스 왼쪽 버튼이("
    elif event.num ==3:
        txt += "마우스 오른쪽 버튼이("

    txt +=str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label1.configure(text = txt)

#
window =Tk()
window.geometry("400x400")
label1 =Label(window,text = "이곳이 바뀜")

window.bind("<Button>", clickMouse)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()'''
                                        
