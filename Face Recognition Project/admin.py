from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from face_recognition import *
from student_detail import student
from train import *
from admin_main import face_recognition_system


class AdminPage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x500+0+0")
        self.root.title("Face Recognition System")


        load = Image.open('photos/log.jpg')
        photo = ImageTk.PhotoImage(load)
        label = Label(root, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = LabelFrame(root, text='Login', bg='ivory', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=150)

        Label1 = Label(border, text="Username",
                          font=("Arial Bold", 15), bg='ivory')
        Label1.place(x=50, y=20)
        Txt1 = Entry(border, width=30, bd=5)
        Txt1.place(x=180, y=20)

        Label2 = Label(border, text="Password",
                          font=("Arial Bold", 15), bg='ivory')
        Label2.place(x=50, y=80)
        TXT2 = Entry(border, width=30, show='*', bd=5)
        TXT2.place(x=180, y=80)

        def verify():
            try:
                with open("Admin_credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == Txt1.get() and p.strip() == TXT2.get():
                            self.new_window=Toplevel(self.root)
                            self.app=face_recognition_system(self.new_window)
                            i = 1
                            break
                    if i == 0:  
                        messagebox.showinfo(
                            "Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo(
                    "Error", "Please provide correct username and password!!")
                
        
        BTN1 = Button(border, text="Submit",font=("times new roman",18,"bold"),command=verify)
        BTN1.place(x=320, y=115,width=100,height=37)


        def register():
            window = Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            Label1 = Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
            Label1.place(x=10, y=10)
            txt1 = Entry(window, width=30, bd=5)
            txt1.place(x=200, y=10)

            lbl2 = Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
            lbl2.place(x=10, y=60)
            txt2 = Entry(window, width=30, show="*", bd=5)
            txt2.place(x=200, y=60)

            lbl3 = Label(window, text="Confirm Password:",
                            font=("Arial", 15), bg="deep sky blue")
            lbl3.place(x=10, y=110)
            txt3 = Entry(window, width=30, show="*", bd=5)
            txt3.place(x=200, y=110)

            def check():
                if txt1.get() != "" or txt2.get() != "" or txt3.get() != "":
                    if txt2.get() == txt3.get():
                        with open("Admin_credential.txt", "a") as f:
                            f.write(txt1.get()+","+txt2.get()+"\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                            window.destroy()
                    else:
                        messagebox.showinfo(
                            "Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo(
                        "Error", "Please fill the complete field!!")

            btn1 = Button(window, text="Sign in", font=(
                "Arial", 15), bg="#ffc22a", command=check)
            btn1.place(x=170, y=150)

            btn1_exit = Button(window, text="Exit", font=(
                "Arial", 15), bg="#ffc22a", command=window.destroy)
            btn1_exit.place(x=300, y=150)

            window.geometry("470x220")
            window.mainloop()

        BTN2 = Button(root, text="Register", bg="dark orange",font=("times new roman",20,"bold"), command=register)
        BTN2.place(x=650, y=20,width=120,height=50)

        BTN_exit = Button(root, text="EXIT", bg="dark orange",font=("times new roman",20,"bold"), command=root.destroy)
        BTN_exit.place(x=650, y=400,width=100,height=50)

        
if __name__=="__main__":
    root=Tk()
    obj=AdminPage(root)
    root.mainloop()
