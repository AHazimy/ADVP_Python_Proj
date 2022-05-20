from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from loginUi4 import Ui_Form
import webbrowser
import sqlite3
import hashlib
import os

class Login(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        # self.Title_text()
        self.pushButton.clicked.connect(self.handleLogin)
        self.pushButton_6.clicked.connect(lambda: self.close())
        # self.exit_btn.clicked.connect(self.close)
        self.pushButton_fb.clicked.connect(lambda: webbrowser.open('http://facebook.com//')) #Enter your address
        self.pushButton_twitt.clicked.connect(lambda: webbrowser.open('http://twitter.com//')) #Enter your address
        self.pushButton_yt.clicked.connect(lambda: webbrowser.open('http://youtube.com//')) #Enter your address
        self.pushButton_in.clicked.connect(lambda: webbrowser.open('http://linkedin.com//in//')) #Enter your address
        
    
        
    def handleLogin(self):
        """A function that applies the H-MAC for the two inputs (Username and password),
        then compares them to login data stored in the database, if they matche the stored data,
        the user will be able to login into the app, else the request will be rejected"""
        
        db_files=[]
        for file in os.listdir("PasswordDB/"):
            if file.endswith(".db"):
                db_files.append(file)
        conn = sqlite3.connect("PasswordDB/"+str(db_files[0]))
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS Ident(Name VARCHAR(100), Password VARCHAR(100))")
        conn.commit()
        cur.execute("SELECT Name FROM Ident")
        users=str(cur.fetchall()).replace("[('", '').replace("',)]","")
        print(users)
        cur.execute("SELECT Password FROM Ident")
        passw=str(cur.fetchall()).replace("[('", '').replace("',)]","")
        print(passw)

        ##HASHING FOR INPUT##
        user_in=self.lineEdit.text()+"Y@1414:M@HdI1414"
        pass_in=self.lineEdit_2.text()+"Y@1414:M@HdI1414"
        user_in_hashed = hashlib.md5(user_in.encode('utf-8')).hexdigest()
        pass_in_hashed = hashlib.md5(pass_in.encode('utf-8')).hexdigest()

        print(user_in_hashed)
        print(pass_in_hashed)


        if (user_in_hashed == str(users) and
            pass_in_hashed == str(passw)):
            self.accept()
        elif (self.lineEdit.text() == '' or
            self.lineEdit_2.text() == ''):
            QMessageBox.warning(
                self, 'Warning', 'Please fill all fields before LogIn!')
        else:
            QMessageBox.warning(
                self, 'Error', 'Incorrect Username or Password!')
            
    def keyPressEvent(self, event):  
        """A function that takes a specific pressed key, and closes the window or call handleLogin() function (depending on the pressed key)"""
        
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Return:
            self.handleLogin()