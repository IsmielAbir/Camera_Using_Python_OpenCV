'''
Camera Application using python 

Author: Md. Ismiel Hossen Abir

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.window_width = 640
        self.window_height = 400
        
        self.img_width = 640
        self.img_height = 400
        
        
        self.setWindowTitle("Philosophy Camera App")
        self.setGeometry(200,200, self.window_width, self.window_height)

        self.setFixedSize(self.window_width, self.window_height)
        
        self.ui()
        
        
        
    def ui(self):
        #container all ui
        self.image_lable = QLabel(self)
        self.image_lable.setGeometry(0,0,self.img_width, self.img_height)
        self.show()
    
    def update(self):
        #all update
        pass
    
    def save_img(self):
        #save images
        pass
    
    def record(self):
        #record images
        pass
        
        
#run

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())