# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector
import rabin_karp as rk
import time
import statistics
import speech_recognition as sr
import docx
from getch import pause_exit
#from openpyxl import Workbook,load_workbook


mydb=mysql.connector.connect(host="localhost",user="root",password="",database="db_skripsi")




class Ui_RecordForm(object):
    def __init__(self):

            startTime = time.time()
            n = 2
            # w = 2
            p = 2
            student = 1
            question = 2
            jmlquest = 2
            human_rater = [35, 73, 36, 62, 42, 75, 90, 65, 86, 68, 97, 57, 15, 77, 92, 97, 93, 96, 80, 87, 88, 98, 94,
                           96, 98, 79,
                           79, 81, 70, 74, 37, 81, 37, 77, 90, 73, 42, 96, 87, 94, 88, 63, 72]
            no1 = []
            excel = []
            list_score = []
            text = docx.Document('soal1.docx')

            for count in range(1, student + 1):
                    print(
                            '===========================================================================================================')
                    print("MAHASISWA", count, "\n")
                    arr_score = []
                    current_score = 0
                    score = 0
                    # doc = ps.read_txt("mahasiswa" + str(count) + ".docx")

                    test = []
                    r = sr.Recognizer()
                    # jmlquest = int(input("Masukan jumlah soal\n"))
                    print("Jawablah pertanyaan berikut ini")

                    with sr.Microphone() as source:
                            for i in range(jmlquest):
                                    a = text.paragraphs[i].text
                                    #self.textQuestion.setText(a)
                                    print(a)
                                    input("Press Enter to answer...")
                                    audio = r.listen(source)
                                    sample_rate_hertz = 8000
                                    enable_automatic_punctuation = True
                                    r.adjust_for_ambient_noise(source)

                                    try:
                                            test.append(r.recognize_google(audio, language="ja-JP"))
                                            print("あなたの答えは:", test)
                                            print("\n")

                                    except:
                                            print('Sorry.. run again...')

                    for q in range(0, question):
                            kj = 1
                            scores = []

                            # process the student's answer document
                            prep = rk.preprocessing(test[
                                                            q])  # delete repetitive from question, convert to romaji(if needed), filter text
                            # prep = ps.winnow(test[q])

                            print('\nJAWABAN ', q + 1)

                            pattern = rk.read_txt("jwbDosen" + str(q + 1) + ".docx")  # read answer key documents
                            # for each answer keys (from each questions)
                            for x in range(0, len(pattern)):
                                    # process answer keys
                                    prep2 = rk.preprocessing(pattern[
                                                                     x])  # delete repetitive from question, convert to romaji(if needed), filter text
                                    winnowing = rk.winnow(prep, p, n)
                                    winnowing2 = rk.winnow(prep2, p, n)
                                    # similarity measurement
                                    jac_measure = rk.jaccard(winnowing, winnowing2)
                                    dice_measure = rk.dice(winnowing, winnowing2)
                                    cos_measure = rk.cosine(winnowing, winnowing2)
                                    scores.append(cos_measure)
                                    # print("jaccard : " + str(jac_measure) + " | dice : " + str(dice_measure) + " | cosine : " + str(cos_measure))
                                    # nilai terbesar dari ketiga metode pengukuran
                                    score = max(jac_measure, dice_measure, cos_measure)
                                    temp_score = score
                                    if current_score <= temp_score:
                                            current_score = temp_score
                                    else:
                                            continue

                                    # #print all processes' results
                                    print('----------------')
                                    print('KUNCI JAWABAN ' + str(kj))
                                    print('---\npreprocessing dosen\n', prep2)
                                    # print('---\ntdm kj\n', tdmkj)
                                    print('---\npreprocessing siswa\n', prep)
                                    # print('---\ntdm student\n', tdms)
                                    # print('---\nSVD KJ: ', svdkj, "SVD S: ", svds, "Nilai KJ ke-", kj, ": ", frobnorm)
                                    # print('---\nSVD S: ', svds)
                                    # print('---\nNilai KJ ke-', kj, '\t: ', frobnorm)

                                    kj += 1  # loop for each answer keys
                            # # print score of each questions (maximum score from list of each key answers' score)
                            # print('\n\nNilai Soal Nomor', q + 1,'\t: ', max(scores), '\n--------------------------')
                            # add the score of each questions to list of scores of each students
                            arr_score.append(max(scores))
                            # excel.append(max(scores))
                    # # print students' score (sum of scores from each questions)
                    # print('\n\nNILAI MAHASISWA ', count, '\t: ', round(sum(arr_score),2))
                    list_score.append(round(sum(arr_score), 2))
                    akurasi = []
                    for n in range(student):
                            acc = round((100 - (((abs(list_score[n] - human_rater[n])) / 100) * 100)), 2)
                            akurasi.append(acc)
                    print("=========================================="
                          "=================================================================")
                    # print("Human Rater\t\t\t: ", human_rater)
                    print("Nilai-nilai Siswa\t: ", list_score)
                    print("Nilai per soal \t\t: ", arr_score)
                    # print("Akurasi\t\t\t\t: ", akurasi)
                    # print("Rata-rata Akurasi\t: ", round(statistics.mean(akurasi),2))
                    # print("Standar Deviasi\t\t: ", round(statistics.stdev(akurasi),2))
                    print("Program Execution Duration: ", (time.time() - startTime), "seconds")

                    pause_exit(status=0, message='Press any key to exit.')

            # create excel file of the data
            # wb = Workbook()                                             # Workbook is created
            # wb = load_workbook('data.xlsx')
            # sheet1 = wb.create_sheet("Test")                  # add_sheet is used to create sheet.
            # for n in range(1, 43):
            # for o in range(len(excel)):
            #     for m in range(2,6):
            #         sheet1.cell(row=n, column=1, value=n)
            #         sheet1.cell(row=n, column=m, value=excel[o])
            # for n in range(len(human_rater)):
            # sheet1.cell(row=1, column=1, value='Siswa')
            # sheet1.cell(row=1, column=2, value='Human Rater Score')
            # sheet1.cell(row=1, column=3, value='Simple-O Score')
            # sheet1.cell(row=1, column=4, value='Accuracy')
            # sheet1.cell(row=n+2, column=1, value=n)
            # sheet1.cell(row=n+2, column=2, value=human_rater[n])
            # sheet1.cell(row=n+2, column=3, value=list_score[n])
            # sheet1.cell(row=n+2, column=4, value=akurasi[n])
            # wb.save('data.xlsx')

    def setupUi(self, RecordForm):
        RecordForm.setObjectName("RecordForm")
        RecordForm.resize(933, 640)
        RecordForm.setStyleSheet(".QWidget{background-color: rgb(25,25, 40);}")
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
        self.icon.setPixmap(QtGui.QPixmap("../../SKRIPSI NEW/Images/icon.png"))
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
        self.textQuestion = QtWidgets.QTextBrowser(self.widget_2)
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
        self.textAnswer = QtWidgets.QTextBrowser(self.widget_2)
        self.textAnswer.setObjectName("textAnswer")
        self.verticalLayout_5.addWidget(self.textAnswer)
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
        self.stopButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 12pt \"Verdana\";\n"
