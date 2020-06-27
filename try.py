import sys
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Session = QtWidgets.QAction(MainWindow)
        self.actionNew_Session.setObjectName("actionNew_Session")
        self.actionSave_Session = QtWidgets.QAction(MainWindow)
        self.actionSave_Session.setObjectName("actionSave_Session")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew_Session)
        self.menuFile.addAction(self.actionSave_Session)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """Custom"""
        self.pushButton.clicked.connect(self.stress_two)
        self.pushButton_3.clicked.connect(self.stress_five)
        self.pushButton_2.clicked.connect(self.stress_one)
        self.pushButton_4.clicked.connect(self.stress_three)
        self.pushButton_5.clicked.connect(self.stress_four)
        self.actionNew_Session.triggered.connect(self.file_save)
        # /Custom"""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manual Stress Input Recorder"))
        self.label_3.setText(_translate("MainWindow", "Status"))
        self.pushButton_2.setText(_translate("MainWindow", "Stress Level 1"))
        self.pushButton.setText(_translate("MainWindow", "Stress Level 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Stress Level 3"))
        self.pushButton_5.setText(_translate("MainWindow", "Stress Level 4"))
        self.pushButton_3.setText(_translate("MainWindow", "Stress Level 5"))
        self.label_2.setText(_translate("MainWindow", "Last Recorded Stress Level"))
        self.label.setText(_translate("MainWindow", "Last Recorded Time"))
        self.label_6.setText(_translate("MainWindow", "Stress Level 0 Represents Lowest Stress Level "))
        self.label_7.setText(_translate("MainWindow", "Stress Level 1 Represents Lowest Stress Level "))
        self.label_8.setText(_translate("MainWindow", "Stress Level 2 Represents Highest Stress Level "))
        self.label_4.setText(
            _translate("MainWindow", "Please press button relevent to your stress level \"0\",\"1\" or \"2\" "))
        self.label_5.setText(_translate("MainWindow", "on screen or on keyboaard when you feel change in stress level"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew_Session.setText(_translate("MainWindow", "New Session"))
        self.actionSave_Session.setText(_translate("MainWindow", "Save Session"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        """Custom"""

    def timer(self):
        """Returns Time in DD:MM:YY::SS"""
        current = str(datetime.datetime.now().time())
        return current

    def stress_one(self):
        """Function for stress 1"""
        time_value = self.timer()
        self.label_2.setText("Last Recorded Stress: 1")
        self.label.setText("Last Recorded Time: " + time_value)
        self.save_text("1")

    def stress_two(self):
        """Function for stress 2"""
        time_value = self.timer()
        self.label_2.setText("Last Recorded Stress: 2")
        self.label.setText("Last Recorded Time: " + time_value)
        self.save_text("2")

    def stress_three(self):
        """Function for stress 3"""
        time_value = self.timer()
        self.label_2.setText("Last Recorded Stress: 3")
        self.label.setText("Last Recorded Time: " + time_value)
        self.save_text("3")

    def stress_four(self):
        """Function for stress 4"""
        time_value = self.timer()
        self.label_2.setText("Last Recorded Stress: 4")
        self.label.setText("Last Recorded Time: " + time_value)
        self.save_text("4")

    def stress_five(self):
        """Function for stress 5"""
        time_value = self.timer()
        self.label_2.setText("Last Recorded Stress: 5")
        self.label.setText("Last Recorded Time: " + time_value)
        self.save_text("5")

    def file_save(self):
        """opens save_file dialoge"""
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        file_name = dlg.getSaveFileName()
        global temp
        temp = file_name[0]
        print(temp)
        return temp

    def save_text(self, btn):
        with open(temp, 'a') as f:
            my_text = self.timer() + "\t\t\t" + btn + "\n"
            f.write(my_text)

    """ / Custom """


if __name__ == "__main__":
    """Initialization function, dunder method"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())