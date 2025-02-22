from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class face_recognition:
    def __init__(self):
        self.face_recog()

# ************************************ Attendance ************************************************
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            my_dataList=f.readlines()
            name_list=[]
            for line in my_dataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{n},{r},{d},{dt},{d1},Present \n")
            
    def face_recog(self):
        def draw_boundary(img,classifire,scaleFactor,min_neighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifire.detectMultiScale(gray_image,scaleFactor,min_neighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name, Roll, Dep, Student_ID FROM student WHERE Student_ID = %s",(id,))
                    student_data = my_cursor.fetchone()

                    if student_data:
                        n, r, d, i = student_data

                        if confidence > 82:
                            cv2.putText(img, f"Accuracy:{confidence}%", (x, y - 115), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, "Attendance Marked", (x, y - 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                            cv2.putText(img, f"Student ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll:{r}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            self.mark_attendance(i, r, n, d)
                        else:
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                            cv2.putText(img,"UnKnown Face ??",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

                    coord=[x,y,w,h]
                
                except mysql.connector.Error as err:
                    print(f"Database error: {err}")

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifire.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            resize=cv2.resize(img,(1200,700))
            cv2.putText(img, "Press 'Enter' To Exit Camera", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255)) 
            cv2.imshow("Face Recognition",resize)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    face_recognition()