"border: 2px solid rgb(255, 130, 47);;\n"
"padding: 10px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)
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
        self.finishButton = QtWidgets.QPushButton(self.widget_2)
        self.finishButton.setStyleSheet("color: rgb(231, 231, 231);\n"
"font: 12pt \"Verdana\";\n"
"border: 2px solid rgb(255, 130, 47);;\n"
"padding: 10px;\n"
"border-radius: 3px;\n"
"opacity: 200;\n"
"")
        self.finishButton.setObjectName("finishButton")
        self.horizontalLayout_8.addWidget(self.finishButton)
        spacerItem8 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.logoutButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setMinimumSize(QtCore.QSize(50, 20))
        self.logoutButton.setMaximumSize(QtCore.QSize(50, 50))
        self.logoutButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logoutButton.setStyleSheet("background-color: rgb(13, 58, 71);\n"
"\n"
"border: 2px solid  rgb(13, 58, 71);")
        self.logoutButton.setObjectName("logoutButton")
        self.verticalLayout_7.addWidget(self.logoutButton)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(RecordForm)
        QtCore.QMetaObject.connectSlotsByName(RecordForm)

    def retranslateUi(self, RecordForm):
        _translate = QtCore.QCoreApplication.translate
        RecordForm.setWindowTitle(_translate("RecordForm", "Form"))
        self.lbl_nama.setText(_translate("RecordForm", "Name :"))
        self.lbl_score.setText(_translate("RecordForm", "Score :"))
        self.label_5.setText(_translate("RecordForm", "Answer The Questions"))
        self.textQuestion.setHtml(_translate("RecordForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("RecordForm", "Your Answer of Number "))
        self.recordButton.setText(_translate("RecordForm", "Record"))
        self.stopButton.setText(_translate("RecordForm", "Stop"))
        self.finishButton.setText(_translate("RecordForm", "Finish"))
        self.logoutButton.setText(_translate("RecordForm", "LOGOUT"))
        self.textQuestion.setText(self.a)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecordForm = QtWidgets.QWidget()
    ui = Ui_RecordForm()
    ui.setupUi(RecordForm)
    RecordForm.show()
    sys.exit(app.exec_())
