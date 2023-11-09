from tkinter import*
from tkinter.filedialog import*

##
value = 0
## 
def func_open():
    global photo
    global pLabel
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일","*.gif"),("모든 파일","*.")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

def max1():
    
    global photo
    value = 2
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def min1():
    
    global photo
    value = 2
    photo = photo.subsample(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
## 메인함수
window = Tk()
window.geometry("600x600")
window.title("명화 감상하기")
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand= 1, anchor = CENTER)

btnplus = Button(window, text= "확대", command= max1)
btnminus = Button(window, text= "축소",command= min1)

btnplus.pack()
btnminus.pack()

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label="열기", command= func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '종료', command = func_exit)

window.mainloop()