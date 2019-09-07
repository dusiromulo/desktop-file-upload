import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMainWindow, QFileDialog, QSystemTrayIcon, QMenu, QListWidgetItem, QMessageBox

from views.loginwindow import Ui_LoginWindow
from views.fileuploadwindow import Ui_FileUploadWindow
from views.fileuploaditem import Ui_Form as UploadListItem
from .UploadThread import UploadThread


class MainWindow(QMainWindow):
    app_id = 'com.romulodusi.desktopupload'

    def __init__(self, app):
        QMainWindow.__init__(self)
        # Config app id to show app icon on taskbar
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.app_id)

        # Config app icon
        self.app_icon = QtGui.QIcon("assets/icon.png")
        self.setWindowIcon(self.app_icon)

        # self.loginWindow = Ui_LoginWindow()
        # self.loginWindow.setupUi(self)

        self.file_upload_window = Ui_FileUploadWindow()
        self.file_upload_window.setupUi(self)
        self.file_upload_window.file_path.setText("")
        self.file_upload_window.upload.clicked.connect(self.add_file_to_upload_list)
        self.file_upload_window.open.clicked.connect(self.open_file_dialog)

        self.uploads_widgets = []

        self.tray_icon = QSystemTrayIcon(self.app_icon, self)
        self.tray_icon.activated.connect(self.tray_icon_event)
        menu = QMenu(self)
        quit_action = menu.addAction("Fechar aplicação")
        quit_action.triggered.connect(app.quit)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def add_file_to_upload_list(self):
        file_path = self.file_upload_window.file_path.text()
        if file_path != "":
            self.file_upload_window.file_path.setText('')
            thread = UploadThread()
            item_widget = QWidget()
            item_raw = UploadListItem()
            item_raw.setupUi(item_widget)
            item_raw.filename.setText(file_path.split('/')[-1])
            item_raw.cancel.clicked.connect(lambda: self.cancel_upload(item_raw))
            item_raw.percentage.setProperty('value', 0)
            item = QListWidgetItem(self.file_upload_window.uploads)
            item.setSizeHint(item_widget.sizeHint())
            self.file_upload_window.uploads.addItem(item)
            self.file_upload_window.uploads.setItemWidget(item, item_widget)
            self.uploads_widgets.append((item_raw, thread))
            thread.start()
            thread.sig_new_percentage.connect(lambda perc, diff: self.update_item_percentage(item_raw, perc, diff))
        else:
            # Open alert message
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setWindowTitle('Arquivo não selecionado')
            alert.setText('Por favor, selecione um arquivo para realizar upload')
            alert.setStandardButtons(QMessageBox.Ok)
            alert.setWindowIcon(self.app_icon)
            alert.exec_()

    def cancel_upload(self, item_widget):
        for item in self.uploads_widgets:
            if item[0] == item_widget:
                if item[1].isRunning():
                    item[1].sig_cancel_upload.emit()
                item_widget.time_prevision.setText('Upload cancelado')
                item_widget.cancel.setDisabled(True)

    @QtCore.pyqtSlot()
    def update_item_percentage(self, item, percentage, diff):
        item.percentage.setProperty("value", percentage)
        if percentage == 100:
            text = 'Upload completo!'
            item.time_prevision.setText(text)
            return
        total_secs_remaining = int((100 - percentage) / diff)
        total_mins_remaining = int(total_secs_remaining / 60)
        total_hours_remaining = int(total_mins_remaining / 60)
        remaining_str = '{:02d}:{:02d}:{:02d}'\
            .format(total_hours_remaining, total_mins_remaining % 60, total_secs_remaining % 60)
        text = 'Tempo restante: ' + remaining_str
        item.time_prevision.setText(text)

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir arquivo')
        self.file_upload_window.file_path.setText(filename[0])

    def tray_icon_event(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if not self.isVisible():
                self.show()

    # When user clicks on window quit button
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("File upload", "Aplicação foi minimizada", QSystemTrayIcon.Information, 1000)
