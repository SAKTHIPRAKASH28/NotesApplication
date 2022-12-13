import speech_recognition as rec
from tkinter import *
from tkinter import messagebox
import time
start=time.time()
fi=open('{}.txt'.format(start),'w')
listener = rec.Recognizer()
def commandread():
    try:
        with rec.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            fi.write(command)
            fi.write("\n \n")
            fi.close() 
                       
    except:
        pass

            

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
Label(text="Enter the subject",font="arial 15 ",background="#4a4a4a",fg="white").pack()
record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=commandread).pack(pady=0)
root.mainloop()
    
