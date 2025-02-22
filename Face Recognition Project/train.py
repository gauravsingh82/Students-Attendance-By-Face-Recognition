from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self):
        data_dir = ("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #grayscale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training ....",imageNP)
            cv2.waitKey(1)==13 
        ids=np.array(ids)

        # *********************** Tain Classifier *****************************
        clf =  cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifire.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed !!!")



if __name__=="__main__":
    Train()
