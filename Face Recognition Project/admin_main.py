from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from face_recognition import face_recognition
from student_detail import student
from train import Train

class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")
        # First Image
        img1 = Image.open(r"photos\\bg1.jpg")
        img1.resize((500,130),Image.LANCZOS)
        self.Photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.Photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second Image
        img2 = Image.open(r"photos\\bg2.jpg")
        img2.resize((500,130),Image.LANCZOS)
        self.Photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.Photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Third Image
        img3 = Image.open(r"photos\\bg_3.jpg")
        img3.resize((500,130),Image.LANCZOS)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.Photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # Fourth Image
        bg = Image.open(r"photos\\login5.jpg")
        bg.resize((500,130),Image.LANCZOS)
        self.Photoimg4=ImageTk.PhotoImage(bg)

        bg_lbl=Label(self.root,image=self.Photoimg4)
        bg_lbl.place(x=0,y=130,width=1350,height=700)

        title_lab1=Label(bg_lbl,text="ADMIN PANEL",font=("times new roman",35,"bold"),bg="yellow",foreground="red")
        title_lab1.place(x=0,y=0,width=1350,height=45)

        # Student Button
        st = Image.open(r"photos\\student copy.png")
        st.resize((220,220),Image.LANCZOS)
        self.Photoimg5=ImageTk.PhotoImage(st)

        b1=Button(bg_lbl,image=self.Photoimg5,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Update Student Detail",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=self.student_details)
        b1.place(x=200,y=300,width=220,height=40)

         # Face Button
        fd = Image.open(r"photos\\face.png")
        fd.resize((220,220),Image.LANCZOS)
        self.Photoimg6=ImageTk.PhotoImage(fd)

        b1=Button(bg_lbl,image=self.Photoimg6,cursor="hand2",command=face_recognition)
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Take Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=face_recognition)
        b1.place(x=500,y=300,width=220,height=40)

         # Train Button
        td = Image.open(r"photos\\train1.png")
        td.resize((220,220),Image.LANCZOS)
        self.Photoimg7=ImageTk.PhotoImage(td)

        b1=Button(bg_lbl,image=self.Photoimg7,cursor="hand2",command=Train)
        b1.place(x=800,y=100,width=220,height=220)

        b1=Button(bg_lbl,text="Train Deta",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",foreground="white",command=Train)
        b1.place(x=800,y=300,width=220,height=40)

        b_exit=Button(bg_lbl,text="EXIT",cursor="hand2",font=("times new roman",26,"bold"),bg="black",foreground="white",command=root.destroy)
        b_exit.place(x=1150,y=450,width=150,height=50)


        # **************************Functions***********************************************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
    