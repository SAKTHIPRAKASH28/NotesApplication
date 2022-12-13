from tkinter import *
from tkinter import messagebox
            
def convert():
    try:
        file1=open('history.txt','r')
        file2=open('note words.txt','r')
        file3=open('test.txt','r')
        notes=open('FinalNotes.txt','w')
        h=""
        n=""
        c=""
        for i in file1:
                h+=i
        for i in file2:
                n+=i
        for i in file3:
                c+=i
        history=h.split(",")
        words=n.split(",")
        content=c.split(".")
        final_notes=""

        indexing=1
        for i in range(len(content)):
            array=content[i].split(" ")
            for j in range(len(array)):
                if array[j] in words:
                    if(content[i]) not in final_notes:
                        temp=content[i].split(",")
                        if(len(temp)>3):
                            final_notes+="{}".format(indexing) + temp[0] +": \n"
                            for k in range(1,len(temp)):
                                if(temp[k] not in final_notes):
                                    final_notes+="->"+temp[k]+"\n"
                            indexing+=1
                        else:  
                            final_notes+="{}".format(indexing) + content[i] +"\n"
                            indexing+=1
                    else:
                        break
                elif array[j] in history:
                    if(content[i]) not in final_notes:
                        temp=content[i].split(",")
                        if(len(temp)>3):
                            final_notes+="{}".format(indexing) + temp[0] +": \n"
                            for k in range(1,len(temp)):
                                if(temp[k] not in final_notes):
                                    final_notes+="->"+temp[k]+"\n"
                            indexing+=1
                        else:  
                            final_notes+="{}".format(indexing) + content[i] +"\n"
                            indexing+=1
                    else:
                        break
                elif array[j].isnumeric():
                    if(content[i]) not in final_notes:
                        temp=content[i].split(",")
                        if(len(temp)>3):
                            final_notes+="{}".format(indexing) + temp[0] +": \n"
                            for k in range(1,len(temp)):
                                if(temp[k] not in final_notes):
                                    final_notes+="->"+temp[k]+"\n"
                            indexing+=1
                        else:  
                            final_notes+="{}".format(indexing) + content[i] +"\n"
                            indexing+=1
                    else:
                        break
                else:
                    continue
            
        notes.write(final_notes)  

        notes.close()
        file1.close()
        file2.close()
        file3.close()
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
record=Button(root,font="arial 20",text="Make Notes",bg="#111111",fg="white",border=0,command=convert).pack(pady=0)
root.mainloop()