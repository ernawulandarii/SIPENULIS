# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from Record import Ui_RecordForm
import mysql.connector as mdb
import hashlib
from User import User
import json
import datetime
import icons_rc  # pylint: disable=unused-import
from customized import PasswordEdit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):

    def DBConnection(self):
        try:
            conn = mdb.connect(host="127.0.0.1",
   port="3306",
   user="root",
   passwd="",
   database="db_skripsi"
)
            self.warning("Connection", "Database Connected Successfully")
        except mdb.Error as e:
               self.warning("Connection", "Failed To Connect Database")

    def messagebox(self,title, message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def warning(self,title, message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def loginCheck(self, name):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        salt = "SkR1PsIQ%%@"
        db_password = password + salt
        h = hashlib.md5(db_password.encode())
        passwordhash = h.hexdigest()
        #connection = sqlite3.connect("login.db")
        connection=mdb.connect(host="localhost", user="root", password="", db="db_skripsi",port=3306,autocommit=True)
        cur=connection.cursor()
        query = "SELECT * FROM user where username=%s AND password=%s"
        data=cur.execute(query,(username,passwordhash))
        rows = cur.fetchall()
        if (len(rows) > 0):
             for row in rows:
                 id = int(row[0])
                 roles = row[1]
                 name = row[2]
                 usern = row[3]
                 passw = row[4]
                 time = row[5]
                 obj_user = User(id, roles, name, usern, passw, time)
                 jsondata = obj_user.to_dict_set()
                 jsdata = json.dumps(jsondata, indent=4, sort_keys=True, default=str)
                 js_data = json.loads(jsdata)
                 #self.messagebox("Congrats", "Welcome "+ name)
                 self.recordForm = QtWidgets.QWidget()
                 self.ui = Ui_RecordForm(name)
                 self.ui.setupUi(self.recordForm)
                 self.recordForm.show()

                 Dialog.close()


        else:
            self.warning("Warning", "Invalid Username And Password")

    def setupUi(self, Form):
        """Setup the login form.
        """

        Form.setObjectName("Form")
        Form.resize(475, 562)
        # remove the title bar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        Form.setStyleSheet(
            """
             QPushButton{
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

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet(".QWidget{background-color: rgb(20,20, 40);}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        '''
        self.login_btn_3 = QtWidgets.QPushButton(self.widget)
        self.login_btn_3.setMinimumSize(QtCore.QSize(35, 25))
        self.login_btn_3.setMaximumSize(QtCore.QSize(35, 25))
        self.login_btn_3.setStyleSheet("color: white;\n"
                                        "font: 13pt \"Verdana\";\n"
                                        "border-radius: 1px;\n"
                                        "opacity: 200;\n")
        self.login_btn_3.clicked.connect(self.close)

        self.verticalLayout_2.addWidget(self.login_btn_3, 0, QtCore.Qt.AlignRight)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        '''

        self.icon = QtWidgets.QLabel(self.widget)
        self.icon.setMinimumSize(QtCore.QSize(100, 150))
        self.icon.setMaximumSize(QtCore.QSize(150, 150))
        self.icon.setPixmap(QtGui.QPixmap("Images/icon.png"))
        self.verticalLayout_3.addWidget(self.icon, 0, QtCore.Qt.AlignHCenter)

        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(50, 35, 59, -1)

        self.u_name_label = QtWidgets.QLabel(self.widget)
        self.u_name_label.setStyleSheet("color: rgb(231, 231, 231);\n"
                                        "font: 15pt \"Verdana\";")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.u_name_label)

        self.uname_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.uname_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.uname_lineEdit.setStyleSheet("QLineEdit {\n"
                                          "color: rgb(231, 231, 231);\n"
                                          "font: 15pt \"Verdana\";\n"
                                          "border: None;\n"
                                          "border-bottom-color: white;\n"
                                          "border-radius: 10px;\n"
                                          "padding: 0 8px;\n"
                                          "background: rgb(20, 20, 40);\n"
                                          "selection-background-color: darkgray;\n"
                                          "}")
        self.uname_lineEdit.setFocus(True)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uname_lineEdit)
        '''
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        '''
        self.pass_label = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pass_label)
        '''
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
                                      "color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        '''
        self.pass_lineEdit = PasswordEdit(self.widget)
        self.pass_lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.pass_lineEdit.setStyleSheet("QLineEdit {\n"
                                         "color: orange;\n"
                                         "font: 15pt \"Verdana\";\n"
                                         "border: None;\n"
                                         "border-bottom-color: white;\n"
                                         "border-radius: 10px;\n"
                                         "padding: 0 8px;\n"
                                         "background: rgb(20, 20, 40);\n"
                                         "selection-background-color: darkgray;\n"
                                         "}")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pass_lineEdit)
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border: 2px solid white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        '''
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setStyleSheet("border: 2px solid white;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        '''
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid orange;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)

        self.login_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())

        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.login_btn.setAutoFillBackground(False)
        self.login_btn.setStyleSheet("color: rgb(231, 231, 231);\n"
                                     "font: 17pt \"Verdana\";\n"
                                     "border: 2px solid orange;\n"
                                     "padding: 5px;\n"
                                     "border-radius: 3px;\n"
                                     "opacity: 200;\n"
                                     "")
        self.login_btn.setAutoDefault(True)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.login_btn)

        self.checkButton = QtWidgets.QPushButton(self.widget)
        self.checkButton.setMinimumSize(QtCore.QSize(0, 60))
        self.checkButton.setStyleSheet("color: rgb(231, 231, 231);\n"
                                       "font: 17pt \"Verdana\";\n"
                                       "border: 2px solid orange;\n"
                                       "padding: 5px;\n"
                                       "border-radius: 3px;\n"
                                       "opacity: 200;\n"
                                       "")
        self.checkButton.setDefault(False)
        self.checkButton.setFlat(False)
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.checkButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.verticalLayout_3.addLayout(self.formLayout_2)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        ######################### Button Event ##############################3
        self.login_btn.clicked.connect(self.loginCheck)
        #####################################################################
        ######################### Button Event ##############################3
        # self.signup_btn.clicked.connect(self.signUpCheck)
        #####################################################################
        ######################### Button Event ##############################3
        self.checkButton.clicked.connect(self.DBConnection)
        #####################################################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.login_btn_3.setText(_translate("Form", "X"))
        self.u_name_label.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/user_32x32.png\"/></p></body></html>"))
        self.pass_label.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/lock_or_32x32.png\"/></p></body></html>"))
        '''
        self.label_4.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/mail_32x32.png\"/></p></body></html>"))
        '''
        self.login_btn.setText(_translate("Form", "Sign In"))
        self.checkButton.setText(_translate("Form", "Check Connection"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



