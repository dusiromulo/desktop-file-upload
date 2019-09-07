import time
from PyQt5.QtCore import QThread, pyqtSignal


class UploadThread(QThread):
    sig_new_percentage = pyqtSignal(str)
    percentage = 0

    def __init__(self, parent=None, file_path=""):
        QThread.__init__(self, parent)
        self.file_path = file_path
        self.running = False

    def on_cancel_upload(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.percentage += 1
            self.sig_new_percentage.emit(self.percentage)
            time.sleep(1)
