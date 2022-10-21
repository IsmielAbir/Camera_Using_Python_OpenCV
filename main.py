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
        self.setWindowTitle("Philosophy Camera App")
        self.setFixedSize(self.window_width, self.window_height)
        
        
        
    def ui(self):
        #container all ui
        pass
    
    def update(self):
        #all update
        pass
    
    def save_img(self):
        #save images
        pass
    
    def record(self):
        #record images
        pass
        