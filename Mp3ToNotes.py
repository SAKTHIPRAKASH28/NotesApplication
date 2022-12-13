import speech_recognition as sr
from tkinter import *
from tkinter import messagebox
import time
def convert():
    start=time.time()
    f=open('{}.txt'.format(start),'w')
    r=sr.Recognizer()
    name=str(duration.get())
    try:
        with sr.AudioFile('{}.wav'.format(name))as source:
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                f.write(text)
                f.close()
                messagebox.showinfo("Progress","Process Completed!")
            except:
                messagebox.showinfo("Progress","Process Failed!")
    except:
        messagebox.showinfo("Progress","FileNotFound!")


    
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
record=Button(root,font="arial 20",text="Convert",bg="#111111",fg="white",border=0,command=convert).pack(pady=0)
root.mainloop()
