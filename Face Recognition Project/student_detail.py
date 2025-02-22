from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("student details")


        # ************** Variable **************************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()
        self.var_search_box = StringVar()


        title_lab1=Label(root,text="Student Management System",font=("times new roman",35,"bold") )
        title_lab1.place(x=0,y=0,width=1530,height=55)

        main_frame=Frame(root,bd=2,bg='white')
        main_frame.place(x=10,y=66,width=1335,height=600)

        #left Lable
        Left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=580)


        img_left = Image.open(r"photos\student.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=635,height=130)


        # *******************************************************************************
        #current Course
        current_course_frame = LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=635,height=120)


        #comboBox1 Department
        dep_lable = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0 ,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("select Department","computer","civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #comboBox2 Course
        cou_lable = Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        cou_lable.grid(row=0,column=2 ,padx=10,sticky=W)

        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        cou_combo["values"]=("select Course","BCA","MCA","PGDCA")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #comboBox1 Year
        year_lable = Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lable.grid(row=1,column=0 ,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #comboBox2 Semester
        semester_lable = Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_lable.grid(row=1,column=2 ,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("select Semester","Semester I","Smester II","Smester III","Semester IV")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # *************************************************************************************************
        
        # class Student Information
        class_student_frame = LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=265,width=635,height=290)

        #student Id
        studentID_lable = Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student Name
        studentID_lable = Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #student Division
        studentID_lable = Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # student Roll Number
        studentID_lable = Label(class_student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Student Gender
        studentID_lable = Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #comboBox3 Gender
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Student DOB
        studentID_lable = Label(class_student_frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        # Student Email
        studentID_lable = Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # Student Phone Number
        studentID_lable = Label(class_student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        # Student Adderess
        studentID_lable = Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         # Class Teacher
        studentID_lable = Label(class_student_frame,text="Class Teacher:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Button
        self.var_radio1 = StringVar()
        Radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=6,column=0)

        Radiobutton2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=6,column=1)

        # Button Frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")  
        btn_frame.place(x=0,y=195,width=630,height=69)

        save_btn = Button(btn_frame,text="Save",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.add_data)
        save_btn.grid(row=0,column=0,padx=0)

        update_btn = Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.update_data)
        update_btn.grid(row=0,column=1,padx=0)

        delete_btn = Button(btn_frame,text="Delete",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.delete_data)
        delete_btn.grid(row=0,column=2,padx=0)

        reset_btn = Button(btn_frame,text="Reset",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.reset_data)
        reset_btn.grid(row=0,column=3,padx=0)

        # *****************************************************************

        btn_frame1 = Frame(class_student_frame,bd=0,relief=FLAT,bg="white")  
        btn_frame1.place(x=2,y=230,width=625,height=32)

        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.generate_dataset)
        take_photo_btn.grid(row=1,column=0,padx=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.generate_dataset)
        update_photo_btn.grid(row=1,column=1,padx=0)


        #right Frame
        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=10,width=650,height=580)

        img_right = Image.open(r"photos\student2.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=635,height=130)


        # ******************* searching System ***************************

        search_frame = LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,text="Searched Result",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=635,height=60)

        search_lable = Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_lable.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        #comboBox2 Semester
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=12)
        search_combo["values"]=("select","Student_ID","Name","Roll","Dob")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=0,sticky=W)

        search_entry = ttk.Entry(search_frame,textvariable=self.var_search_box,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=13,font=("times new roman",10,"bold"),bg="blue",fg="white",command=self.one_data)
        search_btn.grid(row=0,column=3,padx=5)

        showall_photo_btn = Button(search_frame,text="Show All",width=13,font=("times new roman",10,"bold"),bg="blue",fg="white",command=self.fetch_data)
        showall_photo_btn.grid(row=0,column=4,padx=5)

        # ************************** Table Frame *******************************

        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=635,height=350)


        #scroll Bar

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Headings
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo Status")
        self.student_table["show"]="headings"

        # Heading Width
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       


    # ********************************* Query Function *****************************************************

    def add_data(self):
        if self.var_dep.get()=='select department' or self.var_std_name.get() =="" or  self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_curser=conn.cursor()
                my_curser.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                # self.var_radio2.get()

                                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)     

       
                # *************************** Display data ********************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")   
        my_curser=conn.cursor()
        my_curser.execute("select * from student") 
        data = my_curser.fetchall() 

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    # ***************************** Search Data ****************************************************

    def one_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")   
        my_curser=conn.cursor()
        my_curser.execute(f"select * from student where {self.var_search.get()} = '{self.var_search_box.get()}'") 
        data = my_curser.fetchall() 

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    # ******************** fetch Function *********************
    def get_cursor(self,event=" "):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # ***************** Update Function ********************************
    def update_data(self):

        if self.var_dep.get()=='select department' or self.var_std_name.get() ==" " or  self.var_std_id.get()==" ":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                upadate = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if upadate>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")   
                    my_curser=conn.cursor()
                    my_curser.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                   
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get() 
                                                                                                                ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Student Details Update",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ************************ Delete Function ********************** 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page","Do You Want To Delete This Student", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")   
                    my_curser=conn.cursor()
                    sql ="delete from student where Student_ID=%s"
                    val = (self.var_std_id.get(),)
                    my_curser.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ******************** REset Function ******************
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    # **************************** Take Photo Sample ******************************************
    def generate_dataset(self):
        if self.var_dep.get()=='select department' or self.var_std_name.get() =="" or  self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")   
                my_curser=conn.cursor()
                my_curser.execute("select * from student")
                myresult=my_curser.fetchall()
                id=0
                st_id = self.var_std_id.get()
                for x in myresult:
                    id+=1
                my_curser.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(
                    
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ********************* Load predifined data **************************
                
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)  #scaling factor 1.3 , minimum neighbor = 5
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." +str(st_id) +"." +str(img_id) +".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
