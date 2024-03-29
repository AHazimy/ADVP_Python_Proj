from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import os 
import pandas as pd
import winsound
import time
from MainWindow import Ui_MainWindow
from threading import *
from datetime import datetime as dt
import socket
from configparser import ConfigParser
import subprocess
import sqlite3
import plotly.express as px
import numpy as np
import cv2
import imutils
import base64
import hashlib
#import webbrowser
import smtplib, ssl
from PIL import Image
import json
from base64 import b64encode,b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
from Cryptodome.Random import get_random_bytes
from login_class import Login
from table_db import Table

#############To hide Console####################
# import win32gui, win32con                    #
#                                              #
# hide = win32gui.GetForegroundWindow()        #
# win32gui.ShowWindow(hide , win32con.SW_HIDE) #
################################################

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('Img/Alert.png'))
        self.thread()
        self.thread_play_alert()
        self.checkBox_theme.toggled.connect(self.themes)
        self.load_theme()   
        
        self.label_img.setPixmap(QPixmap("Img/no-camera.png"))
        
        self.stop_btn.clicked.connect(self.stop_loop)
        self.add_to_combo_sound()
        self.play_btn.clicked.connect(self.play_test_thread)
        self.checkBox_pause.toggled.connect(self.checkable_pause)
        self.start_run()
        self.btn_sql.clicked.connect(self.show_table)
        self.checkBox_email.toggled.connect(self.activate_emailBox)
       
    """We use 'global' and 'self' with variables for """
       
    global rec_conn_df
    global rec_det_df
    global rec_run_df
        
    rec_conn_df = pd.DataFrame(columns=['Start_Time', 'Stop_Time', 'Type'])

    rec_det_df = pd.DataFrame(columns=['Start_Time', 'Stop_Time', 'Type'])

    rec_run_df = pd.DataFrame(columns=['Start_Time', 'Stop_Time', 'Type'])


    rec_run_time = None

    rec_conn_value=0
    
    rec_det_value=0
    
    sound_value = 0
    
    date_list=[]
    
    temp_start_rec = None
    
    temp_start_det = None
    
    first_time_after_detection = None
    
    def load_db(self, table_name, df):
        """A function that loads the database"""
        try:    
            conn = sqlite3.connect("Report.db")
            cur = conn.cursor()
            query = cur.execute(f"SELECT * FROM {table_name}")
            cols = [column[0] for column in query.description]
            results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
            
            conn.close()
            results = pd.concat([results,df], axis=0)

            return results
        except Exception as e:
            print(str(e))
        
        
            
    
    def show_table(self):
        """A function that loads the database (using load_db()) and creates an object from class Table(),
        then show table"""
        global df_conn
        global df_det
        global df_run
        
        try:
            df_conn = self.load_db('StartStop_conn', rec_conn_df)
            df_det = self.load_db('StartStop_det', rec_det_df)
            df_run = self.load_db('StartStop_run', rec_run_df)

            if self.rec_conn_value == 1:
                df_conn.loc[len(df_conn.index), "Start_Time"] = self.temp_start_rec
                df_conn.loc[len(df_conn.index)-1, "Stop_Time"] = dt.now()
                df_conn.loc[len(df_conn.index)-1, "Type"] = "Connection"

            if self.rec_det_value == 1:
                df_det.loc[len(df_det.index), "Start_Time"] = self.temp_start_det
                df_det.loc[len(df_det.index)-1, "Stop_Time"] = dt.now()
                df_det.loc[len(df_det.index)-1, "Type"] = "Detection"

            df_run.loc[len(df_run.index), "Start_Time"] = self.rec_run_time
            df_run.loc[len(df_run.index)-1, "Stop_Time"] = dt.now()
            df_run.loc[len(df_run.index)-1, "Type"] = "Running"


            dlg = Table(df_det, df_conn, df_run)
            dlg.exec()
        except Exception as e:
            with open('Error.txt', 'a+') as myfile:
                myfile.write("\n"+str(dt.now())+": "+str(e))
    
    def start_run(self):
        """A function that saves the time when the app is oppened"""
        self.rec_run_time=dt.now()
    
    def closeEvent(self, event):
        """A function to close the app, with two options:
        if option is 'no' nothing will happen,
        if yes, all informations will be added to the database then close the app"""
        
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Are you sure you want to close the app?",
                                     QMessageBox.Yes | QMessageBox.No)
        try:
            if close == QMessageBox.Yes:
                if self.rec_conn_value == 1:
                    rec_conn_df.loc[len(rec_conn_df.index), "Start_Time"] = self.temp_start_rec
                    rec_conn_df.loc[len(rec_conn_df.index)-1, "Stop_Time"] = dt.now()
                    rec_conn_df.loc[len(rec_conn_df.index)-1, "Type"] = "Connection"
                if self.rec_det_value == 1:
                    rec_det_df.loc[len(rec_det_df.index), "Start_Time"] = self.temp_start_det
                    rec_det_df.loc[len(rec_det_df.index)-1, "Stop_Time"] = dt.now()
                    rec_det_df.loc[len(rec_det_df.index)-1, "Type"] = "Detection"

                rec_run_df.loc[len(rec_run_df.index), "Start_Time"] = self.rec_run_time
                rec_run_df.loc[len(rec_run_df.index)-1, "Stop_Time"] = dt.now()
                rec_run_df.loc[len(rec_run_df.index)-1, "Type"] = "Running"
    
                conn = sqlite3.connect("Report.db")
                cur = conn.cursor()

                cur.execute("CREATE TABLE IF NOT EXISTS StartStop_conn(Start_Time VARCHAR(100), Stop_Time VARCHAR(100), Type VARCHAR(100))")
                conn.commit()
                for ind in rec_conn_df.index:
                    cur.execute("INSERT INTO StartStop_conn( Start_Time, Stop_Time, Type) VALUES(?,?,?);", (rec_conn_df["Start_Time"][ind], rec_conn_df["Stop_Time"][ind], rec_conn_df["Type"][ind]))
                conn.commit()

                cur.execute("CREATE TABLE IF NOT EXISTS StartStop_det(Start_Time VARCHAR(100), Stop_Time VARCHAR(100), Type VARCHAR(100))")
                conn.commit()
                for ind in rec_det_df.index:
                    cur.execute("INSERT INTO StartStop_det( Start_Time, Stop_Time, Type) VALUES(?,?,?);", (rec_det_df["Start_Time"][ind], rec_det_df["Stop_Time"][ind], rec_det_df["Type"][ind]))
                conn.commit()

                cur.execute("CREATE TABLE IF NOT EXISTS StartStop_run(Start_Time VARCHAR(100), Stop_Time VARCHAR(100), Type VARCHAR(100))")
                conn.commit()
                for ind in rec_run_df.index:
                    cur.execute("INSERT INTO StartStop_run( Start_Time, Stop_Time, Type) VALUES(?,?,?);", (rec_run_df["Start_Time"][ind], rec_run_df["Stop_Time"][ind], rec_run_df["Type"][ind]))
                conn.commit()

                conn.close()

                event.accept()
            else:
                event.ignore()
                print(rec_run_df)
        except Exception as e:
            with open('Error.txt', 'a+') as myfile:
                myfile.write("\n"+str(dt.now())+": "+str(e))
            
    def add_to_combo_sound(self):
        """A function that loads the sounds (*.wav) from the '/Sound/' folder,
        and adds them to the comboBox list"""
        
        sound_files=[]
        for file in os.listdir("Sound/"):
            if file.endswith(".wav"):
                sound_files.append(str(file).replace(".wav",''))
                
        self.comboBox.addItems(sound_files)
    
    def checkable_pause(self):
        """"""
        
        if self.checkBox_pause.isChecked():
            self.spinBox_mute.setEnabled(True)
            self.label_3.setEnabled(True)
        else:
            self.spinBox_mute.setEnabled(False)
            self.label_3.setEnabled(False)
            
    
    email_value, email_date, image_to_send = 0,None,None 
                 
    def play_sound(self):
        """A function that read info from 'alertconfig.ini' and containes configurations for email,
        if theres a detection, it will send an email and play the sound (Enable Email "SecureLess" in Gmail.com to make this send email function works)"""
        print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        send_email_first_time=0
        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "example@gmail.com"  # Enter your address 
        receiver_email = configur.get('SETTING','rec_email')  # Enter receiver address
        password = '***********' #Enter your email password
        message= """From: From Person <from@fromdomain.com>
                    To: To Person <to@todomain.com>
                    Subject: Movement detected

        A movement was detected at {}.""".format(str(dt.now()))
        context = ssl.create_default_context()
        
        def send_email():
            try:
                self.email_date=dt.now()
                # test_message = Image.fromarray(self.image_to_send)
                print("Test message")
                # print(test_message)
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                global send_email_first_time
                send_email_first_time=1
                print("EMail sended")
            except Exception as e:
                print(e)
            finally:
                print("Email Not Sent")
        cond1=self.email_value == 0
        cond2=self.checkBox_email.isChecked() == True
        cond3=self.first_time_after_detection != None
        #cond4=
        while True:
            
            if self.sound_value == 1:
                
                if cond1 and cond2:
                    if send_email_first_time == 0:
                        send_email()

                    if cond3 and dt.now() > self.first_time_after_detection+pd.DateOffset(minutes=int(configur.get('SETTING', 'send_dur'))):
                        if self.checkBox_email.isChecked():
                            send_email()

                self.email_value = 1    
                if self.checkBox_pause.isChecked():
                    
                    if cond3 and dt.now() > self.first_time_after_detection+pd.DateOffset(minutes=self.spinBox_mute.value()):
                        winsound.PlaySound(r"Sound/"+str(self.comboBox.currentText()+".wav"), winsound.SND_FILENAME) 
                    time.sleep(1)  
                else:
                    winsound.PlaySound(r"Sound/"+str(self.comboBox.currentText()+".wav"), winsound.SND_FILENAME)     
                self.label.setStyleSheet('background-color:yellow')
                self.label.setText(configur.get('DETECTION','DETECT'))
                time.sleep(1)
                self.label.setStyleSheet('background-color:red')
                time.sleep(1)
            time.sleep(1)
            
            try:
                if dt.now() > self.email_date+pd.DateOffset(minutes=int(configur.get('SETTING', 'send_dur'))):
                    self.email_value=0
            except:
                continue
            
            
    def thread_play_alert(self):
        """One of the running threads at the beginning of the app"""
        
        t = Thread(target=self.play_sound, daemon=True)
        t.start()

    def start_loop(self):  
        """A function that config a UDP Client Socket,
        and test the connection with the server, then receives the images and decrypt them"""

        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        self.date_list.clear()      

        self.date_label.setText('')
        self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.label.setText(configur.get('DETECTION','NO-DETECT'))
        self.scan_label.setText('Connected to UDP Server')
        BUFF_SIZE = int(configur.get('SETTING', 'buffer'))
        UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        UDPClientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
        UDPClientSocket.setblocking(False)
        host_ip = configur.get('SETTING','IP')
        port=int(configur.get('SETTING', 'port'))
        message = b'Hello'

        PINGSTATUS = 0
        i=0
        j=0
        while True:
            response = subprocess.call("ping -n 1 " + host_ip, shell=True)
            if response == 0:
                PINGSTATUS = 1
            else:
                PINGSTATUS = 0
            if PINGSTATUS == 1:
                if self.rec_conn_value == 0:
                    self.rec_conn_value = 1
                    self.temp_start_rec = dt.now()

                try:
                    
                    UDPClientSocket.sendto(message,(host_ip,port))
                    print(configur.get('SETTING','IP'))
                    print("Sended to server again")  
                    print("Receiving from server")

                    msgFromServer_2= UDPClientSocket.recvfrom(BUFF_SIZE)
                    msgFromServer_2 = str(msgFromServer_2[0].decode('utf-8'))
                    
                    result=UDPClientSocket.recvfrom(BUFF_SIZE)

                    result=result[0].decode()

                    key=b'\xde\xe2\xd2\x04\x06o{%\x1e\x8e\x93TY: \xab'
                    try:
                        b64 = json.loads(result)
                        iv = b64decode(b64['iv'])
                        ct = b64decode(b64['ciphertext'])
                        cipher = AES.new(key, AES.MODE_CBC, iv)

                        decrypted_data = unpad(cipher.decrypt(ct), AES.block_size)

                        decrypted_data_2 = base64.b64decode(decrypted_data,' /')
                        npdata_2 = np.frombuffer(decrypted_data_2,dtype=np.uint8)
                        
                        frame_2 = cv2.imdecode(npdata_2,cv2.IMREAD_COLOR)
                        self.image_to_send = frame_2
                        print(frame_2)
                        
                        frame_2 = imutils.resize(frame_2 ,height = 480, width = 640)
                        
                        frame_2 = QImage(frame_2, frame_2.shape[1],frame_2.shape[0],frame_2.strides[0],QImage.Format_RGB888)
                    
                        self.label_img.setPixmap(QPixmap.fromImage(frame_2))
                    except Exception as e:
                        print("Error is: "+str(e))
                        continue

                    self.scan_label.setText('Scanning.'+i*str('.'))
                    
                    time.sleep(0.02)
                    if str(msgFromServer_2) == "1":
                        if self.rec_det_value == 0:
                            self.rec_det_value = 1
                            self.temp_start_det = dt.now()
                        now=dt.now()
                        self.date_list.append(now.strftime("%Y-%m-%d %H:%M:%S"))
                        self.date_label.setText(str(self.date_list[0]))
                        if self.sound_value == 0:
                            self.sound_value = 1
                            self.first_time_after_detection = dt.now()
                    elif str(msgFromServer_2) != "0":
                        self.scan_label.setText('Scanning.'+i*str('.'))
                        if self.rec_det_value == 1:
                            self.rec_det_value = 0
                            rec_det_df.loc[len(rec_det_df.index), "Start_Time"] = self.temp_start_det
                            rec_det_df.loc[len(rec_det_df.index)-1, "Stop_Time"] = dt.now() 
                            rec_det_df.loc[len(rec_det_df.index)-1, "Type"] = "Detection"
                        if self.sound_value == 0:          
                            self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
                            self.label.setText(configur.get('DETECTION','NO-DETECT'))
                            self.date_list.clear()
                    i+=1
                    if i == 4:
                        i=0
                except Exception as serror:
                    with open('Error.txt', 'a+') as myfile:
                        myfile.write("\n"+str(dt.now())+": "+str(serror))
                    self.scan_label.setText('______')
                    time.sleep(0.02)
                    continue
                
            elif PINGSTATUS == 0:
                try:
                    self.label_img.setPixmap(QPixmap("Img/no-camera.png"))    
                    if self.rec_conn_value == 1:
                        self.rec_conn_value = 0
                        rec_conn_df.loc[len(rec_conn_df.index), "Start_Time"] = self.temp_start_rec
                        rec_conn_df.loc[len(rec_conn_df.index)-1, "Stop_Time"] = dt.now()
                        rec_conn_df.loc[len(rec_conn_df.index)-1, "Type"] = "Connection"
                    if self.rec_det_value == 1:
                        self.rec_det_value = 0 
                        rec_det_df.loc[len(rec_det_df.index), "Start_Time"] = self.temp_start_det
                        rec_det_df.loc[len(rec_det_df.index)-1, "Stop_Time"] = dt.now()
                        rec_det_df.loc[len(rec_det_df.index)-1, "Type"] = "Detection"
                    self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
                    self.label.setText(configur.get('DETECTION','NO-DETECT'))
                    self.scan_label.setText('Reconnecting.'+j*str("."))
                    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    # UDPClientSocket.settimeout(5)
                    UDPClientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
                    UDPClientSocket.sendto(message,(host_ip,port))
                    j+=1
                    if j == 4:
                        j=0                    
                    time.sleep(1)
                    continue
                except:
                    continue
            
        

    def play_test(self):
        """A function to test the chosen sound"""
        
        winsound.PlaySound("Sound/"+str(self.comboBox.currentText()+".wav"), winsound.SND_FILENAME)

    def play_test_thread(self):
        """A thread that runs when the play_test() is called"""
        
        t1=Thread(target=self.play_test, daemon=True)
        t1.start()

    def stop_loop(self):
        """A function to stop the sound by making the sound checkBox checked"""
           
        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        self.sound_value = 0
        self.first_time_after_detection = dt.now()
        self.checkBox_pause.setChecked(True)
        self.label.setStyleSheet('background-color:rgb(0, 255, 0)')
        self.label.setText(configur.get('DETECTION','NO-DETECT'))
        self.scan_label.setText('Stopped')
        
        self.comboBox.setEnabled(True)
        self.play_btn.setEnabled(True)

    def thread(self):
        """One of the running threads at the beginning of the app"""
        
        t1=Thread(target=self.start_loop, daemon=True)
        t1.start()

    def load_theme(self):
        """A function that loads the dark theme status from the file 'AlertConfig.ini'"""
        
        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        theme = configur.get('THEME','DARK')
        print(theme)
        if theme == 'True':
            print("theme is true")
            self.checkBox_theme.setChecked(True)
        else:
            print("theme is false")
            self.checkBox_theme.setChecked(False)

    def themes(self):
        """A function thats save the last status of the dark theme"""
        
        configur = ConfigParser()
        configur.read('AlertConfig.ini')
        if self.checkBox_theme.isChecked() == False:
            configur.set('THEME','DARK','False')
            with open('AlertConfig.ini','w') as myfile:
                configur.write(myfile)
            self.setStyleSheet("""""")
        elif self.checkBox_theme.isChecked() == True:        
            configur.set('THEME','DARK','True')
            with open('AlertConfig.ini','w') as myfile:
                configur.write(myfile)
            self.Dark_themes()


    def Dark_themes(self):
        """A function that loads the theme from the css file"""
        
        self.setStyleSheet(open('DarkStyle.css').read())
        
    def activate_emailBox(self):
        if self.checkBox_email.isChecked() == True:
            self.label_4.setEnabled(True)
            self.label_5.setEnabled(True)
        else:
            self.label_4.setEnabled(False)
            self.label_5.setEnabled(False)

if __name__ == '__main__':
    """Create an object from Login() class, and check the username and the password,
    if they are True, the MainWindow() will be launched,
    else, nothing will happened and you should try again"""

    import sys
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
