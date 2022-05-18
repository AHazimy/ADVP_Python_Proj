from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from table import Ui_Dialog
from threading import *
import plotly.express as px
from datetime import datetime as dt
import openpyxl



class Table(QDialog):
    def __init__(self, df_det,df_conn,df_run,parent=None):
        super(Table, self).__init__(parent)       
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 
        self.df_det=df_det
        self.df_conn=df_conn
        self.df_run=df_run
        self.ui.comboBox.addItems(['StartStop_conn','StartStop_det','StartStop_run'])
        self.ui.comboBox.currentTextChanged.connect(lambda: self.show_data(self.df_det, self.df_conn, self.df_run))
        self.ui.comboBox.setCurrentIndex(2)
        self.ui.btn_show_timeline.clicked.connect(self.export_timeline_thread)
        self.ui.btn_to_excel.clicked.connect(lambda: self.export_excel(self.df_det))
    
    def export_excel(self, df_det):
        """A function that exports excel file for the detection times"""
        
        try:
            fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'EXCEL files (*.xlsx)')
            df_det.to_excel(fname[0])
            QMessageBox.information(self, "Complete", "Excel exported!")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Warning", "Enter the true path!")
            
            
    def show_data(self,df_det,df_conn,df_run):    
        """A function that show the databse in an organaized way inside the table"""
    
        try:
            if self.ui.comboBox.currentText() == "StartStop_conn":
                self.ui.tableWidget.setRowCount(0)
                tablerow=0
                for row in df_conn.index:
                    self.ui.tableWidget.insertRow(tablerow)
                    self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(df_conn['Start_Time'][row])))
                    self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(df_conn['Stop_Time'][row])))
                    tablerow+=1
            elif self.ui.comboBox.currentText() == "StartStop_det":
                self.ui.tableWidget.setRowCount(0)
                tablerow=0
                for row in df_det.index:
                    self.ui.tableWidget.insertRow(tablerow)
                    self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(df_det['Start_Time'][row])))
                    self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(df_det['Stop_Time'][row])))
                    tablerow+=1
            elif self.ui.comboBox.currentText() == "StartStop_run":
                self.ui.tableWidget.setRowCount(0)
                tablerow=0
                for row in df_run.index:
                    self.ui.tableWidget.insertRow(tablerow)
                    self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(df_run['Start_Time'][row])))
                    self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(df_run['Stop_Time'][row])))
                    tablerow+=1
        except Exception as e:
            with open('Error.txt', 'a+') as myfile:
                myfile.write("\n"+str(dt.now())+": "+str(e))


    def export_timeline_thread(self):
        """A thread will run when the show_timeline() function is called"""
        
        fname = QFileDialog.getSaveFileName(self, 'Save file', '', 'HTML files (*.html)')
        t = Thread(target=self.show_timeline, args=(str(fname[0]),self.df_run, self.df_conn, self.df_det), daemon=True)
        t.start()


    def show_timeline(self, path, df_run, df_conn, df_det):
        """A function that creates a timeline using the dataframes"""
        
        try:
            if path != '':    
                self.ui.label_timeline.setText('Saving...')
                fig_1 = px.timeline(df_run, x_start='Start_Time', x_end='Stop_Time', y="Type", color="Type",color_discrete_map={"Running":"yellow"})
                fig_1.update_yaxes(ticks="outside", tickson="boundaries", autorange="reversed", showgrid=True, showspikes=True,  linewidth=2, tickfont=dict(

                    size=18

                ))
                fig_1.update_xaxes(ticks="outside",
                                  tickson="boundaries", rangeslider_visible=True, showspikes=True, showgrid=True,  linewidth=2, title="DateTime")

                fig_1.update_layout(template="plotly_dark")
                fig_2 = px.timeline(df_conn, x_start='Start_Time', x_end='Stop_Time', y="Type", color="Type",color_discrete_map={"Connection":"green"})
                fig_3 = px.timeline(df_det, x_start='Start_Time', x_end='Stop_Time', y="Type", color="Type",color_discrete_map={"Detection":"red"})
                try:
                    fig_1.add_trace(fig_2.data[0])
                except: 
                    pass
                try:
                    fig_1.add_trace(fig_3.data[0])
                except:
                    pass
                fig_1.write_html(path)
                self.ui.label_timeline.setText('Complete!')
            else:
                self.ui.label_timeline.setText("Incorrect Path")
        except Exception as e:
            with open('Error.txt', 'a+') as myfile:
                myfile.write("\n"+str(dt.now())+": "+str(e))    