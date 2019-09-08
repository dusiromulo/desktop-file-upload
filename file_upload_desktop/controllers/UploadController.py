import datetime
from PyQt5.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QMessageBox

from views.fileuploadwindow import Ui_FileUploadWindow
from views.fileuploaditem import Ui_Form as UploadListItem

from utils.UploadThread import UploadThread


class UploadController:
    def __init__(self, main_window, username):
        self.main_window = main_window
        self.username = username

        self.upload_window = Ui_FileUploadWindow()
        self.upload_window.setupUi(main_window)
        self.upload_window.file_path.setText("")

        self.uploads_widgets = []
        self.register_callbacks()

    def register_callbacks(self):
        self.upload_window.upload.clicked.connect(self.add_file_to_upload_list)
        self.upload_window.open.clicked.connect(self.open_file_dialog)

    def cb_upload_success(self, item):
        item.percentage.setProperty('value', 100)
        text = 'Upload completo!'
        item.time_prevision.setText(text)
        item.cancel.setDisabled(True)

    def cb_upload_failure(self, item):
        text = 'Upload falhou!'
        item.time_prevision.setText(text)
        item.cancel.setDisabled(True)

    def add_file_to_upload_list(self):
        file_path = self.upload_window.file_path.text()
        if file_path != "":
            self.upload_window.file_path.setText('')
            item_widget = QWidget()
            item_raw = UploadListItem()
            item_raw.setupUi(item_widget)
            item_raw.filename.setText(file_path.split('/')[-1])
            item_raw.cancel.clicked.connect(lambda: self.cancel_upload(item_raw))
            item_raw.percentage.setProperty('value', 0)
            item = QListWidgetItem(self.upload_window.uploads)
            item.setSizeHint(item_widget.sizeHint())
            self.upload_window.uploads.addItem(item)
            self.upload_window.uploads.setItemWidget(item, item_widget)
            thread = UploadThread(file_path, self.username)
            thread.start()
            thread.sig_new_percentage.connect(lambda perc, diff: self.update_item_percentage(thread, item_raw, perc, diff))
            thread.sig_failure.connect(lambda: self.cb_upload_failure(item_raw))
            thread.sig_success.connect(lambda: self.cb_upload_success(item_raw))
            self.uploads_widgets.append((item_raw, thread))
        else:
            # Open alert message
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setWindowTitle('Arquivo não selecionado')
            alert.setText('Por favor, selecione um arquivo para realizar upload')
            alert.setStandardButtons(QMessageBox.Ok)
            alert.setWindowIcon(self.main_window.app_icon)
            alert.exec_()

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(self.main_window, 'Abrir arquivo')
        self.upload_window.file_path.setText(filename[0])

    def cancel_upload(self, item_widget):
        for item in self.uploads_widgets:
            if item[0] == item_widget:
                if item[1].isRunning():
                    item[1].terminate()
                item_widget.time_prevision.setText('Upload cancelado')
                item_widget.cancel.setDisabled(True)

    def update_item_percentage(self, thread, item, percentage, diff):
        now = datetime.datetime.now()
        item.percentage.setProperty("value", percentage)
        if percentage >= 100:
            text = 'Upload completo!'
            item.time_prevision.setText(text)
            return
        if diff > 0:
            if thread.now == 0:
                thread.now = now
                return
            timedelta = (now - thread.now).total_seconds()
            if timedelta > 0.0000001:
                total_secs_remaining = int((100 - percentage) * (timedelta / diff))
                total_mins_remaining = int(total_secs_remaining / 60)
                total_hours_remaining = int(total_mins_remaining / 60)
                remaining_str = '{:02d}:{:02d}:{:02d}'\
                    .format(total_hours_remaining, total_mins_remaining % 60, total_secs_remaining % 60)
                text = 'Tempo restante: ' + remaining_str
                item.time_prevision.setText(text)
                thread.now = now
