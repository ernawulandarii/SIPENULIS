# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Record.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Sipenulis.rabin_karp as rk
import datetime
import time
import statistics
import speech_recognition as sr
import docx
import xml.etree.ElementTree as ET

from Sipenulis.loading import MovieSplashScreen
from PyQt5.QtGui import *
import mysql.connector as mdb
from PyQt5.QtWidgets import *

# from openpyxl import Workbook,load_workbook
n = 2
p = 2
student = 43
question = 5
m1 = [100, 100, 100, 100, 100, 100]
m2 = [76, 81, 92, 53, 79, 76]
m3 = [94, 65, 69, 68, 78, 75]
m4 = [98, 78, 78, 75, 87, 83]
m5 = [88, 61, 67, 68, 77, 72]
m6 = [80, 64, 71, 39, 39, 59]
m7 = [75, 63, 53, 68, 39, 60]
m8 = [66, 50, 42, 60, 34, 50]
m9 = [67, 68, 61, 28, 70, 59]
m10 = [86, 54, 80, 34, 70, 65]
m11 = [90, 25, 65, 70, 88, 68]
m12 = [85, 75, 68, 35, 59, 64]
m13 = [85, 71, 85, 75, 75, 78]
m14 = [80, 85, 80, 61, 75, 76]
m15 = [70, 70, 75, 69, 77, 72]
m16 = [75, 90, 72, 70, 75, 76]
m17 = [83, 85, 73, 60, 85, 77]
m18 = [85, 80, 65, 95, 95, 84]
m19 = [90, 50, 70, 70, 90, 74]
m20 = [80, 80, 75, 69, 75, 74]
m21 = [75, 73, 82, 67, 85, 76]
m22 = [100, 100, 100, 100, 100, 98]
m23 = [95, 84, 95, 55, 49, 94]
m24 = [95, 90, 76, 59, 75, 96]
m25 = [97, 57, 70, 75, 60, 98]
m26 = [97, 69, 68, 65, 65, 79]
m27 = [69, 66, 63, 55, 58, 79]
m28 = [75, 63, 53, 70, 32, 81]
m29 = [66, 50, 42, 60, 34, 70]
m30 = [67, 68, 61, 28, 60, 74]
m31 = [86, 54, 80, 34, 63, 37]
m32 = [75, 70, 85, 100, 75, 81]
m33 = [25, 25, 25, 85, 25, 37]
m34 = [100, 100, 90, 0, 95, 77]
m35 = [100, 80, 90, 100, 80, 90]
m36 = [75, 25, 95, 85, 85, 73]
m37 = [65, 25, 70, 25, 25, 42]
m38 = [100, 100, 100, 85, 95, 96]
m39 = [100, 55, 100, 100, 80, 87]
m40 = [95, 90, 100, 90, 95, 94]
m41 = [100, 85, 100, 95, 60, 88]
m42 = [100, 25, 100, 25, 65, 63]
m43 = [95, 90, 90, 25, 60, 72]
nilai_mahasiswa = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10,
                   m11, m12, m13, m14, m15, m16, m17, m18, m19, m20,
                   m21, m22, m23, m24, m25, m26, m27, m28, m29, m30,
                   m31, m32, m33, m34, m35, m36, m37, m38, m39, m40,
                   m41, m42, m43]
no1 = []
excel = []
list_score = []
arr_score = []
score = 0
r = sr.Recognizer()
jmlquest = 5
scores = []

