import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot


class UploadThread(QThread):
    sig_new_percentage = pyqtSignal(int, int)
    sig_cancel_upload = pyqtSignal()
    percentage = 0

    def __init__(self, parent=None, file_path=""):
        QThread.__init__(self, parent)
        self.file_path = file_path
        self.running = False
        self.sig_cancel_upload.connect(self.on_cancel_upload)

    @pyqtSlot()
    def on_cancel_upload(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            total_diff = 2
            self.percentage += total_diff
            if self.percentage >= 100:
                self.sig_new_percentage.emit(100, total_diff)
                break
            else:
                self.sig_new_percentage.emit(self.percentage, total_diff)
            time.sleep(1)
