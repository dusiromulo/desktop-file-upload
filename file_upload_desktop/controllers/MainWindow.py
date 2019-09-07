import ctypes
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QSystemTrayIcon, QMenu, QListWidgetItem

from views.fileuploadwindow import Ui_FileUploadWindow
from views.fileuploaditem import Ui_Form as UploadListItem


class MainWindow(QMainWindow):
    app_id = 'com.romulodusi.desktopupload'

    def __init__(self, app):
        QMainWindow.__init__(self)
        # Config app id to show app icon on taskbar
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.app_id)

        # Config app icon
        app_icon = QtGui.QIcon("assets/icon.png")
        self.setWindowIcon(app_icon)

        # self.loginWindow = Ui_LoginWindow()
        # self.loginWindow.setupUi(mainWindow)

        self.file_upload_window = Ui_FileUploadWindow()
        self.file_upload_window.setupUi(self)
        self.file_upload_window.file_path.setText("path file")
        self.file_upload_window.upload.clicked.connect(self.add_file_to_upload_list)
        self.file_upload_window.open.clicked.connect(self.open_file_dialog)

        self.uploads_widgets = []

        self.tray_icon = QSystemTrayIcon(app_icon, self)
        self.tray_icon.activated.connect(self.tray_icon_event)
        menu = QMenu(self)
        quit_action = menu.addAction("Fechar aplicação")
        quit_action.triggered.connect(app.quit)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def add_file_to_upload_list(self):
        item_widget = QWidget()
        item_raw = UploadListItem()
        item_raw.setupUi(item_widget)

        item = QListWidgetItem(self.file_upload_window.uploads)
        item.setSizeHint(item_widget.sizeHint())
        self.file_upload_window.uploads.addItem(item)
        self.file_upload_window.uploads.setItemWidget(item, item_widget)
        self.uploads_widgets.append(item_widget)

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file')
        self.file_upload_window.file_path.setText(filename[0])

    def tray_icon_event(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if not self.isVisible():
                self.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("File upload", "Aplicação foi minimizada", QSystemTrayIcon.Information, 1000)