test = []
class Ui_Record1Form(object):

    def setupUi(self, Record1Form):
        Record1Form.setWindowIcon(QtGui.QIcon('Images/icon.png'))

        ##################################################

        self.nowCol = 0
        # self.maxCol = len(self.index)
        # print(len(self.index))
        self.nowI = 0
        self.maxI = 5

        # tree_question
        self.tree_question = ET.parse('Soal/mbti_sorted.xml')
        self.tree_question_root = self.tree_question.getroot()
        self.questions = []
        for elem in self.tree_question_root:
            att = elem.attrib
            self.questions.append((att["id"], att["q"], att["a"], att["b"]))
        self.questions.append(["", "", "", ""])

        ##################################################

        Record1Form.setObjectName("Record1Form")
        Record1Form.resize(933, 640)

        Record1Form.showMaximized()
        Record1Form.setStyleSheet(
            """
            QWidget{background-color: rgb(25,25, 40);}
            QPushButton {
                border-style: outset;
                border-radius: 0px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #cf7500;
                border-style: inset;
            }
            QPushButton:pressed {
                background-color: #ffa126;
                border-style: inset;
            }
            """
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(Record1Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Record1Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 10, -1, 10)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_nama = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nama.sizePolicy().hasHeightForWidth())
        self.lbl_nama.setSizePolicy(sizePolicy)
        self.lbl_nama.setStyleSheet("color: rgb(231, 231, 231);\n"
                                    "font: 15pt \"Verdana\";")
        self.lbl_nama.setObjectName("lbl_nama")
        self.horizontalLayout_4.addWidget(self.lbl_nama)
        self.nameLabel = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
                                     "font: 15pt \"Verdana\";")
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_4.addWidget(self.line_4)
        self.lbl_score = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_score.sizePolicy().hasHeightForWidth())
        self.lbl_score.setSizePolicy(sizePolicy)
        self.lbl_score.setStyleSheet("color: rgb(231, 231, 231);\n"
                                     "font: 15pt \"Verdana\";")
        self.lbl_score.setObjectName("lbl_score")
        self.horizontalLayout_4.addWidget(self.lbl_score)
        self.scoreLabel = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy)
        self.scoreLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";")
        self.scoreLabel.setText("")
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.scoreLabel.hide()
        self.lbl_score.hide()
        self.horizontalLayout_4.addWidget(self.scoreLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setStyleSheet("background-color:rgb(25,25, 40);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_4.addWidget(self.line_5)
        self.line_7 = QtWidgets.QFrame(self.widget_2)
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet("background-color: rgb(25,25, 40);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_4.addWidget(self.line_7)
        self.icon = QtWidgets.QLabel(self.widget_2)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("Images/icon.png"))
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout_4.addWidget(self.icon)
        self.line_8 = QtWidgets.QFrame(self.widget_2)
        self.line_8.setStyleSheet("background-color:rgb(25,25, 40);")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_4.addWidget(self.line_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("color: rgb(231, 231, 231);\n"
                                   "font: 13pt \"Verdana\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.textQuestion = QtWidgets.QLabel(self.widget_2)
        self.textQuestion.setMinimumSize(QtCore.QSize(100, 100))
        self.textQuestion.setStyleSheet("color: rgb(231, 231, 231);\n"
                                        "font: 15pt \"Verdana\";")
        self.textQuestion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textQuestion.setText("")
        self.textQuestion.setAlignment(QtCore.Qt.AlignCenter)
        self.textQuestion.setWordWrap(True)
        self.textQuestion.setObjectName("textQuestion")
        self.verticalLayout_5.addWidget(self.textQuestion)
        self.line_6 = QtWidgets.QFrame(self.widget_2)
        self.line_6.setAutoFillBackground(False)
        self.line_6.setStyleSheet("background-color:rgb(25,25, 40);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("color: rgb(231, 231, 231);\n"
                                   "font: 12pt \"Verdana\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.textAnswer = QtWidgets.QLabel(self.widget_2)
        self.textAnswer.setMinimumSize(QtCore.QSize(100, 100))
        self.textAnswer.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";")
        self.textAnswer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textAnswer.setText("")
        self.textAnswer.setAlignment(QtCore.Qt.AlignCenter)
        self.textAnswer.setWordWrap(True)
        self.textAnswer.setObjectName("textAnswer")
        self.verticalLayout_5.addWidget(self.textAnswer)
        ##
        self.finishscoreLabel = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finishscoreLabel.sizePolicy().hasHeightForWidth())
        self.finishscoreLabel.setSizePolicy(sizePolicy)
        self.finishscoreLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
                                            "font: 13pt \"Verdana\";")
        self.finishscoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.finishscoreLabel.setObjectName("finishscoreLabel")
        self.verticalLayout_5.addWidget(self.finishscoreLabel)
        self.finishscoreLabel.hide()
        self.contentscoreLabel = QtWidgets.QLabel(self.widget_2)
        self.contentscoreLabel.setMinimumSize(QtCore.QSize(100, 300))
        self.contentscoreLabel.setStyleSheet("color: rgb(231, 231, 231);\n"
                                             "font: 14pt \"Verdana\";")
        self.contentscoreLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentscoreLabel.setText("")
        # self.contentscoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contentscoreLabel.setWordWrap(True)
        self.contentscoreLabel.setObjectName("contentscoreLabel")
        self.verticalLayout_5.addWidget(self.contentscoreLabel)
        self.contentscoreLabel.hide()
        ##
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.recordButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordButton.sizePolicy().hasHeightForWidth())
        self.recordButton.setSizePolicy(sizePolicy)
        self.recordButton.setStyleSheet("color: rgb(231, 231, 231);\n"
                                        "font: 12pt \"Verdana\";\n"
                                        "border: 2px solid rgb(255, 130, 47);;\n"
                                        "padding: 10px;\n"
                                        "border-radius: 3px;\n"
                                        "opacity: 200;\n"
                                        "")
        self.recordButton.setObjectName("recordButton")
        self.horizontalLayout_5.addWidget(self.recordButton)
        ###################################
        self.recordButton.clicked.connect(self.startRecord)
        ###################################
        self.nextButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 12pt \"Verdana\";\n"
                                      "border: 2px solid rgb(255, 130, 47);;\n"
                                      "padding: 10px;\n"
                                      "border-radius: 3px;\n"
                                      "opacity: 200;\n"
                                      "")
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)
        spacerItem5 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)

        spacerItem8 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.logoutButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setMinimumSize(QtCore.QSize(80, 30))
        self.logoutButton.setMaximumSize(QtCore.QSize(80, 50))
        self.logoutButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logoutButton.setStyleSheet("border: 2px solid  rgb(13, 58, 71);")
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout_7.addWidget(self.logoutButton)
        self.logoutButton.hide()
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Record1Form)
        QtCore.QMetaObject.connectSlotsByName(Record1Form)
        self.nextButton.hide()
        self.nextButton.clicked.connect(self.nextBtnClicked)

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.messagebox("Congrats", "Welcome " + self.name)
        # print(self.name)
        self.check()

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def check(self):
        # nameid = self.name
        connection = mdb.connect(host="localhost", user="root", password="", db="db_skripsi", port=3306,
                                 autocommit=True)
        cur = connection.cursor()
        query = "SELECT * from user where name=%s"
        data = cur.execute(query, [self.name])
        rows = cur.fetchall()
        for row in rows:
            id = int(row[0])
            time = datetime.datetime.now()
            cur.execute("UPDATE user SET last_login=%s WHERE id_user=%s", (time, id))
            myresult = connection.commit()
        print(rows)
        print(self.name)

    def startRecord(self):
        with sr.Microphone() as source:
            ini = self.questions[self.nowCol * 10 + self.nowI][1]
            print(ini)

            audio = r.listen(source)

            sample_rate_hertz = 8000
            enable_automatic_punctuation = True
            r.adjust_for_ambient_noise(source)
            movie = QMovie("Images/loading1.gif")
            splash = MovieSplashScreen(movie)
            splash.show()

            start = time.time()

            while movie.state() == QMovie.Running and time.time() < start + 2:
                QApplication.processEvents()
            try:
                test.append(r.recognize_google(audio, language="ja-JP"))
                text_output = (r.recognize_google(audio, language="ja-JP"))

                print("あなたの答えは:", test)
                self.textAnswer.setText(text_output)
                print("\n")

                self.nextButton.show()
                self.recordButton.hide()

            except:
                self.recordButton.show()
                self.nextButton.hide()
                print('Sorry.. run again...')
                self.textAnswer.setText("Sorry.. Record again...")

    def finalscore(self):
        startTime = time.time()
        accuracy = []
        paramp = []
        paramn = []

        # insert
        connection = mdb.connect(host="localhost", user="root", password="", db="db_skripsi", port=3306,
                             autocommit=True)
        cur = connection.cursor()
        query = "SELECT * from user where name=%s"
        data = cur.execute(query, [self.name])
        rows = cur.fetchall()
        for row in rows:
            id = int(row[0])
            cur.execute(
            "INSERT INTO collect_data(id_user,number_1,number_2,number_3,number_4,number_5) VALUES(%s,%s,%s,%s,%s,%s) ",
            (id, test[0], test[1], test[2], test[3], test[4]))
            myresult = connection.commit()
            # looping untuk tiap mahasiswa
            count = id

            for q in range(1, question + 1):
                prep = rk.preprocessing(test[q-1])
                # jumlah variasi kunci
                '''pada soal 1,3,4 terdapat 2 variasi kunci, pada soal 2 terdapat 3 variasi kunci,
                   pada soal 5 terdapat 7 variasi kunci'''
                if q == 1 or 3 or 4:
                    var = 2
                if q == 2:
                    var = 3
                if q == 5:
                    var = 7
                current_score = 0
                current_akurasi = 0
                # looping untuk tiap kunci
                for x in range(1, var + 1):
                    key = rk.read_txt("Key/key" + str(q) + "-" + str(x) + ".docx")
                    prep2 = rk.preprocessing(key)
                    # looping untuk tiap parameter p dan n
                    '''percobaan ini bertujuan untuk mencari tau pola nilai mahasiswa.
                       hanya bisa digunakan jika ada nilai human rater.'''
                    for p in range(2, 6):
                        if p == 2 or p % 2 == 1:
                            for n in range(2, 8):
                                rabinkarp = rk.rabin(prep, p, n)
                                rabinkarp2 = rk.rabin(prep2, p, n)
                                # similarity measurement
                                jac_measure = rk.jaccard(rabinkarp, rabinkarp2)
                                dice_measure = rk.dice(rabinkarp, rabinkarp2)
                                cos_measure = rk.cosine(rabinkarp, rabinkarp2)
                                score = cos_measure
                                print("Ngram:" + str(n) + "-" + "Prime:" + str(p))
                                selisih = abs(score - nilai_mahasiswa[count - 1][q - 1])
                                akurasi = abs(100 - ((selisih / 100) * 100))
                                print("Nomor " + str(q) + " : " + str(score))
                                # akurasi terbesar dipilih, ditampilkan nilai dan parameternya
                                temp_akurasi = akurasi
                                temp_score = score
                                #if current_score <= temp_score:
                                    #current_score = temp_score
                                    #current_akurasi = akurasi
                                    #xx = x
                                    #px = p
                                    #nx = n
                                if current_akurasi < temp_akurasi:
                                    current_akurasi = temp_akurasi
                                    current_score = score
                                    xx = x
                                    px = p
                                    nx = n
                                else:
                                    continue
                # print hasil untuk tiap nomor
                print("NOMOR " + str(q))
                print("Nilai : " + str(current_score))
                print("Akurasi : " + str(current_akurasi))
                print("Parameter (pnw) : " + (str(px) + "," + str(nx)))
                print("--------------------------------------")

                arr_score.append(current_score)
                accuracy.append(current_akurasi)
                paramp.append(px)
                paramn.append(nx)
            cur.execute("INSERT INTO parameter(id_user,n1,n2,n3,n4,n5,p1,p2,p3,p4,p5) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ", (id, paramn[0], paramn[1], paramn[2], paramn[3], paramn[4], paramp[0], paramp[1], paramp[2], paramp[3], paramp[4]))
            connection.commit()
                #a = a + 1
                # print hasil nilai total
            average = sum(arr_score) / len(arr_score)
            print("Total Skor     : " + str(average))
            self.scoreLabel.setText(str(average))
            # akurasi sistem
            acc = abs(100 - (abs(average - nilai_mahasiswa[count - 1][question]) / 100) * 100)
            print("Human Rater    : " + str(nilai_mahasiswa[count - 1][question]))
            print("Akurasi Sistem : " + str(acc))
            print("--------------------------------------\n")
            # print("Rata-rata Akurasi\t: ", round(statistics.mean(akurasi),2))
            # print("Standar Deviasi\t\t: ", round(statistics.stdev(akurasi),2))
            print("Program Execution Duration: ", (time.time() - startTime), "seconds")
            timing = round((time.time() - startTime), 3)
            self.contentscoreLabel.setText("\tTotal Score\t\t: " + str(average) +
                                           "\n\n" "\tScore Number 1\t\t: " + (str(arr_score[0])) +
                                           "\n" "\tScore Number 2\t\t: " + str(arr_score[1]) +
                                           "\n" "\tScore Number 3\t\t: " + str(arr_score[2]) +
                                           "\n" "\tScore Number 4\t\t: " + str(arr_score[3]) +
                                           "\n" "\tScore Number 5\t\t: " + str(arr_score[4]) +
                                           "\n\n" "\tProgram Execution Duration: " + str((time.time() - startTime)) + " seconds")

        # insert
        connection = mdb.connect(host="localhost", user="root", password="", db="db_skripsi", port=3306,
                                 autocommit=True)
        cur = connection.cursor()
        query = "SELECT * from user where name=%s"
        data = cur.execute(query, [self.name])
        rows = cur.fetchall()
        for row in rows:
            id = int(row[0])
            cur.execute("INSERT INTO score(id_user,score,human_rater,accuracy_rk,exec_time) VALUES(%s,%s,%s,%s,%s) ",
                        (id, average, (nilai_mahasiswa[count - 1][question]), acc, timing))
            myresult = connection.commit()
            # insert
            cur.execute(
                "INSERT INTO rabinkarp_score(id_user,score_1,hr_1,acc_1,score_2,hr_2,acc_2,score_3,hr_3,acc_3,score_4,hr_4,acc_4,score_5,hr_5,acc_5) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",
                (id, arr_score[0], (nilai_mahasiswa[count - 1][0]), accuracy[0], arr_score[1], (nilai_mahasiswa[count - 1][1]),
                 accuracy[1], arr_score[2], (nilai_mahasiswa[count - 1][2]), accuracy[2], arr_score[3], (nilai_mahasiswa[count - 1][3]),
                 accuracy[3], arr_score[4], (nilai_mahasiswa[count - 1][4]), accuracy[4]))
            myresult = connection.commit()

    def resetClicked(self):
            self.result = [0, 0, 0, 0, 0, 0, 0, 0, ""]
            self.nowCol = 0
            self.nowI = 0
            self.retranslateUi(Record1Form)

    def nextBtnClicked(self):
            self.nextButton.hide()
            self.recordButton.show()
            if self.nowI < self.maxI:
                self.nowI += 1
                self.textAnswer.setText("")

                self.textQuestion.setText(self.questions[self.nowCol * 10 + self.nowI][1])

            if self.nowI == self.maxI:
                self.finalscore()
                self.showResult()

            print(self.nowI)

    def showResult(self):
            self.label_7.hide()
            self.label_5.hide()
            self.textAnswer.hide()
            self.textQuestion.hide()
            self.recordButton.hide()
            self.nextButton.hide()
            self.scoreLabel.show()
            self.lbl_score.show()
            self.finishscoreLabel.show()
            self.contentscoreLabel.show()
            self.finishscoreLabel.setText("Your Score")

            # self.resultLabel.show()
            # self.resultLabelDesc.show()

    def retranslateUi(self, Record1Form):
            _translate = QtCore.QCoreApplication.translate
            Record1Form.setWindowTitle(_translate("Record1Form", "SIPENULIS"))
            self.lbl_nama.setText(_translate("Record1Form", "Name :"))
            self.lbl_score.setText(_translate("Record1Form", "Score :"))
            self.label_5.setText(_translate("Record1Form", "Answer The Questions"))
            self.label_7.setText(_translate("Record1Form", "Your Answer"))
            self.recordButton.setText(_translate("Record1Form", "RECORD"))
            # self.nextButton.setaText(_translate("Record1Form", "NEXT"))
            self.logoutButton.setText(_translate("Record1Form", "LOGOUT"))
            self.textQuestion.setText(_translate(
                "Record1Form", self.questions[self.nowCol * 10 + self.nowI][1]))
            self.nextButton.setText(_translate("Record1Form", "NEXT"))
            ########################################################
            self.nameLabel.setText(_translate("Record1Form", self.name))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Record1Form = QtWidgets.QWidget()
    ui = Ui_Record1Form()
    ui.setupUi(Record1Form)
    Record1Form.show()
    sys.exit(app.exec_())
