from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from face_recognition import face_recognition
from student_detail import student
from train import Train
from admin import AdminPage

class HomePage():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")
        # First Image
        img1 = Image.open(r"photos\\bg6.png")
        img1.resize((500,130),Image.LANCZOS)
        self.Photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.Photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img2 = Image.open(r"photos\\bg4.jpg")
        img2.resize((500,130),Image.LANCZOS)
        self.Photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.Photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Third Image
        img3 = Image.open(r"photos\\bg10.jpg")
        img3.resize((500,130),Image.LANCZOS)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.Photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # Fourth Image
        bg = Image.open(r"photos\\bg3.jpg")
        bg.resize((500,130),Image.LANCZOS)
        self.Photoimg4=ImageTk.PhotoImage(bg)

        bg_lbl=Label(self.root,image=self.Photoimg4)
        bg_lbl.place(x=0,y=130,width=1350,height=700)

        title_lab1=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",foreground="red")
        title_lab1.place(x=0,y=0,width=1350,height=45)

        # Admin Button
        st = Image.open(r"photos\\admin.png")
        st.resize((220,220),Image.LANCZOS)
        self.Photoimg5=ImageTk.PhotoImage(st)

        b1=Button(bg_lbl,image=self.Photoimg5,cursor="hand2",command=self.admin_page)
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Admin Login",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=self.admin_page)
        b1.place(x=200,y=300,width=220,height=40)

         # Face Button
        fd = Image.open(r"photos\\face2.png")
        fd.resize((220,220),Image.LANCZOS)
        self.Photoimg6=ImageTk.PhotoImage(fd)

        b1=Button(bg_lbl,image=self.Photoimg6,cursor="hand2",command=face_recognition)
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Take Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=face_recognition)
        b1.place(x=500,y=300,width=220,height=40)

        # **************************Functions***********************************************
        def register():
            title_lab2=Label(bg_lbl,font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab2.place(x=400,y=150,width=720,height=350)

            title_lab3=Label(title_lab2,text="( Help )",font=("times new roman",20,"bold"),bg="white",foreground="green")
            title_lab3.place(x=320,y=0)

            title_lab3=Label(title_lab2,text="Step 1: Click Admin Login Button.",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=30)

            title_lab3=Label(title_lab2,text="Step 2: Click On Register Button If You Are Not Register.",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=60)

            title_lab3=Label(title_lab2,text="Step 3: Fill The Sign in Form and click Sign in button.",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=90)

            title_lab3=Label(title_lab2,text="Step 4: Now Fill The Login Details and click on Submit,          \nAfter Successfully login a new window get open.",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=120)

            title_lab3=Label(title_lab2,text="Step 5: Now for click on update student details for adding details of new student - ",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=170)

            title_lab3=Label(title_lab2,text="* First Fill All The Entry and click on save button. ",font=("times new roman",13,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=100,y=200)

            title_lab3=Label(title_lab2,text="* Now Click on Take Photo Sample , and photo sample getting collected. ",font=("times new roman",13,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=100,y=225)

            title_lab3=Label(title_lab2,text="Step 6: Now Click on Train Button To Train The Model. ",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=255)

            title_lab3=Label(title_lab2,text="Step 7: After successfully Training, For Attendance Click on Take attendance button. ",font=("times new roman",14,"bold"),bg="white",foreground="blue")
            title_lab3.place(x=10,y=285)

            def destroy1():
                title_lab2.destroy()
                b_exit1.destroy()

            b_exit1=Button(bg_lbl,text="Exit Help",cursor="hand2",font=("times new roman",24,"bold"),bg="yellow",foreground="red",command=destroy1)
            b_exit1.place(x=1199,y=43,width=150,height=50)
            
         # Help Button
        td = Image.open(r"photos\\train1.png")
        td.resize((220,220),Image.LANCZOS)
        self.Photoimg7=ImageTk.PhotoImage(td)

        b1=Button(bg_lbl,image=self.Photoimg7,cursor="hand2",command=register)
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=register)
        b1.place(x=800,y=300,width=220,height=40)

        b_exit=Button(bg_lbl,text="EXIT",cursor="hand2",font=("times new roman",26,"bold"),bg="black",foreground="white",command=root.destroy)
        b_exit.place(x=950,y=450,width=150,height=50)

    def admin_page(self):
        self.new_window=Toplevel(self.root)
        self.app2=AdminPage(self.new_window)       


if __name__=="__main__":
    root=Tk()
    obj=HomePage(root)
    root.mainloop()
    