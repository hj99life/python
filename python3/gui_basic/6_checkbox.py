from tkinter import * 

root = Tk()
root.title("TKINTER GUI")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
#chkbox.select()
#chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) 
    


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()