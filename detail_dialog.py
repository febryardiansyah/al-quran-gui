
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 446)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName("label")
        self.label.setFixedSize(300, 10)
        
        self.lcdJumlahSurat = QtWidgets.QLCDNumber(Dialog)
        self.lcdJumlahSurat.setGeometry(QtCore.QRect(300, 10, 81, 30))
        self.lcdJumlahSurat.setStyleSheet("color:red;\n"
"font-weight: bold;")
        self.lcdJumlahSurat.setObjectName("lcdJumlahSurat")
        
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 591, 381))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setItemAlignment(QtCore.Qt.AlignRight)
        

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(300,10)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.closeFun)
    
    def closeFun(self):
        print('close')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Surat"))
        self.label.setText(_translate("Dialog",'Nama Surat'))
        self.label_2.setText(_translate("Dialog", "Arti Indonesia"))
        self.pushButton.setText(_translate("Dialog", "Close"))
    def getSurat(self,data):
        suratList = data['ayahs']
        self.label.setText('Nama Surat :\t'+data['englishName'])
        self.label_2.setText('Arti :\t'+data['idNameTranslation'])
        self.lcdJumlahSurat.display(data['numberOfAyahs'])
        for item in suratList:
            self.listWidget.addItem(item['text']['arab'])
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
