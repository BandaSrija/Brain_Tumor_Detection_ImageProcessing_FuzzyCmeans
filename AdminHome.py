

from PyQt5 import QtCore, QtGui, QtWidgets
from ImageAcquisition import Ui_ImageAcquisition
from FuzzyGUI import Ui_FuzzyGUI
from ThresholdGUI import Ui_ThresholdGUI
from Preprocessing import Ui_Preprocessing
import cv2
class Ui_AdminHome(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def imageacquition(self):

        self.home = QtWidgets.QDialog()
        self.ui = Ui_ImageAcquisition(self.home)
        self.ui.setupUi(self.home)
        self.home.show()

    def preprocessing(self):

        self.home = QtWidgets.QDialog()
        self.ui = Ui_Preprocessing(self.home)
        self.ui.setupUi(self.home)
        self.ui.processimg()
        self.home.show()

    def fuzzyclustering(self):
        self.home = QtWidgets.QDialog()
        self.ui = Ui_FuzzyGUI(self.home)
        self.ui.setupUi(self.home)
        self.ui.processimg()
        self.home.show()

    def thresholding(self):
        self.home = QtWidgets.QDialog()
        self.ui =  Ui_ThresholdGUI(self.home)
        self.ui.setupUi(self.home)
        self.ui.processimg()
        self.home.show()

    def segmentation(self):
        brain = cv2.imread('images/FCM.jpg')
        tumor = cv2.imread('images/threshld.jpg')
        segimg = cv2.addWeighted(brain, 0.5, tumor, 0.7, 0)
        cv2.imwrite('images/segimg.jpg', segimg)
        cv2.imshow("Segmentation", segimg)

    def dataanalysis(self):

        try:

            detected_edges = cv2.Canny(cv2.imread('images/segimg.jpg'), 10, 10 * 3, 5)
            colour = cv2.applyColorMap(cv2.imread('images/segimg.jpg'), cv2.COLORMAP_JET)
            cv2.imshow("Color Map", colour)
            cv2.imshow("Canny Edge Detector", detected_edges)
            cv2.waitKey()

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 467)
        Dialog.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 211, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.imageacquition)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 210, 211, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.preprocessing)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 310, 211, 41))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fuzzyclustering)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 110, 211, 41))
        self.pushButton_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.thresholding)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 210, 211, 41))
        self.pushButton_5.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.segmentation)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(380, 310, 211, 41))
        self.pushButton_6.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.dataanalysis)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Home"))
        self.pushButton.setText(_translate("Dialog", "Image Acquisition"))
        self.pushButton_2.setText(_translate("Dialog", "Preprocessing"))
        self.pushButton_3.setText(_translate("Dialog", "Fuzzy C-Means"))
        self.pushButton_4.setText(_translate("Dialog", "Thresholding"))
        self.pushButton_5.setText(_translate("Dialog", "Segmentation"))
        self.pushButton_6.setText(_translate("Dialog", "Data Analysis"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_AdminHome(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
