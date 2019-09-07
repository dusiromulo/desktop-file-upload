# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop File Upload Qt Project\FileUpload\file_upload_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 80)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filename = QtWidgets.QLabel(Form)
        self.filename.setObjectName("filename")
        self.horizontalLayout_2.addWidget(self.filename)
        self.percentage = QtWidgets.QProgressBar(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentage.sizePolicy().hasHeightForWidth())
        self.percentage.setSizePolicy(sizePolicy)
        self.percentage.setProperty("value", 24)
        self.percentage.setObjectName("percentage")
        self.horizontalLayout_2.addWidget(self.percentage)
        self.time_prevision = QtWidgets.QLabel(Form)
        self.time_prevision.setObjectName("time_prevision")
        self.horizontalLayout_2.addWidget(self.time_prevision)
        self.cancel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setMinimumSize(QtCore.QSize(75, 0))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.filename.setText(_translate("Form", "Filename"))
        self.time_prevision.setText(_translate("Form", "Tempo restante: N/A"))
        self.cancel.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
