from tkinter import *



btnlist = [None]*3

## main
window = Tk()
window.geometry("700x500")

for i in range(3):
    btnlist[i]= Button(window, text ="button"+str(i+1))
    
for i in btnlist:
    i.pack(side = TOP,expand = 1 )
    

window.mainloop()