

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import numpy as np
class Ui_ThresholdGUI(object):

    def __init__(self, Dialog):
        self.dialog = Dialog


    def processimg(self):
        img = "BCET.jpg"
        self.lineEdit.setText(img)

    def submit(self):

        try:
            bcet_image = self.lineEdit.text()
            image = cv2.imread('images/'+str(bcet_image))
            blur = cv2.GaussianBlur(image, (5, 5), 0)
            #cv2.imshow("blur", blur)
            T,thresh= cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
            img_otsu=self.Otsuthreshold(thresh)
            cv2.imwrite('images/threshld.jpg', img_otsu)
            self.showMessageBox("Information", "Thresholding completed..!")
            cv2.imshow("Thresholding", img_otsu)
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

    def Otsuthreshold(self,image):
        try:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            img_out = image.copy()
            height = image.shape[0]
            width = image.shape[1]

            for i in np.arange(5, height - 5):
                for j in np.arange(5, width - 5):
                    neighbors = []
                    for k in np.arange(-6, 6):
                        for l in np.arange(-6, 6):
                            a = image.item(i + k, j + l)
                            neighbors.append(a)
                    neighbors.sort()
                    median = neighbors[24]
                    b = median
                    img_out.itemset((i, j), b)

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        return img_out.astype(np.uint8)

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
        Dialog.setWindowTitle(_translate("Dialog", "Thresholding"))
        self.label.setText(_translate("Dialog", "Thresholding"))
        self.label_2.setText(_translate("Dialog", " Filter  Image"))
        self.pushButton_3.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ThresholdGUI(Dialog)
    ui.setupUi(Dialog)
    ui.processimg()
    Dialog.show()
    sys.exit(app.exec_())
