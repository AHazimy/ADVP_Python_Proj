# from tracemalloc import Frame
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import cv2, time, imutils
from datetime import datetime
import pandas as pd
from MainWindow2 import Ui_MainWindow
from configparser import ConfigParser
import socket
from threading import*
import numpy as np
import base64
import hashlib
import sqlite3
import json
from base64 import b64encode,b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
from Cryptodome.Random import get_random_bytes


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('Img/Alert.png'))
        self.label_img.setPixmap(QPixmap("Img/H.png"))
        self.btn_play.clicked.connect(self.thread_play)
        self.btn_server.clicked.connect(self.thread_server)
        self.btn_apply_hash.clicked.connect(self.apply_hash)
        self.btn_export_hash.clicked.connect(self.add_hashed_to_db)
    
    check=None
    buffer=None
    img=None
    camValue=0
    Status=0
    
    def thread_server(self):
        """A thread that calls serverUDP() function when server button is clicked"""
        
        t_server = Thread(target=self.serverUDP, daemon=True)
        t_server.start()
        
    def thread_play(self):
        """A thread that calls loadImage() function when open_camera button is clicked"""
        
        t_server = Thread(target=self.loadImage, daemon=True)
        t_server.start()

    def serverUDP(self):
        """A function that configs the UDP Server Socket, and encrypt the image,
        then send it with the movement status (0 or 1) to the clients"""
        
        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        BUFF_SIZE = int(configur.get('SETTING', 'buffer'))
        Server=socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
        Server.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
        host_ip = ''
        port = int(configur.get('SETTING', 'port'))
        socket_address = (host_ip,port)
        Server.bind(socket_address)
        self.statusBar().showMessage("UDP Server is Running")
        print('Listening at:',socket_address)
        self.btn_server.setEnabled(False)
        i=0
        while True:
            msg,client_addr = Server.recvfrom(BUFF_SIZE)
            self.statusBar().showMessage("Connected to "+str(BUFF_SIZE))
            message = base64.b64encode(self.buffer)
            message_2=str(self.Status).encode('utf-8')
            i+=1
            data = b"Hello World!"
            key = b'\xde\xe2\xd2\x04\x06o{%\x1e\x8e\x93TY: \xab'
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(message, AES.block_size))
            iv =b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            result = json.dumps({'iv':iv, 'ciphertext':ct})
            result=result.encode()
            Server.sendto(message_2,client_addr)
            Server.sendto(result,client_addr)
            self.statusBar().showMessage("Server is UP")
            time.sleep(0.02)


    def loadImage(self):
        """A function that takes the image then detect the movment"""
        
        config=ConfigParser()
        config.read('AlertConfig.ini')
        contour_area=int(config.get('SETTING', 'contour'))
        
        first_frame = None
        self.statusBar().showMessage("Opening Camera...")
        status_list = [None, None]
        
        times = []
        ##To do for timeline on server with 'times' list
        # df=pd.DataFrame(columns=["Start", "End"])
        
        video = cv2.VideoCapture(0)

        self.statusBar().showMessage("Camera is opened")
        self.btn_server.setEnabled(True)
        self.btn_play.setEnabled(False)
        while self.camValue != 1: 
            check, frame = video.read()  

            self.img = frame
            self.check = check
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            self.Status=0
            gray = cv2.GaussianBlur(gray, (21,21), 0)
            if first_frame is None:
                first_frame = gray
                continue
            delta_frame = cv2.absdiff(first_frame, gray)
            thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
            (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in cnts:
                if cv2.contourArea(contour) < contour_area:
                    continue
                self.Status=1
                (x,y,w,h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
            status_list.append(self.Status)
            status_list=status_list[-2:]
            if status_list[-1]==1 and status_list[-2]==0:
                times.append(datetime.now())
            if status_list[-1]==0 and status_list[-2]==1:
                times.append(datetime.now())
            frame  = imutils.resize(frame ,height = 480, width = 640)
            encoded,self.buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,50])
            frame = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.label_img.setPixmap(QPixmap.fromImage(frame))
            time.sleep(0.02)
            print("status is: "+str(self.Status))
            
            
    def apply_hash(self):
        """A function that applies the hashfunction 'MD5' to the username and password"""
        
        key = "Y@1414:M@HdI1414"
        username=self.lineEdit_username.text()+key
        hashed_username = hashlib.md5(username.encode('utf-8')).hexdigest()
        password=self.lineEdit_password.text()+key
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.label_hashed_username.setText(hashed_username)
        self.label_hashed_password.setText(hashed_password)

    def add_hashed_to_db(self):
        """A function that exports the hashed username and password as (.db) file (sqlite)"""
        
        fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'DB file (*.db)')
        conn = sqlite3.connect(fname[0]) 
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Ident") 
        c.execute("CREATE TABLE IF NOT EXISTS Ident(Name VARCHAR(100), Password VARCHAR(100))")
        c.execute("""INSERT INTO Ident (Name, Password)
                       VALUES(?,?);""",(self.label_hashed_username.text(), self.label_hashed_password.text()))
        conn.commit()
        conn.close()
        QMessageBox.information(self, 'Done', 'Exporting password file completed!')
        
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Are you sure want to stop process?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            self.camValue=1
        else:
            event.ignore()
            
            
app = QApplication([])
window = MainWindow()
window.show()
app.exec()