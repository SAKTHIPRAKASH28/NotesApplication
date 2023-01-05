
from tkinter import *
from tkinter import messagebox
import requests


def convert():
    file2= open("{}_converted.txt".format(duration.get()),'w')
    try:
        file1= open("{}.txt".format(duration.get()),'r')
        
        content=""
        for i in file1:
            content+=i
    


        url = "http://bark.phon.ioc.ee/punctuator"
        x = requests.post(url, params={"text": content})
        con=x.text
        file2.write(con)
        file1.close()
        file2.close()
        messagebox.showinfo("Alert!","Done!")
    except:
       messagebox.showinfo("Alert!","File Not Found!")





    
root=Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Notes Application")
root.configure(background="#4a4a4a")
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False,image_icon)
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(padx=5,pady=5)

Label(text="Notes Application",font="arial 30 bold",background="#4a4a4a",fg="white").pack()
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15).pack(pady=10)
Label(text="Enter the filename",font="arial 15 ",background="#4a4a4a",fg="white").pack()
record=Button(root,font="arial 20",text="Punctuate",bg="#111111",fg="white",border=0,command=convert).pack(pady=0)
root.mainloop()