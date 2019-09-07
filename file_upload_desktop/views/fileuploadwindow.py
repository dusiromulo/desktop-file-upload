# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop File Upload Qt Project\FileUpload\fileuploadscreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileUploadWindow(object):
    def setupUi(self, FileUploadWindow):
        FileUploadWindow.setObjectName("FileUploadWindow")
        FileUploadWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileUploadWindow.sizePolicy().hasHeightForWidth())
        FileUploadWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(FileUploadWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uploadframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadframe.sizePolicy().hasHeightForWidth())
        self.uploadframe.setSizePolicy(sizePolicy)
        self.uploadframe.setMinimumSize(QtCore.QSize(0, 0))
        self.uploadframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploadframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uploadframe.setObjectName("uploadframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uploadframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.uploadframe)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.file_path = QtWidgets.QLineEdit(self.uploadframe)
        self.file_path.setObjectName("file_path")
        self.horizontalLayout.addWidget(self.file_path)
        self.open = QtWidgets.QPushButton(self.uploadframe)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(self.uploadframe)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.upload = QtWidgets.QPushButton(self.frame)
        self.upload.setObjectName("upload")
        self.horizontalLayout_2.addWidget(self.upload)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout.addWidget(self.uploadframe)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uploads = QtWidgets.QListWidget(self.groupBox)
        self.uploads.setObjectName("uploads")
        self.verticalLayout_2.addWidget(self.uploads)
        self.verticalLayout.addWidget(self.groupBox)
        FileUploadWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FileUploadWindow)
        QtCore.QMetaObject.connectSlotsByName(FileUploadWindow)

    def retranslateUi(self, FileUploadWindow):
        _translate = QtCore.QCoreApplication.translate
        FileUploadWindow.setWindowTitle(_translate("FileUploadWindow", "Upload de arquivos"))
        self.label_2.setText(_translate("FileUploadWindow", "Escolher arquivo: "))
        self.open.setText(_translate("FileUploadWindow", "Abrir"))
        self.upload.setText(_translate("FileUploadWindow", "Fazer upload"))
        self.groupBox.setTitle(_translate("FileUploadWindow", "Status dos uploads"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileUploadWindow = QtWidgets.QMainWindow()
    ui = Ui_FileUploadWindow()
    ui.setupUi(FileUploadWindow)
    FileUploadWindow.show()
    sys.exit(app.exec_())
