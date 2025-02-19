

from PyQt5 import QtCore, QtGui, QtWidgets
from AMF import newfilters
import cv2
from BCET import BalanceContrastEnhancementTechnique
import sys
class Ui_Preprocessing(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def processimg(self):
        path="images/resize.jpg"
        self.lineEdit.setText(path)

    def bilateral_filter(self):
        try:
            image = self.lineEdit.text()
            img = cv2.imread(image)  # Load image
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # gb = cv2.GaussianBlur(gray_image, (3, 3), 1, 1)
            bilateral = cv2.bilateralFilter(gray_image, 9, 275, 250)
            cv2.imwrite('images/bilateral.jpg', bilateral)
            self.showMessageBox("Information", "Removed noisy data by Bilateral")
            cv2.imshow(" Bilateral Filter", bilateral)
            cv2.waitKey(0)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def BCET(self):
        try:
            gray_image = self.lineEdit.text()
            gray_image = cv2.imread(gray_image)
            gray_image = cv2.cvtColor(gray_image, cv2.COLOR_BGR2GRAY)
            image_bcet=BalanceContrastEnhancementTechnique(gray_image)
            self.showMessageBox("Information", "Highlighting the area of interest is done by BCET")
            #cv2.imwrite('images/BCET.jpg', image_bcet)
            cv2.imshow("BCET", image_bcet)
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
        Dialog.setStyleSheet("background-color: rgb(98, 32, 49);")
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
        self.pushButton_3.setGeometry(QtCore.QRect(170, 240, 121, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(170, 85, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bilateral_filter)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 240, 121, 31))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(43, 61, 91);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.BCET)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Preprocessing"))
        self.label.setText(_translate("Dialog", " Image Preprocessing"))
        self.label_2.setText(_translate("Dialog", "Gray Color Image"))
        self.pushButton_3.setText(_translate("Dialog", "Bilateral"))
        self.pushButton_4.setText(_translate("Dialog", "BCET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Preprocessing(Dialog)
    ui.setupUi(Dialog)
    ui.processimg()
    Dialog.show()
    sys.exit(app.exec_())
