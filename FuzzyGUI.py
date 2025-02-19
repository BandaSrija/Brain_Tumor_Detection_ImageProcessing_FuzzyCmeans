

from PyQt5 import QtCore, QtGui, QtWidgets
from FuzzyClustering import FCM
import cv2
class Ui_FuzzyGUI(object):

    def __init__(self, Dialog):
        self.dialog = Dialog


    def processimg(self):
        img = "bilateral.jpg"
        self.lineEdit.setText(img)

    def submit(self):

        try:
            amf_image = self.lineEdit.text()
            image_fcm = FCM(amf_image)
            self.showMessageBox("Information", "Fuzzy C-Means Clustering completed..!")
            cv2.imshow("Fuzzy C-Means Clustering", image_fcm)
            cv2.waitKey(0)
            self.dialog.hide()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 409)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 80);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 50, 341, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 151, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 411, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 230, 121, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(170, 85, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.submit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fuzzy C-Means"))
        self.label.setText(_translate("Dialog", "Fuzzy C-Means Clustering"))
        self.label_2.setText(_translate("Dialog", " Filter  Image"))
        self.pushButton_3.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_FuzzyGUI(Dialog)
    ui.setupUi(Dialog)
    ui.processimg()
    Dialog.show()
    sys.exit(app.exec_())
