from tkinter import *

def stop():
    root.destroy()
#-----window configuration-----
root =Tk()
root.geometry("400x100")
root.title('Calculate FreeFall')
root.config(background='#ffffff')
root.resizable(False,False)

#Setting Header
heading = Label(text="Ingresa la altura.",bg="black",fg="white", width="400", height="1")
heading.pack()
#-----window configuration-----

#-----Data Request-----
height_text = Label(text="Altura",)
height_text.place(x="90",y="40")

height_ = IntVar()


height_entry = Entry(textvariable = height_, width = "20")
height_entry.place(x="140",y="38")

submit = Button(root,text="Submit", width="10",height="1" ,command=stop)
submit.place(x ="140",y="65")
root.mainloop()
#-----Data Request-----

