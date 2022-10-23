'''
Camera Application using python 

Author: Md. Ismiel Hossen Abir

'''
import sys
from tkinter import Grid
from turtle import shape
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
import cv2

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.window_width = 640
        self.window_height = 400
        
        self.img_width = 640
        self.img_height = 400
        
        
        self.camera_icon = QIcon(cam_icon_path)
        
        self.setWindowTitle("Philosophy Camera App")
        self.setGeometry(200,200, self.window_width, self.window_height)

        self.setFixedSize(self.window_width, self.window_height)
        
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        
        self.ui()
        
        
        
    def ui(self):
        
        
        grid = QGridLayout()
        self.setLayout(grid)
        
        
        #container all ui
        self.image_lable = QLabel(self)
        self.image_lable.setGeometry(0,0,self.img_width, self.img_height)
        
        
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        
        self.capture_btn.setStyleSheet("border-radius:30; border: 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(60,60)
        self.capture_btn.clicked.connect(self.save_img)
        
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            
            
        grid.addWidget(self.capture_btn, 0,0)
        grid.addWidget(self.image_lable,0,1)
        
        
        self.show()
    
    def update(self):
        #all update
        
        
        _, self.frame = self.cap.read()
        
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width 
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_lable.setPixmap(QPixmap.fromImage(q_frame))
         
    
    def save_img(self):
        #save images
        cv2.imwrite('my_cap_img.jpg', self.frame)
    
    def record(self):
        #record images
        pass
        
        
#run


cam_icon_path = 'assets/camera.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())