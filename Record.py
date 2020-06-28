# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Record.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rabin_karp as rk
import datetime
import time
import statistics
import speech_recognition as sr
import docx
import xml.etree.ElementTree as ET
from loading import MovieSplashScreen
from PyQt5.QtGui import *
import mysql.connector as mdb
from PyQt5.QtWidgets import *

#from openpyxl import Workbook,load_workbook


n = 2
# w = 2
p = 2
student = 43
question = 5
human_rater = [35, 73, 36, 62, 42, 75, 90, 65, 86, 68,
               97, 57, 15, 77, 92, 97, 93, 96, 80, 87,
               88, 98, 94, 96, 98, 79, 79, 81, 70, 74,
               37, 81, 37, 77, 90, 73, 42, 96, 87, 94,
               88, 63, 72]
no1 = []
excel = []
list_score = []
arr_score = []

score = 0

r = sr.Recognizer()

test = []
jmlquest = 5

scores = []
#text = docx.Document('soal1.docx')

class Ui_RecordForm(object):

    def setupUi(self, RecordForm):

        ##################################################

        self.nowCol = 0
        #self.maxCol = len(self.index)
        #print(len(self.index))
        self.nowI = 0
        self.maxI = 5

        # tree_question
        self.tree_question = ET.parse('mbti_sorted.xml')
        self.tree_question_root = self.tree_question.getroot()
        self.questions = []
        for elem in self.tree_question_root:
            att = elem.attrib
            self.questions.append((att["id"], att["q"], att["a"], att["b"]))
        self.questions.append(["", "", "", ""])

        # tree_answer
        self.tree_answer = ET.parse('mbti_result.xml')
        self.tree_answer_root = self.tree_answer.getroot()
        self.answers = []
        for elem in self.tree_answer_root:
            att = elem.attrib
            self.answers.append((att["id"], att["answer"]))
        self.answers.append(["", ""])

        ##################################################

        RecordForm.setObjectName("RecordForm")
        RecordForm.resize(933, 640)

        RecordForm.showMaximized()
        RecordForm.setStyleSheet(
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
        self.verticalLayout = QtWidgets.QVBoxLayout(RecordForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(RecordForm)
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
        #self.contentscoreLabel.setAlignment(QtCore.Qt.AlignCenter)
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

        self.retranslateUi(RecordForm)
        QtCore.QMetaObject.connectSlotsByName(RecordForm)
        self.nextButton.hide()
        self.nextButton.clicked.connect(self.nextBtnClicked)

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.messagebox("Congrats", "Welcome " + self.name)
        #print(self.name)
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
            cur.execute("UPDATE user SET last_login=%s WHERE id_user=%s",(time,id))
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
        current_score = 0
        n = 2
        p = 2
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
        for q in range(question):

            prep = rk.preprocessing(test[q])

            kj = 1
            scores = []
            # process the student's answer document
             # delete repetitive from question, convert to romaji(if needed), filter text

            print('\nJAWABAN ', q + 1)
            # variasi kunci
            if q == 0 or 2 or 3:
                var = 2
            if q == 1:
                var = 3
            if q == 4:
                var = 7
              # read answer key documents
            # for each answer keys (from each questions):
            for x in range(1, var+1):
                pattern = rk.read_txt("key" + str(q+1) + "-" + str(x) + ".docx")
                # process answer keys
                prep2 = rk.preprocessing(pattern)  # delete repetitive from question, convert to romaji(if needed), filter text
                winnowing = rk.rabin(prep, p, n)
                winnowing2 = rk.rabin(prep2, p, n)
                # similarity measurement
                jac_measure = rk.jaccard(winnowing, winnowing2)
                dice_measure = rk.dice(winnowing, winnowing2)
                cos_measure = rk.cosine(winnowing, winnowing2)
                scores.append(cos_measure)

                # nilai terbesar dari ketiga metode pengukuran
                score = max(jac_measure, dice_measure, cos_measure)
                print("Nomor " + str(q+1) + " : " + str(score))
                temp_score = score
                if current_score <= temp_score:
                    current_score = temp_score
                else:
                    continue

                # #print all processes' results
                print('--------------------------------------')
                print('---\npreprocessing dosen\n', prep2)
                print('---\npreprocessing siswa\n', prep)
                print('---------------------------------------')
                print("\n")
                kj += 1  # loop for each answer keys

            arr_score.append(max(scores))
        totalscore = round(sum(arr_score) / len(arr_score),2)
        list_score.append(round(sum(arr_score), 2))
        akurasi = []
        ac = []
        for n in range(1, student + 1):
            average = sum(arr_score) / len(arr_score)
        print("Total Skor     : " + str(average))
        # print(average)
        # akurasi sistem
        acc = round(100 - (((abs(average - human_rater[n - 1])) / 100) * 100),2)
        akurasi.append(acc)
        #ac.append(round(max(akurasi)))

        print("======================================")
        print("======================================")
        print("Human Rater    : " + str(human_rater[n-1]))
        print("Nilai-nilai Siswa\t: ", totalscore)
        self.scoreLabel.setText(str(totalscore))
        print("Nilai per soal \t\t: ", arr_score)
        print("Akurasi Sistem \t\t: " + str(acc))
        # print("Rata-rata Akurasi\t: ", round(statistics.mean(akurasi),2))
        # print("Standar Deviasi\t\t: ", round(statistics.stdev(akurasi),2))
        print("Program Execution Duration: ", (time.time() - startTime), "seconds")
        timing = round((time.time() - startTime),2)
        self.contentscoreLabel.setText("\tTotal Score\t\t: " + str(totalscore) +
                                           "\n\n" "\tScore Number 1\t\t: " + (str(arr_score[0])) +
                                           "\n" "\tScore Number 2\t\t: " + str(arr_score[1]) +
                                           "\n" "\tScore Number 3\t\t: " + str(arr_score[2]) +
                                           "\n" "\tScore Number 4\t\t: " + str(arr_score[3]) +
                                           "\n" "\tScore Number 5\t\t: " + str(arr_score[4]) +
                                           "\n\n" "\tProgram Execution Duration: " + str(
                (time.time() - startTime)) + " seconds")

        #insert
        connection = mdb.connect(host="localhost", user="root", password="", db="db_skripsi", port=3306,
                                 autocommit=True)
        cur = connection.cursor()
        query = "SELECT * from user where name=%s"
        data = cur.execute(query, [self.name])
        rows = cur.fetchall()
        for row in rows:
            id = int(row[0])
            cur.execute("INSERT INTO score(id_user,score,accuracy_rk,exec_time) VALUES(%s,%s,%s,%s) ", (id, totalscore, acc, timing))
            myresult = connection.commit()
        # insert
            cur.execute(
                "INSERT INTO rabinkarp_score(id_user,score_1,score_2,score_3,score_4,score_5,accuracy_rk,human_rater) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ",
                (id, arr_score[0], arr_score[1], arr_score[2], arr_score[3], arr_score[4], acc, human_rater[n-1]))
            myresult = connection.commit()



    def resetClicked(self):
        self.result = [0, 0, 0, 0, 0, 0, 0, 0, ""]
        self.nowCol = 0
        self.nowI = 0
        self.retranslateUi(RecordForm)

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

    def retranslateUi(self, RecordForm):
        _translate = QtCore.QCoreApplication.translate
        RecordForm.setWindowTitle(_translate("RecordForm", "Form"))
        self.lbl_nama.setText(_translate("RecordForm", "Name :"))
        self.lbl_score.setText(_translate("RecordForm", "Score :"))
        self.label_5.setText(_translate("RecordForm", "Answer The Questions"))
        self.label_7.setText(_translate("RecordForm", "Your Answer"))
        self.recordButton.setText(_translate("RecordForm", "RECORD"))
        #self.nextButton.setText(_translate("RecordForm", "NEXT"))
        self.logoutButton.setText(_translate("RecordForm", "LOGOUT"))
        self.textQuestion.setText(_translate(
            "RecordForm", self.questions[self.nowCol*10+self.nowI][1]))
        self.nextButton.setText(_translate("RecordForm", "NEXT"))
        ########################################################
        self.nameLabel.setText(_translate("RecordForm", self.name))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecordForm = QtWidgets.QWidget()
    ui = Ui_RecordForm()
    ui.setupUi(RecordForm)
    RecordForm.show()
    sys.exit(app.exec_())
